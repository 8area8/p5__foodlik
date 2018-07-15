#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""Category section."""

import textwrap

from termcolor import colored

from core.front.classes.globals import BaseSection
from core.back.database.data_wrapper import datas_wrapper as datas


class Category(BaseSection):
    """The Category class."""

    def __init__(self):
        """Initialization."""
        super().__init__()

        self.name = datas.chosen_category.upper()

        self.page = 0
        self.max_pages = datas.get_len_products() // 15
        self.current_products = []

        # FOOTER COMMANDS
        self.c_next = "[n] or [next]: go to the next page.\n"
        self.c_bef = "[b] or [before]: go to the previous page.\n"
        self.c_page = "[number] keyword: go to the corresponding page.\n"
        self.c_ctg = "[categorie_name] keyword: go to the categorie page.\n"

    @property
    def header(self):
        """Return the header informations."""
        title = f"   {self.name} (PAGE: {self.page + 1}/{self.max_pages + 1})"
        return colored(title, "yellow") + "\n" + "   " + "-" * 23

    @property
    def content(self):
        """Return the content."""
        self.current_products = datas.load_products(self.page)
        text = ""
        for product in self.current_products:
            product = textwrap.wrap(str(product), 45)
            product = "\n     ".join(product)
            text += ("   * " + colored(product, "yellow") + " \n")
        return text

    @property
    def footer(self):
        """Return the footer informations.

        Call 'super().footer' to get the error messages.
        """
        return (self.comm + self.c_return_ctgs + self.c_next + self.c_bef +
                self.c_page + self.c_ctg + self.c_quit + "\n") + super().footer

    @property
    def actions(self):
        """Return the possible actions.

        Call 'super().actions' to get the basic actions.
        """
        return (self.a_nextbef + self.a_return_ctgs +
                [str(num) for num in range(1, self.max_pages + 2)] +
                self.current_products +
                [prod.lower() for prod in self.current_products] +
                super().actions)

    def apply(self, action):
        """Apply an action."""
        if action == "return cat":
            self.change_to = "Categories"
        if action == "next" or action == "n":
            self.page += 1
            self.page = 0 if self.page > self.max_pages else self.page
        if action == "before" or action == "b":
            self.page -= 1
            self.page = self.max_pages if self.page < 0 else self.page
        if action.isdigit() and (0 < int(action) <= self.max_pages + 1):
            self.page = int(action) - 1
        if action.lower() in [prod.lower() for prod in self.current_products]:
            datas.chosen_product = ([prod for prod in self.current_products
                                    if prod.lower() == action.lower()][0])
            self.change_to = "Product"
