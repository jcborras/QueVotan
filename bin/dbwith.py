#!/usr/bin/env python
# -*- coding: utf-8; mode: python; -*-

# http://effbot.org/zone/python-with-statement.htm

from csv import DictWriter, QUOTE_NONNUMERIC, register_dialect
from datetime import datetime
from re import sub

from psycopg2 import connect as psyconnect
from psycopg2 import ProgrammingError as psyProgrammingError


class DbConnection(object):
    def __init__(self, connect_function, params):
        self.connect = connect_function
        self.params = params

    def __enter__(self):
        self.dbcon = self.connect(**self.params)
        self.dbcon.autocommit = True
        self.cur = self.dbcon.cursor()
        return self

    def __exit__(self, type, value, traceback):
        self.cur.close()
        self.dbcon.close()

    def __call__(self, query):
        self.cur.execute(query)
        colnames, tuples = None, None
        if self.cur.description:
            colnames = [i[0] for i in self.cur.description]
            tuples = [i for i in self.cur]
        return tuples, colnames

    def nrows(self, tablename):
        qry = "SELECT COUNT(*) AS n FROM {t:s};".format(t=tablename)
        rows, cols = self.__call__(qry)
        return rows[0][0]

    def bulkload(self, tablename, filename):
        raise RuntimeError('Please implement bulkload() on all descendents')


class PostgreSQLconnection(DbConnection):
    def __init__(self, params):
        super().__init__(psyconnect, params)

    def __call__(self, query):
        try:
            return super().__call__(query)
        except psyProgrammingError as e:
            # print(dir(e.diag)) # TODO: nice object for detailed error report
            raise RuntimeError(e.pgerror)
        except BaseException as e:
            raise RuntimeError(e.args)

    def bulkload(self, tablename, filename):
        tplt = "COPY {t:s} FROM '{f:s}' DELIMITER ',' CSV;"
        qry = tplt.format(f=filename, t=tablename)
        self.__call__(qry)
