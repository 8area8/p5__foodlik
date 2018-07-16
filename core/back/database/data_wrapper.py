#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""Display the datas of 'foodlik'."""

from core.back.database.databases_wrapper import database_wrapper as database


class _DataWrapper():
    """Communicate and display the 'foodlik' datas.

    NOTE: do not use this class.
    Use the Singleton 'data_wrapper' variable below.
    """

    def __init__(self):
        """Initialization."""
        self.len_categories = None

        self.chosen_category = ""
        self.chosen_product = ""

    def connect(self, db_name="foodlik"):
        """Connect to the database."""
        database.connect(db_name)

        database.execute("SELECT COUNT(title) FROM CATEGORY;")
        self.len_categories = database.get_row()[0]

    def get_len_products(self):
        """Return the products len in the current category.

        Call this method when you initialize a new Category class.
        """
        database.execute("SELECT COUNT(*) "
                         "FROM CATEGORY_PER_PRODUCT "
                         f"WHERE category_title = '{self.chosen_category}'")
        return database.get_row()[0]

    def load_products(self, page):
        """Load the products of a category."""
        database.execute("SELECT product_title "
                         "FROM CATEGORY_PER_PRODUCT "
                         f"WHERE category_title = '{self.chosen_category}' "
                         f"LIMIT 15 OFFSET {page * 15}")
        return [prod[0] for prod in database.get_row(True)]

    def load_categories(self, page):
        """Load the categories."""
        database.execute("SELECT * FROM CATEGORY "
                         f"LIMIT 15 OFFSET {page * 15}")
        return [wrd[0:2] for wrd in database.get_row(True)]

    def load_product(self):
        """Load a product."""
        database.execute("SELECT * FROM PRODUCT "
                         f"WHERE title = '{self.chosen_product}'")
        return database.get_row()

    def load_substituts(self):
        """Load the substituts of a product."""
        pass

    def close(self):
        """Close the connection."""
        database.close()


datas_wrapper = _DataWrapper()
