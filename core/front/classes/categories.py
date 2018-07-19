#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""Categories section."""

from termcolor import colored

from core.front.classes.globals import BaseSection
from core.back.database.data_wrapper import datas_wrapper as datas


class Categories(BaseSection):
    """Categories class."""

    def __init__(self):
        """Initialization."""
        super().__init__()

        self.page = 0
        self.max_pages = datas.len_categories // 15
        self.current_categories = []

        # FOOTER COMMANDS
        self.c_next = "[s] or [suivant]: page suivante.\n"
        self.c_bef = "[a] or [avant]: page précédente.\n"
        self.c_page = "[nombre] mot-clé: va à la page correspondante.\n"
        self.c_ctg = "[nom de catégorie] mot-clé: va à la page de catégorie.\n"

    @property
    def header(self):
        """Return the header informations."""
        title = f"   CATEGORIES (PAGE: {self.page + 1}/{self.max_pages + 1})"
        return colored(title, "yellow") + "\n" + "   " + "-" * 23

    @property
    def content(self):
        """Return the content."""
        self.current_categories = datas.load_categories(self.page)
        text = ""
        for category in self.current_categories:
            text += ("   * " + colored(category[0], "yellow") + " " +
                     "[" + str(category[1]) + " produits]\n")
        return text

    @property
    def footer(self):
        """Return the footer informations.

        Call 'super().footer' to get the error messages.
        """
        return (self.comm + self.c_next + self.c_bef + self.c_page +
                self.c_ctg + self.c_quit + "\n") + super().footer

    @property
    def actions(self):
        """Return the possible actions.

        Call 'super().actions' to get the basic actions.
        """
        categories = [cat[0] for cat in self.current_categories]
        return (self.a_nextbef +
                [str(num) for num in range(1, self.max_pages + 2)] +
                categories +
                [cat.lower() for cat in categories] +
                super().actions)

    def apply(self, action):
        """Apply an action."""
        if action == "suivant" or action == "s":
            self.page += 1
            self.page = 0 if self.page > self.max_pages else self.page
        if action == "avant" or action == "a":
            self.page -= 1
            self.page = self.max_pages if self.page < 0 else self.page
        if action.isdigit() and (0 < int(action) <= self.max_pages + 1):
            self.page = int(action) - 1
        if action.capitalize() in [cat[0] for cat in self.current_categories]:
            datas.chosen_category = action.capitalize()
            self.change_to = "Category"
