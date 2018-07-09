#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""Display the datas of 'foodlik'."""


class DataWrapper():
    """Communicate and display the 'foodlik' datas."""

    def __init__(self):
        """Initialization."""
        self.len_categories_page = 0

    def max_products_index(self, categorie):
        """Return max product index in the current categorie."""
        pass

    def load_categories(self, page):
        """Load the categories."""
        pass

    def load_products(self, categorie_name):
        """Load the porducts of a categorie."""
        pass

    def load_product(self, product_name):
        """Load a product."""
        pass


datas_wrapper = DataWrapper()
