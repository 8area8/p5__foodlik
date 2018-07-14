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

    @property
    def header(self):
        """Return the header informations."""
        return f"   CATEGORIES (PAGE: {self.page})"

    @property
    def content(self):
        """Return the content."""
        return ""

    @property
    def footer(self):
        """Return the footer informations.

        Call 'super().footer' to get the error messages.
        """
        return "text"

    @property
    def actions(self):
        """Return the possible actions.

        Call 'super().actions' to get the basic actions.
        """
        return "ENTER keyword, " + super().actions

    def apply(self, action):
        """Apply an action."""
        if action == "":
            self.change_to = "Categories"
