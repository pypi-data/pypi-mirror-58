#!/usr/bin/env python
# -*- coding: utf-8 -*-

__all__ = ["SQLRow", "SQLRowCollection", "SQLParser", "Connection", "Database", "MultipleDatabase"]

import os, re
from inspect import isclass
from collections import OrderedDict
from contextlib import contextmanager

from sqlalchemy import (
    create_engine,
    exc,
    inspect,
    text
)


class SQLRow(dict):
    def __init__(self, keys, values):
        assert len(keys) == len(values)
        super(SQLRow, self).__init__(zip(keys, values))
        self.cursor_description = [x for x in keys]

    def __repr__(self):
        return "<{} {}>".format(self.__class__.__name__, super(SQLRow, self).__repr__())

    def __getitem__(self, key):
        if isinstance(key, int):
            if key > len(self.cursor_description):
                raise IndexError("data index out of range")
            key = self.cursor_description[key]
            return super(SQLRow, self).__getitem__(key)

        if key in self.cursor_description:
            return super(SQLRow, self).__getitem__(key)

        raise KeyError("SQLRow contains no '{}' field.".format(key))

    def __getattr__(self, key):
        if key in self.cursor_description:
            return super(SQLRow, self).__getitem__(key)
        return None

    def __len__(self):
        return len(self.cursor_description)

    def as_dict(self, ordered=False):
        return OrderedDict(self) if ordered else dict(self)

    def __getstate__(self):
        return self.as_dict()

    def __setstate__(self, state):
        self.__init__(state.keys(), state.values())


class SQLRowCollection(object):
    def __init__(self, rows):
        self._rows = rows
        self._all_rows = []
        self.pending = True

    def __repr__(self):
        return '<SQLRowCollection size={} pending={}>'.format(len(self), self.pending)

    def __iter__(self):
        i = 0
        while True:
            if i < len(self):
                yield self[i]
            else:
                try:
                    yield next(self)
                except StopIteration:
                    return
            i += 1

    def next(self):
        return self.__next__()

    def __next__(self):
        try:
            nextrow = next(self._rows)
            self._all_rows.append(nextrow)
            return nextrow
        except StopIteration:
            self.pending = False
            raise StopIteration('SQLRowCollection contains no more rows.')

    def __getitem__(self, key):
        is_int = isinstance(key, int)

        if is_int:
            key = slice(key, key + 1)

        while len(self) < key.stop or key.stop is None:
            try:
                next(self)
            except StopIteration:
                break

        rows = self._all_rows[key]
        if is_int:
            return rows[0]
        else:
            return SQLRowCollection(iter(rows))

    def __len__(self):
        return len(self._all_rows)

    def list(self, as_dict=False, as_ordereddict=False):
        rows = list(self)

        if as_dict:
            return [r.as_dict() for r in rows]
        elif as_ordereddict:
            return [r.as_dict(ordered=True) for r in rows]

        return rows

    def as_dict(self, ordered=False):
        return self.list(as_dict=not (ordered), as_ordereddict=ordered)

    def first(self, default=None, as_dict=False, as_ordereddict=False):
        try:
            record = self[0]
        except IndexError:
            if isexception(default):
                raise default
            return default

        if as_dict:
            return record.as_dict()
        elif as_ordereddict:
            return record.as_dict(ordered=True)
        else:
            return record

    def one(self, default=None, as_dict=False, as_ordereddict=False):
        try:
            self[1]
        except IndexError:
            return self.first(default=default, as_dict=as_dict, as_ordereddict=as_ordereddict)
        else:
            raise ValueError('SQLRowCollection contained more than one row. '
                             'Expects only one row when using '
                             'SQLRowCollection.one')

    def scalar(self, default=None):
        row = self.one()
        return row[0] if row else default


def isexception(obj):
    if isinstance(obj, Exception):
        return True
    if isclass(obj) and issubclass(obj, Exception):
        return True
    return False


