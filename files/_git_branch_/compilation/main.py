#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## my_scripts - main.py
## File description:
## jitter jitter
##

import constants as my_const
import colors as co

def main(self) -> None:
    """ The default function to test code """
    print("Hello World!")
    print(f"System = {self.Current_OS}")
    if (self.argc == 2):
        co.Color.init_pallet(self)
        if "test" in self.argv:
            co.Color.test_colors(self)
        else:
            co.Color.Display(self, self.argv[1])
    else:
        print(f"Usage: {self.filename} <color>")


CI = co.Color(my_const)
main(CI)
