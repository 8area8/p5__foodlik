#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""Display the datas of 'foodlik'."""

import getpass

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class DataWrapper():
    """Communicate and display the 'foodlik' datas."""

    def __init__(self):
        """Initialization."""
        user = input("PostgreSQL user:")
        pwd = getpass.getpass("PostgreSQL password:")
        self.connection = psycopg2.connect(dbname="foodlik", user=user,
                                           host="localhost", password=pwd)
        self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        self.cursor = self.connection.cursor()

        self.len_ctg = self.cursor.execute(f"SELECT COUNT(title) "
                                           "FROM CATEGORY;").fetchone()
        self.ctg_book = self.len_ctg // 15 + self.len_ctg % 15

    def max_products_index(self, categorie):
        """Return the max product index in the current categorie."""
        pass

    def load_categories(self, page):
        """Load the categories."""
        req = self.cursor.execute("SELECT * FROM CATEGORY "
                                  f"LIMIT 15 OFFSET {page * 15}")
        return req.fetchone()

    def load_products(self, categorie_name):
        """Load the porducts of a categorie."""
        pass

    def load_product(self, product_name):
        """Load a product."""
        pass

    def close(self):
        """Close the connection."""
        self.cursor.close()
        self.connection.close()


datas_wrapper = DataWrapper()
