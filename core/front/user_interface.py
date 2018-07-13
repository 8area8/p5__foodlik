#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""User Interface."""

import os


def init():
    """Initialize the interface."""
    running = True
    page = Interface()
    while running:
        action = input("type an action:")

        if action in page.actions:
            page.apply(action)
        elif action == "quit()":
            print("good bye!")
            running = False
        else:
            page.action_error(action)


class Interface():
    """This class is the UI of the application."""

    def __init__(self):
        """Initialization."""
        self.section = TitleScreen()

    @property
    def actions(self):
        """Show the possibles actions."""
        return self.section.actions
    
    def display(self):
        """Display the current section."""
        clear()
        print(self.section)

    def apply(self, action):
        """Apply an action."""
        self.section.apply(action)

    def action_error(self, action):
        """Return an error message."""
        self.section.action_error(action)


def clear():
    """Clear the console."""
    os.system('cls' if os.name == 'nt' else 'clear')
