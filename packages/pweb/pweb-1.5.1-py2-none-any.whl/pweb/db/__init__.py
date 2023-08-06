#!/usr/bin/env python
# -*- coding: utf-8 -*-

__all__ = ["DbDialect", "database", "SQLConn", "BaseSQLClass", "sql"]

from .. import conf
from .client import SQLParser, Database as _DBS
from ..utils.py3helpers import string_types


class DbDialect:
    def __init__(self, dialect, version=None):
        self.params_mark = SQLParser.params_mark
        self.dialect = dialect
        self.version = version

    def _getversion(self):
        if not self.version:
            return None

        _vstr = self.version.upper()
        if self.dialect.lower() == "mssql":
            if "SQL SERVER 2014" in _vstr:
                return 12
            elif "SQL SERVER 2012" in _vstr:
                return 11
            elif "SQL SERVER 2008R2" in _vstr:
                return 10.5
            elif "SQL SERVER 2008" in _vstr:
                return 10
            elif "SQL SERVER 2005" in _vstr:
                return 9
        return None

    def _parseKwargs(self, **kwargs):
        if len(kwargs) <= 0:
            return ""

        sql = []
        for key in kwargs.keys():
            sql.append("%s=:%s" % (key, key))
        sql = " AND ".join(sql)
        return "(" + sql + ")"

    def _parseArgs(self, where, *args):
        if not where:
            return "", {}

        if len(args) <= 0:
            return where or "", {}

        paramstyle_count = where.count('?')
        assert paramstyle_count == len(args)

        where_list = where.split('?')
        where_len = len(where_list)
        where_result = []
        for i, w in enumerate(where_list):
            where_result.append(w)
            if where_len > (i + 1):
                where_result.append(":%s%d" % (self.params_mark, i))
        where = "".join(where_result)

        params = {}
        for i, argv in enumerate(args):
            _key = "%s%d" % (self.params_mark, i)
            params.update({_key: argv})

        return where, params

    def _parseFields(self, fields, temp=None):
        def not_empty(s):
            return str(s) and str(s).strip()

        if isinstance(fields, str):
            fields = fields.split(",")
        if not isinstance(fields, list) and not isinstance(fields, tuple):
            raise KeyError("fields must be string or list/tuple for string")

        fields = list(set(fields))
        fields = list(filter(not_empty, fields))
        if temp:
            fields = ["{temp}.{value}".format(temp=temp, field=field) for field in fields]
        return ",".join(fields)

    def MySqlDialect(self, table, fields, page, pagesize, where, order, primarykey, *args, **kwargs):
        offset = (page - 1) * pagesize
        if offset < 0:
            offset = 0

        sql = ["SELECT {fields} FROM {table}".format(fields=self._parseFields(fields), table=table)]

        where_result = []
        _where1 = self._parseKwargs(**kwargs)
        _where2, _params = self._parseArgs(where, *args)
        kwargs.update(_params)

        if _where1:
            where_result.append(_where1)
        if _where2:
            where_result.append(_where2)
        if len(where_result) > 0:
            where = " AND ".join(where_result)
            sql.append("WHERE {where}".format(where=where))

        if order:
            sql.append("ORDER BY {order}".format(order=order))

        sql.append("LIMIT {offset},{pagesize}".format(offset=offset, pagesize=pagesize))
        return " ".join(sql), kwargs

    def Mssql2012Dialect(self, table, fields, page, pagesize, where, order, primarykey, *args, **kwargs):
        offset = (page - 1) * pagesize
        if offset < 0:
            offset = 0

        sql = ["SELECT {fields} FROM {table}".format(fields=self._parseFields(fields), table=table)]

        where_result = []
        _where1 = self._parseKwargs(**kwargs)
        _where2, _params = self._parseArgs(where, *args)
        kwargs.update(_params)

        if _where1:
            where_result.append(_where1)
        if _where2:
            where_result.append(_where2)
        if len(where_result) > 0:
            where = " AND ".join(where_result)
            sql.append("WHERE {where}".format(where=where))

        if order:
            sql.append("ORDER BY {order}".format(order=order))
        else:
            sql.append("ORDER BY {primarykey}".format(primarykey=primarykey))

        sql.append("OFFSET {offset} ROWS FETCH NEXT {pagesize} ROWS ONLY".format(offset=offset, pagesize=pagesize))
        return " ".join(sql), kwargs

    def MssqlDialect(self, table, fields, page, pagesize, where, order, primarykey, *args, **kwargs):
        offset = (page - 1) * pagesize
        if offset < 0:
            offset = 0

        fields = self._parseFields(fields)
        sql = ["SELECT TOP {pagesize} {fields} FROM {table}".format(pagesize=pagesize, fields=fields, table=table)]
        tsql = ["SELECT TOP {offset} {prikey} FROM {table}".format(offset=offset, prikey=primarykey, table=table)]

        where_result = []
        _where1 = self._parseKwargs(**kwargs)
        _where2, _params = self._parseArgs(where, *args)
        kwargs.update(_params)

        if _where1:
            where_result.append(_where1)
        if _where2:
            where_result.append(_where2)
        if len(where_result) > 0:
            where = " AND ".join(where_result)
            sql.append("WHERE")
            sql.append(where)
            tsql.append("WHERE")
            tsql.append(where)

        kwargs.update(_params)

        if order:
            order = "ORDER BY {order}".format(order=order)
        else:
            order = "ORDER BY {primarykey}".format(primarykey=primarykey)
        tsql.append(order)

        if offset > 0:
            if "WHERE" in sql:
                sql.append("AND")
            else:
                sql.append("WHERE")
            sql.append("{primarykey} NOT IN ({tsql})".format(primarykey=primarykey, tsql=" ".join(tsql)))

        sql.append(order)
        return " ".join(sql), kwargs

    def OracleDialect(self, table, fields, page, pagesize, where, order, primarykey, *args, **kwargs):
        raise TypeError("Not Support {dialect} in this version.".format(dialect=self.dialect))

    def SqliteDialect(self, table, fields, page, pagesize, where, order, primarykey, *args, **kwargs):
        raise TypeError("Not Support {dialect} in this version.".format(dialect=self.dialect))

    def PostgreSqlDialect(self, table, fields, page, pagesize, where, order, primarykey, *args, **kwargs):
        raise TypeError("Not Support {dialect} in this version.".format(dialect=self.dialect))

    def AnsiSqlDialect(self, table, fields, page, pagesize, where, order, primarykey, *args, **kwargs):
        raise TypeError("Not Support {dialect} in this version.".format(dialect=self.dialect))

    def forPaginate(self, table, fields, page, pagesize, where, order, primarykey, *args, **kwargs):
        if self.dialect.lower() == "mssql":
            version = self._getversion()
            if version and version >= 11:
                return self.Mssql2012Dialect(table, fields, page, pagesize, where, order, primarykey, *args, **kwargs)
            return self.MssqlDialect(table, fields, page, pagesize, where, order, primarykey, *args, **kwargs)
        elif self.dialect.lower() == "mysql":
            return self.MySqlDialect(table, fields, page, pagesize, where, order, primarykey, *args, **kwargs)
        elif self.dialect.lower() == "oracle":
            return self.OracleDialect(table, fields, page, pagesize, where, order, primarykey, *args, **kwargs)
        elif self.dialect.lower() == "sqlite":
            return self.SqliteDialect(table, fields, page, pagesize, where, order, primarykey, *args, **kwargs)
        elif self.dialect.lower() == "postgresql":
            return self.PostgreSqlDialect(table, fields, page, pagesize, where, order, primarykey, *args, **kwargs)
        else:
            return self.AnsiSqlDialect(table, fields, page, pagesize, where, order, primarykey, *args, **kwargs)


