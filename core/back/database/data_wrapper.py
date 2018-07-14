#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""Display the datas of 'foodlik'."""

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

import core.passwords as db_connect


class DataWrapper():
    """Communicate and display the 'foodlik' datas."""

    def __init__(self):
        """Initialization."""
        user = db_connect.DB_USER
        pwd = db_connect.DB_PASSWORD
        self.connection = psycopg2.connect(dbname="foodlik", user=user,
                                           host="localhost", password=pwd)
        self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        self.cursor = self.connection.cursor()

        self.cursor.execute("SELECT COUNT(title) FROM CATEGORY;")
        self.len_ctg = self.cursor.fetchone()[0]
        ctg_book = self.len_ctg // 15
        self.ctg_book = ctg_book + 1 if self.len_ctg % 15 else ctg_book

    def max_products_index(self, categorie):
        """Return the max product index in the current categorie."""
        pass

    def load_categories(self, page):
        """Load the categories."""
        page = page if 0 < page < self.ctg_book else 1

        self.cursor.execute("SELECT * FROM CATEGORY "
                            f"LIMIT 15 OFFSET {page * 15}")
        return [wrd[0] for wrd in self.cursor.fetchall()]

    def load_product_number(self, category):
        """Return the number of product in the given category."""
        self.cursor.execute("SELECT COUNT(*) FROM CATEGORY_PER_PRODUCT "
                            f"WHERE category_title = '{category}'")
        return str([dig[0] for dig in self.cursor.fetchall()][0])

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
