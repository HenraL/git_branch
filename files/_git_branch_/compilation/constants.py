#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## hello_world
## File description:
## constants.py
##

__Author__ = "Henry Letellier"
__Program_Name__ = "Git Branch"

import platform
from sys import argv

current_os = platform.system()

argc = len(argv)
filename = argv[0]

# Color class related vars
Colorise_Output = True
# The final reference created depending on if you are unser windows or not
Color_Pallet = dict()
default_background = '0'
default_foreground = 'A'
Windows_Color_Command = "color "
Non_Windows_Color_Command = "echo -e "
# Windows Color pallet (+ r (equivalent to a 'color AA'))
Options_For_Color_Pallet = "042615378CAE9DBFr"
Options_for_testing_Color_Pallet = "0123456789ABCDEFr"
Non_Windows_Colors = []
# Create colour list
for i in range(30,38):
    Non_Windows_Colors.append(f"{i}")
for i in range(90, 98):
    Non_Windows_Colors.append(f"{i}")
Non_Windows_Colors.append("0")