class database(_DBS):
    params_mark = "_LeafPy_argv_"

    def _converModify(self, sql, *args, **kwargs):
        paramstyle_count = sql.count('?')
        assert len(args) == paramstyle_count

        q_list = sql.split('?')
        q_len = len(q_list)
        q_result = []
        for i, q in enumerate(q_list):
            q_result.append(q)
            if q_len > (i + 1):
                q_result.append(":%s%d" % (self.params_mark, i))

        params = {}
        for i, argv in enumerate(args):
            _key = "%s%d" % (self.params_mark, i)
            params.update({_key: argv})
        kwargs.update(params)

        return "".join(q_result), kwargs

    def selectpage(self, table, fields, page, pagesize, **kwargs):
        where = kwargs.pop("where", None)
        args = kwargs.pop("args", ())
        order = kwargs.pop("order", None)
        primarykey = kwargs.pop("primarykey", "id")
        _fetchall = True if self._engine.name.lower() == "mssql" else False
        fetchall = kwargs.pop("fetchall", _fetchall)

        _test = kwargs.pop("_test", False)
        dbDialect = DbDialect(self._engine.name, self.get_version())
        query, params = dbDialect.forPaginate(table, fields, page, pagesize, where, order, primarykey, *args, **kwargs)
        if _test:
            return query, params

        return True, self.query(query, fetchall=fetchall, **params)

    def modify(self, sql, *args, **kwargs):
        _test = kwargs.pop("_test", False)
        query, params = self._converModify(sql, *args, **kwargs)
        if _test:
            return query, params

        return True, self.query(query, **params)


class SQLConn(object):
    def __init__(self, *args, **configs):
        _baseconn = None
        if len(args) > 0:
            assert isinstance(args[0], string_types)
            _baseconn = args[0].strip()
        _baseconn = _baseconn or configs.pop("_baseconn", "default")

        self._baseconn = _baseconn
        self._dbc = configs.copy()
        self._dbs = {}

    def __len__(self):
        return len(self._dbs)

    def __repr__(self):
        return "SQLConn {}".format(self._dbs)

    def __getattr__(self, name):
        db = None
        if name.lower() not in dir(database):
            db = self._gen_conn(name)
            return db

        if not db:
            db = self._gen_conn(self._baseconn)
            if hasattr(db, name):
                return getattr(db, name)

        raise KeyError("not find database: %s in DB Config" % name)

    def _gen_conn(self, name):
        if (not self._dbc) or conf.settings.DEBUG:
            self._dbc = conf.settings.DATABASE.copy()

        if conf.settings.DEBUG:  # close all cache db connection in debug model every time
            self.close()

        if name in self._dbs:
            return self._dbs.get(name)
        else:
            _dbc = self._dbc.get(name)
            _lpt = _dbc.pop("printing", False)
            printing = any([_lpt, _dbc.get("PRINTING"), conf.settings.DEBUG_SQL])
            _dbc.update(dict(PRINTING=printing))
            if _dbc:
                _db = database(**_dbc)
                self._dbs[name] = _db
                return _db
        return None

    def close(self):
        for v in self._dbs.values():
            v.close()
        self._dbs.clear()


BaseSQLClass = SQLConn

sql = SQLConn()
