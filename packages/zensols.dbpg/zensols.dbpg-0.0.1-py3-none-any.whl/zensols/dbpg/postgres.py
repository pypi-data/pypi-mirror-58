"""Postgres implementation of the ``ConnectionManager``.

"""
__author__ = 'Paul Landes'

import logging
from pathlib import Path
import psycopg2
from psycopg2.extras import RealDictCursor
from zensols.db import (
    connection,
    DbPersister,
    ConnectionManager,
    ConnectionManagerConfigurer,
    DbPersisterFactory,
)

logger = logging.getLogger(__name__)


class PostgresConnectionManager(ConnectionManager):
    """An Postgres connection factory.

    """
    EXISTS_SQL = 'select count(*) from information_schema.tables where table_schema = \'public\''
    DROP_SQL = 'drop owned by {user}'

    def __init__(self, db_name: str, host: str, port: str,
                 user: str, password: str,
                 persister: DbPersister, create_db: bool = True,
                 capture_lastrowid: bool = False, fast_insert: bool = False):
        """Initialize.

        :param persister: the persister that will use this connection factory
                          (needed to get the initialization DDL SQL)

        """
        super(PostgresConnectionManager, self).__init__()
        self.db_name = db_name
        self.port = port
        self.host = host
        self.user = user
        self.password = password
        self.persister = persister
        self.create_db = create_db
        self.capture_lastrowid = capture_lastrowid
        self.fast_insert = fast_insert

    def _init_db(self, conn, cur):
        logger.info(f'initializing database...')
        for sql in self.persister.parser.get_init_db_sqls():
            logger.debug(f'invoking sql: {sql}')
            cur.execute(sql)
            conn.commit()

    def create(self):
        logger.debug(f'creating connection to {self.host}:{self.port} with '+
                     f'{self.user} on database: {self.db_name}')
        conn = psycopg2.connect(
            host=self.host, database=self.db_name, port=self.port,
            user=self.user, password=self.password)
        try:
            cur = conn.cursor()
            cur.execute(self.EXISTS_SQL, ())
            if cur.fetchone()[0] == 0:
                self._init_db(conn, cur)
        finally:
            cur.close()
        return conn

    def drop(self):
        conn = self.create()
        cur = conn.cursor()
        try:
            cur.execute(self.DROP_SQL.format(**self.__dict__))
            conn.commit()
        finally:
            cur.close()
            conn.close()

    def execute(self, conn, sql, params, row_factory, map_fn):
        """See ``DbPersister.execute``.

        """
        def other_rf_fn(row):
            return row_factory(*row)

        create_fn = None
        if row_factory == 'dict':
            cur = conn.cursor(cursor_factory=RealDictCursor)
        elif row_factory == 'tuple':
            cur = conn.cursor()
        else:
            create_fn = other_rf_fn
            cur = conn.cursor()
        try:
            cur.execute(sql, params)
            res = cur.fetchall()
            if create_fn is not None:
                res = map(create_fn, res)
            if map_fn is not None:
                res = map(map_fn, res)
            return tuple(res)
        finally:
            cur.close()

    def execute_no_read(self, conn, sql, params=()) -> int:
        cur = conn.cursor()
        logger.debug(f'execute no read: {sql}')
        try:
            cur.execute(sql, params)
            conn.commit()
            if self.capture_lastrowid:
                return cur.fetchone()[0]
        finally:
            cur.close()

    def _insert_row(self, conn, cur, sql, row):
        cur.execute(sql, row)
        conn.commit()
        if self.capture_lastrowid:
            return cur.fetchall()[0][0]

    def _insert_rows_slow(self, conn, sql, rows: list, errors: str,
                          set_id_fn, map_fn) -> int:
        rowid = None
        cur = conn.cursor()
        try:
            for row in rows:
                if map_fn is not None:
                    org_row = row
                    row = map_fn(row)
                if errors == 'raise':
                    rowid = self._insert_row(conn, cur, sql, row)
                elif errors == 'ignore':
                    try:
                        rowid = self._insert_row(conn, cur, sql, row)
                    except Exception as e:
                        logger.error(f'could not insert row ({len(row)})', e)
                else:
                    raise ValueError(f'unknown errors value: {errors}')
                if set_id_fn is not None:
                    set_id_fn(org_row, cur.lastrowid)
        finally:
            cur.close()
        logger.debug(f'inserted with rowid: {rowid}')
        return rowid

    def _insert_rows_fast(self, conn, sql, rows: list, map_fn) -> int:
        cur = conn.cursor()
        logger.debug('inserting rows fast')
        try:
            if map_fn is not None:
                rows = map(map_fn, rows)
            cur.executemany(sql, rows)
            conn.commit()
        finally:
            cur.close()

    def insert_rows(self, conn, sql, rows: list, errors: str,
                    set_id_fn, map_fn) -> int:
        if self.fast_insert:
            return self._insert_rows_fast(conn, sql, rows, map_fn)
        else:
            return self._insert_rows_slow(conn, sql, rows, errors, set_id_fn, map_fn)


class SqliteConnectionManagerConfigurer(ConnectionManagerConfigurer):
    def configure(self, params):
        params['sql_file'] = Path(params['sql_file'])
        kwargs = {}
        pnmes = 'host port db_name user password create_db ' + \
            'capture_lastrowid fast_insert'
        for n in pnmes.split():
            if n in params:
                kwargs[n] = params[n]
                del params[n]
        logger.debug(f'config using arguments: {kwargs}')
        kwargs['persister'] = None
        params['conn_manager'] = PostgresConnectionManager(**kwargs)


DbPersisterFactory.register_connection_manager_configurer(
    SqliteConnectionManagerConfigurer, 'postgres')
