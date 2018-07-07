#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""Title screen."""

import sys
from datetime import datetime

from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected

url = 'https://github.com/8area8/P4_OpenFoodFact_interface'
version = "version 0.2"

print(f"Foodlik {version}", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print(f"Documentation available at {url}")
print('\n' * 3)
cprint(figlet_format('Foodlik', font='roman'), 'yellow', attrs=['bold'])
print('\n' * 3)
cprint("Welcome to Foodlik !", "yellow", attrs=['bold'])
print("-" * 20)
print("blablalba")
