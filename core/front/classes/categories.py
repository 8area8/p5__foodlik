#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""Categorie section."""

from termcolor import colored

from core.front.classes.globals import BaseSection
from core.back.database.data_wrapper import datas_wrapper as datas


class Categories(BaseSection):
    """Categories class."""

    def __init__(self):
        """Initialization."""
        super().__init__()

        self.page = 1
        self.max_pages = datas.ctg_book
        self.current_category = []

        # ACTION COMMANDS
        self.ac_nextbef = "'next', 'n', 'before', 'b'"
        self.ac_page = "page_number keyword"
        self.ac_ctg = ""
        self.ac_ctg_lower = ""

        # FOOTER COMMANDS
        self.c_next = "[n] or [next]: go to the next page.\n"
        self.c_bef = "[b] or [before]: go to the previous page.\n"
        self.c_page = "[number] keyword: go to the corresponding page.\n"
        self.c_ctg = "[categorie_name] keyword: go to the categorie page.\n"

    @property
    def header(self):
        """Return the header informations."""
        title = f"   CATEGORIES (PAGE: {self.page}/{self.max_pages})"
        return colored(title, "yellow") + "\n" + "   " + "-" * 23

    @property
    def content(self):
        """Return the content."""
        self.current_category = datas.load_categories(self.page)
        text = ""
        for category in self.current_category:
            products_nb = datas.load_product_number(category)
            text += ("   * " + colored(category, "yellow") + " " +
                     "[" + products_nb + " products]" "\n")
        return text

    @property
    def footer(self):
        """Return the footer informations.

        Call 'super().footer' to get the error messages.
        """
        return (self.comm + self.c_next + self.c_bef + self.c_page +
                self.c_ctg + self.c_quit + "\n")

    @property
    def actions(self):
        """Return the possible actions.

        Call 'super().actions' to get the basic actions.
        """
        self.ac_ctg = ", ".join(self.current_category)
        self.ac_ctg_lower = self.ac_ctg.lower()
        i_page = ", ".join(str(num) for num in range(1, self.max_pages + 1))

        return (f"{self.ac_nextbef}, {self.ac_page}, "
                f"{self.ac_ctg}, {self.ac_ctg_lower}, " +
                i_page + ", " +
                super().actions)

    def apply(self, action):
        """Apply an action."""
        if action == "next" or action == "n":
            self.page += 1
            self.page = 1 if self.page > self.max_pages else self.page
        if action == "before" or action == "b":
            self.page -= 1
            self.page = self.max_pages if self.page < 1 else self.page
        if action.isdigit() and (0 < int(action) <= self.max_pages):
            self.page = int(action)
        if action.capitalize() in self.current_category:
            self.change_to = "Category"
