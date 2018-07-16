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
        self.nutriscore_msg = ""

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

    def load_substituts(self, score, title):
        """Load the substituts of a product."""
        first_res = self._load_first_substituts(score, title)
        second_res = self.load_second_substituts(title, score)
        return (first_res, second_res)

    def _load_first_substituts(self, score, title):
        """Find two better product in the same category."""
        database.execute("SELECT DISTINCT prod.title, prod.description, "
                         "prod.stores, cat_prod.category_title, "
                         "prod.site_url, prod.score FROM PRODUCT as prod "
                         "INNER JOIN CATEGORY_PER_PRODUCT AS cat_prod "
                         "ON prod.title=cat_prod.product_title "
                         f"WHERE category_title='{self.chosen_category}' "
                         f"AND prod.score < {score} "
                         "ORDER BY prod.score ASC LIMIT 1")
        result = database.get_row(True)
        if result:
            return result

        database.execute("SELECT DISTINCT prod.title, prod.description, "
                         "prod.stores, cat_prod.category_title, "
                         "prod.site_url, prod.score FROM PRODUCT as prod "
                         "INNER JOIN CATEGORY_PER_PRODUCT AS cat_prod "
                         "ON prod.title=cat_prod.product_title "
                         f"WHERE category_title='{self.chosen_category}' "
                         f"AND prod.score >= {score} AND "
                         f"prod.title <> '{title}' "
                         "ORDER BY prod.score ASC LIMIT 1")
        return database.get_row(True)

    def load_second_substituts(self, title, score):
        """Find 2 better product in the smallest product category."""
        database.execute("SELECT cat.title, cat.product_number "
                         "FROM CATEGORY as cat "
                         "INNER JOIN CATEGORY_PER_PRODUCT AS cat_prod "
                         "ON cat.title=cat_prod.category_title "
                         "INNER JOIN PRODUCT AS prod "
                         "ON prod.title=cat_prod.product_title "
                         f"WHERE prod.title='{title}' "
                         "ORDER BY cat.product_number ASC LIMIT 5")
        result = database.get_row(True)
        if result[0][0] == self.chosen_category:
            return "sorry, we didn't find a better category."
        ncategory = result[0][0]
        database.execute("SELECT DISTINCT prod.title, prod.description, "
                         "prod.stores, cat_prod.category_title, "
                         "prod.site_url, prod.score FROM PRODUCT as prod "
                         "INNER JOIN CATEGORY_PER_PRODUCT AS cat_prod "
                         "ON prod.title=cat_prod.product_title "
                         f"WHERE category_title='{ncategory}' "
                         f"AND prod.score < {score} "
                         "ORDER BY prod.score ASC LIMIT 1")
        return database.get_row(True)

    def close(self):
        """Close the connection."""
        database.close()


datas_wrapper = _DataWrapper()
