#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""Display the datas of 'foodlik'."""

from core.back.database.databases_wrapper import database_wrapper as database
from core.back.database.create_database import write_error

SUBSTITUTE1 = """
SELECT DISTINCT prod.title, prod.description, prod.stores,
 cat_prod.category_title, prod.site_url, prod.score
 FROM PRODUCT as prod
 INNER JOIN CATEGORY_PER_PRODUCT AS cat_prod
 ON prod.title=cat_prod.product_title
 WHERE category_title='*category*'
 AND prod.score < *score*
 ORDER BY prod.score ASC LIMIT 1"""

SUBSTITUTE2 = """
SELECT DISTINCT prod.title, prod.description, prod.stores,
 cat_prod.category_title, prod.site_url, prod.score
 FROM PRODUCT as prod
 INNER JOIN CATEGORY_PER_PRODUCT AS cat_prod
 ON prod.title=cat_prod.product_title
 WHERE category_title='*category*'
 AND prod.score >= *score* AND prod.title <> '*title*'
 ORDER BY prod.score ASC LIMIT 1"""

SUBSTITUTE3 = """
SELECT cat.title, cat.product_number
 FROM CATEGORY as cat
 INNER JOIN CATEGORY_PER_PRODUCT AS cat_prod
 ON cat.title=cat_prod.category_title
 INNER JOIN PRODUCT AS prod
 ON prod.title=cat_prod.product_title
 WHERE prod.title='*title*'
 ORDER BY cat.product_number ASC LIMIT 5"""

SUBSTITUTE4 = """
SELECT DISTINCT prod.title, prod.description, prod.stores,
 cat_prod.category_title, prod.site_url, prod.score
 FROM PRODUCT as prod
 INNER JOIN CATEGORY_PER_PRODUCT AS cat_prod
 ON prod.title=cat_prod.product_title
 WHERE category_title='*ncategory*' AND prod.score < *score*
 ORDER BY prod.score ASC LIMIT 1"""


class _DataWrapper():
    """Communicate and display the 'foodlik' datas.

    NOTE: do not use this class.
    Use the Singleton 'data_wrapper' variable below.
    """

    def __init__(self):
        """Initialization."""
        self.len_categories = None
        self.len_substitutes = None

        self.chosen_category = ""
        self.chosen_product = ""
        self.nutriscore_msg = ""

    def connect(self, db_name="foodlik"):
        """Connect to the database."""
        database.connect(db_name)

        database.execute("SELECT COUNT(title) FROM CATEGORY;")
        self.len_categories = database.get_row()[0]

        database.execute("SELECT COUNT(*) FROM SUBSTITUTE")
        self.len_substitutes = database.get_row()[0]

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

    def load_product_substitutes(self, score, title):
        """Load the substitutes of a product."""
        first_res = self._load_first_substitute(score, title)
        second_res = self.load_second_substitute(title, score)
        return (first_res, second_res)

    def _load_first_substitute(self, score, title):
        """Find a better product in the same category."""
        query = SUBSTITUTE1.replace("*category*", self.chosen_category)
        query = query.replace("*score*", str(score))
        database.execute(query)
        result = database.get_row(True)
        if result:
            return result

        query = SUBSTITUTE2.replace("*category*", self.chosen_category)
        query = query.replace("*score*", str(score))
        query = query.replace("*title*", title)
        database.execute(query)
        return database.get_row(True)

    def load_second_substitute(self, title, score):
        """Find a better product in the smallest product category."""
        query = SUBSTITUTE3.replace("*title*", title)
        database.execute(query)
        result = database.get_row(True)
        if result[0][0] == self.chosen_category:
            return "sorry, we didn't find a better category."

        query = SUBSTITUTE4.replace("*ncategory*", result[0][0])
        query = query.replace("*score*", str(score))
        database.execute(query)
        return database.get_row(True)

    def save_substitute(self, substitute):
        """Save the substitute title in the database."""
        try:
            database.execute("INSERT INTO substitute (product_title) "
                             f"VALUES ('{substitute[0]}')")
        except Exception as error:
            write_error(error)  # to be sure it's the good error.
            pass  # substitute already in the databse.

        try:
            database.execute("INSERT INTO product_per_substitute "
                             "(substitute_title, product_title) VALUES "
                             f"('{substitute[0]}', '{self.chosen_product}')")
        except Exception as error:
            write_error(error)
            return "The substitute is already saved for this product."
        else:
            return "Substitute saved."

    def load_substitutes_page(self, page):
        """Load the substitutes."""
        database.execute("SELECT * FROM substitute "
                         f"LIMIT 15 OFFSET {page * 15}")
        return [wrd[0] for wrd in database.get_row(True)]

    def load_substitute_page(self):
        """Load the substitute page."""
        database.execute("SELECT prd.title, prd.description, prd.stores, "
                         "prd.site_url, prd.score FROM product AS prd "
                         f"WHERE prd.title = '{self.chosen_product}'")
        substitut = database.get_row()
        database.execute("SELECT product_title FROM product_per_substitute "
                         f"WHERE substitute_title = '{self.chosen_product}'")
        products = database.get_row(True)
        return substitut, products

    def close(self):
        """Close the connection."""
        database.close()


datas_wrapper = _DataWrapper()
