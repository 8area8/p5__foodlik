#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""Contain the section of saved substitutes."""

from termcolor import colored

from core.front.classes.globals import BaseSection
from core.back.database.data_wrapper import datas_wrapper as datas


class Substitutes(BaseSection):
    """This class show the title screen of the application."""

    def __init__(self):
        """Initialization."""
        super().__init__()

        self.page = 0
        self.max_pages = datas.len_substitutes // 15
        self.current_substitutes = []

        # FOOTER COMMANDS
        self.c_next = "[s] or [suivant]: page suivante.\n"
        self.c_bef = "[a] or [avant]: page précédente.\n"
        self.c_page = "[nombre] mot-clé: va à la page correspondante.\n"
        self.c_sbt = "[nom substitut] mot-clé: va à la page du substitut.\n"

    @property
    def header(self):
        """Return the header informations."""
        title = f"   SUBSTITUTS (PAGE: {self.page + 1}/{self.max_pages + 1})"
        return colored(title, "yellow") + "\n" + "   " + "-" * 23

    @property
    def content(self):
        """Return the content."""
        self.current_substitutes = datas.load_substitutes_page(self.page)
        text = ""
        for substitute in self.current_substitutes:
            text += ("   * " + colored(substitute, "yellow") + "\n")
        return text

    @property
    def footer(self):
        """Return the footer informations.

        Call 'super().footer' to get the error messages.
        """
        return (self.comm + self.c_next + self.c_bef + self.c_page +
                self.c_return_title +
                self.c_sbt + self.c_quit + "\n") + super().footer

    @property
    def actions(self):
        """Return the possible actions.

        Call 'super().actions' to get the basic actions.
        """
        return (self.a_nextbef +
                [str(num) for num in range(1, self.max_pages + 2)] +
                self.current_substitutes + self.a_return_title +
                [sbt.lower() for sbt in self.current_substitutes] +
                super().actions)

    def apply(self, action):
        """Apply an action."""
        if action == "suivantext" or action == "s":
            self.page += 1
            self.page = 0 if self.page > self.max_pages else self.page
        if action == "avant" or action == "a":
            self.page -= 1
            self.page = self.max_pages if self.page < 0 else self.page
        if action.isdigit() and (0 < int(action) <= self.max_pages + 1):
            self.page = int(action) - 1
        if action.lower() in [prd.lower() for prd in self.current_substitutes]:
            datas.chosen_product = ([prod for prod in self.current_substitutes
                                     if prod.lower() == action.lower()][0])
            self.change_to = "Substitute"
        if action == "retour titre":
            self.change_to = "TitleScreen"