class SQLParser:
    params_mark = "_LeafPy_argv_"

    @staticmethod
    def select(query, *args, **kwargs):
        """转换查询语句"""
        paramstyle_count = query.count('?')

        # 参数长度和query字符串中的?个数必须一致
        assert len(args) == paramstyle_count

        keys = kwargs.keys()
        if paramstyle_count == 0 and len(keys) <= 0:
            return query, {}

        params = {}
        if paramstyle_count > 0:
            query_list = query.split('?')
            param_len = len(query_list)
            result = []
            for i, q in enumerate(query_list):
                result.append(q)
                if param_len > (i + 1):
                    result.append(":%s%d" % (SQLParser.params_mark, i))
            query = "".join(result)
            for i, argv in enumerate(args):
                _key = "%s%d" % (SQLParser.params_mark, i)
                params.update({_key: argv})

        if len(keys) > 0:
            extparams = []
            for key in keys:
                extparams.append("%s=:%s" % (key, key))
            extparams_str = " AND ".join(extparams)
            ret = re.findall("where", query, flags=re.IGNORECASE)
            if len(ret) > 0:
                extparams_str = "WHERE (%s) AND" % extparams_str
                query = re.sub("where", extparams_str, query, flags=re.IGNORECASE)
            else:
                extparams_str = "WHERE %s" % extparams_str
                query = "%s %s" % (query, extparams_str)
            params.update(kwargs)

        return query, params

    @staticmethod
    def insert(table, **kwargs):
        """转换插入语句"""
        keys = kwargs.keys()
        params = []
        values = []
        for key in keys:
            params.append(key)
            values.append(":%s" % key)
        return "INSERT INTO %s (%s) VALUES (%s)" % (table, ",".join(params), ",".join(values))

    @staticmethod
    def update(table, *args, **kwargs):
        """转换更新语句"""
        where = kwargs.pop("where", None)
        sqls = ["UPDATE %s SET" % table]

        keys = kwargs.keys()
        params = []
        for key in keys:
            params.append("%s=:%s" % (key, key))
        sqls.append(",".join(params))

        if where:
            sqls.append("WHERE")
            paramstyle_count = where.count('?')
            assert len(args) == paramstyle_count

            where_list = where.split('?')
            where_len = len(where_list)
            where_result = []
            for i, w in enumerate(where_list):
                where_result.append(w)
                if where_len > (i + 1):
                    where_result.append(":%s%d" % (SQLParser.params_mark, i))
            where = "".join(where_result)
            sqls.append(where)

            params = {}
            for i, argv in enumerate(args):
                _key = "%s%d" % (SQLParser.params_mark, i)
                params.update({_key: argv})
            kwargs.update(params)
        return " ".join(sqls), kwargs

    @staticmethod
    def delete(table, *args, **kwargs):
        """转换删除语句"""
        where = kwargs.pop("where", None)
        sqls = ["DELETE FROM %s" % table]

        keys = kwargs.keys()
        if len(keys) > 0:
            sqls.append("WHERE")
            result = []
            for key in keys:
                result.append("%s=:%s" % (key, key))
            sqls.append("(")
            sqls.append(" AND ".join(result))
            sqls.append(")")

        if where:
            if "WHERE" in sqls:
                sqls.append("AND")

            paramstyle_count = where.count('?')
            assert len(args) == paramstyle_count

            where_list = where.split('?')
            where_len = len(where_list)
            where_result = []
            for i, w in enumerate(where_list):
                where_result.append(w)
                if where_len > (i + 1):
                    where_result.append(":%s%d" % (SQLParser.params_mark, i))
            where = "".join(where_result)
            sqls.append(where)

            params = {}
            for i, argv in enumerate(args):
                _key = "%s%d" % (SQLParser.params_mark, i)
                params.update({_key: argv})
            kwargs.update(params)
        return " ".join(sqls), kwargs


