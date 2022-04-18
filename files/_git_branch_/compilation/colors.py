#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## my_scripts - colors (main menu)
## File description:
## jitter jitter
##

# __Version__ = 4.0

import os
from time import sleep
from random import randint

class Color:
    """ The class in charge of displaying color """
    def __init__(self, My_Globals) -> None:
        """ passing the globals the class needs """
        self.version = 4.0
        self.Current_OS = My_Globals.current_os
        self.Color_Pallet = My_Globals.Color_Pallet
        self.Windows_Color_Command = My_Globals.Windows_Color_Command
        self.Non_Windows_Color_Command = My_Globals.Non_Windows_Color_Command
        self.Colorise_Output = My_Globals.Colorise_Output
        self.Opts_Color_Pallet = My_Globals.Options_For_Color_Pallet
        self.Opts_for_testing_Color_Pallet = My_Globals.Options_for_testing_Color_Pallet
        self.Non_Windows_Colors = My_Globals.Non_Windows_Colors
        self.default_background = My_Globals.default_background
        self.default_foreground = My_Globals.default_foreground
        self.argc = My_Globals.argc
        self.argv = My_Globals.argv
        self.filename = My_Globals.filename

    def output_for_windows_system(self, Input_Color) -> None:
        """ If the system is windows, setting the color for it """
        if (self.Current_OS == "Windows"):
            os.system(f"{self.Windows_Color_Command}{self.Color_Pallet[Input_Color]}")

    def output_for_non_Windows_system(self, Input_Color) -> None:
        """ If the system is not windows, setting the color for it """
        if (self.Current_OS != "Windows"):
            os.system(f"{self.Non_Windows_Color_Command}\"{self.Color_Pallet[Input_Color]}\"")

    def Check_if_Digit_Is_In_List(self, Input_Didgit:str) -> bool:
        if (Input_Didgit in self.Opts_Color_Pallet) == True:
            return True
        return False

    def Color_Input_Error_Handling(self, Input_Color:str) -> str:
        """ Deal with potential errors that might occur during color input """
        if (len(Input_Color) == 1):
            if (Color.Check_if_Digit_Is_In_List(self, Input_Color[0]) == False):
                Input_Color = f'{self.default_background}{self.default_foreground}'
            else:
                temp = Input_Color[0]
                Input_Color=f"{temp}{self.default_foreground}"
        elif (len(Input_Color) > 2):
            if (Color.Check_if_Digit_Is_In_List(self, Input_Color[0]) == False):
                Input_Color[0] = self.default_background
            if (Color.Check_if_Digit_Is_In_List(self, Input_Color[1]) == False):
                Input_Color[1] = self.default_foreground
            Input_Color=f"{Input_Color[0]}{Input_Color[1]}"

        elif (len(Input_Color) < 1):
            Input_Color = f'{self.default_background}{self.default_foreground}'
        else:
            return Input_Color
        return Input_Color

    def Display(self, Input_Color) -> None:
        """ If setting the color is true, changing the color for the required system """
        if (self.Colorise_Output == True):
            Input_Color = Color.Color_Input_Error_Handling(self, Input_Color)
            Color.output_for_non_Windows_system(self, Input_Color)
            Color.output_for_windows_system(self, Input_Color)

    def init_for_non_windows(self) -> None:
        """ If the sytem is not windows, initialising pallet for it """
        if (self.Current_OS != "Windows") :
            g=0
            for i in self.Opts_Color_Pallet:
                h=0
                for b in self.Opts_Color_Pallet:
                    self.Color_Pallet[f"{i}{b}"]=f"\\e[{int(self.Non_Windows_Colors[g])+10}m\\e[{int(self.Non_Windows_Colors[h])}m"
                    h+=1
                g+=1

    def init_for_windows(self) -> None:
        """ If the system is windows, initialising the pallet for it """
        if (self.Current_OS == "Windows"):
            for i in self.Opts_Color_Pallet:
                for b in self.Opts_Color_Pallet:
                    if (i == 'r'):
                        if (b == 'r'):
                            self.Color_Pallet[f"{i}{b}"] = f"{self.Windows_Color_Command}0A"
                        else:
                            self.Color_Pallet[f"{i}{b}"] = f"{self.Windows_Color_Command}0{b}"
                    elif (b == 'r'):
                        self.Color_Pallet[f"{i}{b}"] = f"{self.Windows_Color_Command}{i}A"
                    else:
                        self.Color_Pallet[f"{i}{b}"] = f"{self.Windows_Color_Command}{i}{b}"

    def init_pallet(self) -> None:
        """ Initialising the color pallet for the program """
        Color.init_for_non_windows(self)
        Color.init_for_windows(self)

    def test_colors(self, delay=0.05) -> None:
        """ This is a small function to test the output of the colors (avoid using if epileptic) """
        if (delay == 0):
            delay = 0.05
        for i in self.Opts_for_testing_Color_Pallet:
            for b in self.Opts_for_testing_Color_Pallet:
                self.Display(f'{i}{b}')
                print(f"The color is: {i}{b}")
                sleep(delay)

    def random_color(self) -> None:
        """ Change the color to a random choice (r) excluded """
        color2_found = False
        len_color = len(self.Opts_for_testing_Color_Pallet)-1
        color1 = randint(0, len_color)
        while color2_found == False:
            color2 = randint(0, len_color)
            if color1 != color2:
                color2_found = True
        self.Display(f'{self.Opts_for_testing_Color_Pallet[color1]}{self.Opts_for_testing_Color_Pallet[color2]}')
