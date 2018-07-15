#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""Display the datas of 'foodlik'."""

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

import core.passwords as db_connect


class _DataWrapper():
    """Communicate and display the 'foodlik' datas.

    NOTE: don't use the class. Use the Singleton 'data_wrapper' variable below.
    """

    def __init__(self):
        """Initialization."""
        user = db_connect.DB_USER
        pwd = db_connect.DB_PASSWORD
        self.connection = psycopg2.connect(dbname="foodlik", user=user,
                                           host="localhost", password=pwd)
        self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        self.cursor = self.connection.cursor()

        self.cursor.execute("SELECT COUNT(title) FROM CATEGORY;")
        self.len_category = self.cursor.fetchone()[0]

        self.chosen_category = ""
        self.chosen_product = ""

    def len_products(self):
        """Return the products len in the current category."""
        pass

    def load_categories(self, page):
        """Load the categories."""
        self.cursor.execute("SELECT * FROM CATEGORY "
                            f"LIMIT 15 OFFSET {page * 15}")
        return [wrd[0:2] for wrd in self.cursor.fetchall()]

    def load_products(self):
        """Load the porducts of a categorie."""
        pass

    def load_product(self):
        """Load a product."""
        pass

    def close(self):
        """Close the connection."""
        self.cursor.close()
        self.connection.close()


datas_wrapper = _DataWrapper()