class Connection(object):
    def __init__(self, connection):
        self._conn = connection
        self._dbtype = (connection.engine.name or "").lower().strip()
        self.open = not connection.closed

    def close(self):
        self._conn.close()
        self.open = False

    def __enter__(self):
        return self

    def __exit__(self, exc, val, traceback):
        self.close()

    def __repr__(self):
        return '<Connection open={}>'.format(self.open)

    def query(self, query, fetchall=False, **params):
        cursor = self._conn.execute(text(query), **params)
        row_gen = (SQLRow(cursor.keys(), row) for row in cursor)
        results = SQLRowCollection(row_gen)
        if fetchall:
            results.list()
        return results

    def bulk_query(self, query, *multiparams):
        self._conn.execute(text(query), *multiparams)

    def query_file(self, path, fetchall=False, **params):
        if not os.path.exists(path):
            raise IOError("File '{}' not found!".format(path))
        if os.path.isdir(path):
            raise IOError("'{}' is a directory!".format(path))
        with open(path) as f:
            query = f.read()
        return self.query(query=query, fetchall=fetchall, **params)

    def bulk_query_file(self, path, *multiparams):
        if not os.path.exists(path):
            raise IOError("File '{}'' not found!".format(path))
        if os.path.isdir(path):
            raise IOError("'{}' is a directory!".format(path))
        with open(path) as f:
            query = f.read()
        self._conn.execute(text(query), *multiparams)

    def select(self, query, *args, **kwargs):
        """SELECT 语句"""
        _test = kwargs.pop("_test", False)
        _fetchall = True if self._dbtype == "mssql" else False
        fetchall = kwargs.pop("fetchall", _fetchall)
        query, params = SQLParser.select(query, *args, **kwargs)
        if _test:
            return query, params
        return True, self.query(query, fetchall=fetchall, **params)

    def selectone(self, query, *args, **kwargs):
        """SELECT 第一个结果"""
        _test = kwargs.pop("_test", False)
        _fetchall = True if self._dbtype == "mssql" else False
        fetchall = kwargs.pop("fetchall", _fetchall)

        query, params = SQLParser.select(query, *args, **kwargs)
        if _test:
            return query, params

        row = self.query(query, fetchall=fetchall, **params).first()
        if not row:
            return False, row
        return True, row

    def insert(self, table, **kwargs):
        """插入单条数据"""
        _test = kwargs.pop("_test", False)
        query = SQLParser.insert(table, **kwargs)
        if _test:
            return query, kwargs

        return True, self.query(query, **kwargs)

    def multiple_insert(self, table, values, **kwargs):
        """同时插入多条数据"""
        if not isinstance(values, list):
            return ValueError("values must be a list for dict.")

        if len(values) <= 0:
            if len(kwargs) > 0:
                return self.insert(table, **kwargs)
            return ValueError("values must be not empty.")

        _test = kwargs.pop("_test", False)
        query = SQLParser.insert(table, **values[0])
        if _test:
            return query, values

        return True, self.bulk_query(query, values)

    def update(self, table, *args, **kwargs):
        """更新数据"""
        _test = kwargs.pop("_test", False)
        where = kwargs.pop("where", None)

        if not where:
            # 从第一个参数获取where语句
            if len(args) > 0:
                where = args[0]
                args = args[1:]
        if where:
            kwargs.update(dict(where=where))

        query, params = SQLParser.update(table, *args, **kwargs)
        if _test:
            return query, params

        return True, self.query(query, **params)

    def delete(self, table, *args, **kwargs):
        """删除数据"""
        _test = kwargs.pop("_test", False)
        where = kwargs.pop("where", None)

        if not where:
            # 从第一个参数获取where语句
            if len(args) > 0:
                where = args[0]
                args = args[1:]
        if where:
            kwargs.update(dict(where=where))

        query, params = SQLParser.delete(table, *args, **kwargs)
        if _test:
            return query, params

        return True, self.query(query, **params)

    def transaction(self):
        return self._conn.begin()


