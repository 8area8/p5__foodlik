#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""Global functions for cross SGBDR compatibility."""

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

import mysql
import mysql.connector

import core.passwords as psw


class Database():
    """Wrapper for the database modules.

    NOTE: do not use this class.
    Use the Singleton 'database_wrapper' variable below.
    """

    def __init__(self):
        """Initialization."""
        self.name = ""
        self._connection = None
        self._cursor = None

    def connect(self, dbname="foodlik"):
        """Connect to the database."""
        self.name = psw.DB_CHOICE
        user = psw.DB_USER
        pwd = psw.DB_PASSWORD

        if self.name == "psql":
            dbname = "postgres" if dbname == "root" else dbname
            self._connection = psycopg2.connect(dbname=dbname,
                                                user=user,
                                                host="localhost",
                                                password=pwd)
            self._connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        elif self.name == "msql":
            dbname = "" if dbname == "root" else dbname
            self._connection = mysql.connector.connect(host='localhost',
                                                       database=dbname,
                                                       user=user,
                                                       password=pwd)
            self._connection.autocommit = True
        else:
            raise ValueError(f"Wrong database name: {self.name}")

        self._cursor = self._connection.cursor()

    def execute(self, query, multi=False):
        """Execute a query."""
        if multi and self.name == "msql":
            for _ in self._cursor.execute(query, multi=True):
                pass  # dirty !
        else:
            self._cursor.execute(query)

    def get_row(self, all_rows=False):
        """Return the result of a query."""
        if all_rows:
            return self._cursor.fetchall()
        return self._cursor.fetchone()

    def close(self):
        """Close the connection."""
        self._cursor.close()
        self._connection.close()


database_wrapper = Database()
