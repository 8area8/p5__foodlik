#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""Title screen."""

from datetime import datetime

from termcolor import colored

from core.front.classes.globals import BaseSection


TITLE = """
    oooooooooooo                           .o8  oooo   o8o  oooo   COPYRIGHT
    '888'     '8                          "888  '888   '"'  `888
     888          .ooooo.   .ooooo.   .oooo888   888  oooo   888  oooo
     888oooo8    d88' '88b d88' '88b d88' '888   888  `888   888 .8P'
     888    "    888   888 888   888 888   888   888   888   888888.
     888         888   888 888   888 888   888   888   888   888 `88b.
    o888o        'Y8bod8P' 'Y8bod8P' `Y8bod88P" o888o o888o o888o o888o"""


class TitleScreen(BaseSection):
    """This class show the title screen of the application."""

    def __init__(self):
        """Initialization."""
        super().__init__()

        self.c_select = "[choisir produit]: aller aux catégories.\n"
        self.c_see_substitus = ("[voir substituts]: voir "
                                "les substituts sauvegardés.\n")

        url = 'https://github.com/8area8/P4_OpenFoodFact_interface'
        version = "version 1.0"

        self.header = (f"Foodlik {version} | "
                       f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}."
                       f"\nDocumentation disponible: {colored(url, 'cyan')}."
                       + "\n" * 2 + colored(TITLE, "green") + "\n" * 3 +
                       colored("Bienvenu dans Foodlik !", "yellow") +
                       "\n" + colored("-" * 20, "yellow"))  # YOLO.

        self.content = (f"Faites un choix." + "\n" * 2)

    @property
    def footer(self):
        """Return the footer informations.

        Call 'Super().footer' to get the error messages.
        """
        text = (self.comm + self.c_quit + self.c_select +
                self.c_see_substitus + '\n')
        text += super().footer
        return text

    @property
    def actions(self):
        """Return the possible actions.

        Call 'super().actions' to get the basic actions.
        """
        return ["choisir produit", "voir substituts"] + super().actions

    def apply(self, action):
        """Apply an action."""
        if action == "choisir produit":
            self.change_to = "Categories"
        if action == "voir substituts":
            self.change_to = "Substitutes"