class Database(object):
    # 定义默认的数据库驱动字典
    engines = {
        "mssql": "pymssql",
        "mysql": "pymysql",
        "oracle": "cx_oracle",
        "postgresql": "psycopg2"
    }

    def __init__(self, db_url=None, **kwargs):
        if not db_url:
            db_url, kwargs = self.gen_dburl(**kwargs)

        # Create an engine.
        self._engine = create_engine(db_url, **kwargs)
        self.open = True
        self.version = None

    def gen_dburl(self, **kwargs):
        """
        自定义从字典中获取链接串
        """
        engine = kwargs.pop("ENGINE", None)
        if not engine:
            return None

        driver = kwargs.pop("ODBC", self.engines.get(engine))
        if driver:
            engine = "%s+%s" % (engine, driver)

        dbname = kwargs.pop("NAME", None)
        if not dbname:
            return None

        user = kwargs.pop("USER", "")
        pwd = kwargs.pop("PASSWORD", kwargs.pop("PWD", ""))
        host = kwargs.pop("HOST", "127.0.0.1")
        port = kwargs.pop("PORT", None)
        if port:
            host = "%s:%s" % (host, port)
        charset = kwargs.pop("CHARSET", "utf8")

        echo = kwargs.pop("PRINTING", False)
        pool_size = kwargs.pop("CONNECTIONS", 5)
        pool_recycle = kwargs.pop("TIMEOUT", 3600)

        kwargs.update(dict(echo=echo, pool_size=pool_size, pool_recycle=pool_recycle))

        configs = {"engine": engine, "user": user, "pwd": pwd, "host": host, "dbname": dbname, "charset": charset}
        db_url = "{engine}://{user}:{pwd}@{host}/{dbname}?charset={charset}".format(**configs)
        return db_url, kwargs

    def close(self):
        self._engine.dispose()
        self.open = False

    def __enter__(self):
        return self

    def __exit__(self, exc, val, traceback):
        self.close()

    def __repr__(self):
        return '<Database open={}>'.format(self.open)

    def get_table_names(self, internal=False):
        # Setup SQLAlchemy for Database inspection.
        return inspect(self._engine).get_table_names()

    def get_version(self):
        if not self.version:
            _fetchall = True if self._engine.name.lower() == "mssql" else False
            self.version = self.query("select @@version", fetchall=_fetchall).first()[0]
        return self.version

    def get_connection(self):
        if not self.open:
            raise exc.ResourceClosedError('Database closed.')
        return Connection(self._engine.connect())

    def query(self, query, fetchall=False, **params):
        with self.get_connection() as conn:
            return conn.query(query, fetchall, **params)

    def bulk_query(self, query, *multiparams):
        with self.get_connection() as conn:
            conn.bulk_query(query, *multiparams)

    def query_file(self, path, fetchall=False, **params):
        with self.get_connection() as conn:
            return conn.query_file(path, fetchall, **params)

    def bulk_query_file(self, path, *multiparams):
        with self.get_connection() as conn:
            conn.bulk_query_file(path, *multiparams)

    @contextmanager
    def transaction(self):
        conn = self.get_connection()
        tx = conn.transaction()
        try:
            yield conn
            tx.commit()
        except Exception:
            tx.rollback()
        finally:
            conn.close()

    def select(self, query, *args, **kwargs):
        with self.get_connection() as conn:
            return conn.select(query, *args, **kwargs)

    def selectone(self, query, *args, **kwargs):
        with self.get_connection() as conn:
            return conn.selectone(query, *args, **kwargs)

    def insert(self, table, **kwargs):
        with self.get_connection() as conn:
            return conn.insert(table, **kwargs)

    def multiple_insert(self, table, values, **kwargs):
        with self.get_connection() as conn:
            return conn.multiple_insert(table, values, **kwargs)

    def update(self, table, *args, **kwargs):
        with self.get_connection() as conn:
            return conn.update(table, *args, **kwargs)

    def delete(self, table, *args, **kwargs):
        with self.get_connection() as conn:
            return conn.delete(table, *args, **kwargs)


class MultipleDatabase(object):
    def __init__(self, **kwargs):
        self._baseconn = kwargs.pop("_baseconn", "default")
        self._dbs = {}

        for k, v in kwargs.items():
            self._dbs[k] = Database(**v)

    def __len__(self):
        return len(self._dbs)

    def __repr__(self):
        return "MultipleDatabase {}".format(self._dbs)

    def __getattr__(self, name):
        if name in self._dbs:
            return self._dbs.get(name)
        elif (self._baseconn in self._dbs) and hasattr(self._dbs.get(self._baseconn), name):
            return getattr(self._dbs.get(self._baseconn), name)

        raise KeyError("not find database: %s in DB Config" % name)

    def close(self):
        for v in self._dbs.values():
            v.close()
