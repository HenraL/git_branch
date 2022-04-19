#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## my_scripts - colors (main menu)
## File description:
## jitter jitter
##

# __Version__ = 5.0
# Fix the pb with the text intentionally shifting color during the print

import os
from time import sleep
from random import randint

class Color:
    """ The class in charge of displaying color """
    def __init__(self, My_Globals) -> None:
        """ passing the globals the class needs """
        self.version = 5.0
        self.Current_OS = My_Globals.Current_OS
        self.Color_Pallet = My_Globals.Color_Pallet
        self.Windows_Color_Command = My_Globals.Windows_Color_Command
        self.non_windows_colour_command = My_Globals.Non_Windows_Color_Command
        self.colorise_output = My_Globals.Colorise_Output
        self.opts_color_pallet = My_Globals.Options_For_Color_Pallet
        self.opts_for_testing_color_pallet = My_Globals.Options_for_testing_Color_Pallet
        self.non_windows_colours = My_Globals.Non_Windows_Colors
        self.default_background = My_Globals.default_background
        self.default_foreground = My_Globals.default_foreground
        self.current_foreground = self.default_foreground
        self.current_background = self.default_background

    def initialise_pallet_if_not(self):
        """ If the pallet is not initialised, initialise it"""
        if (len(self.Color_Pallet) == 0):
            self.init_pallet()

    def output_for_windows_system(self, Input_Color) -> None:
        """ If the system is windows, setting the color for it """
        if (self.Current_OS == "Windows"):
            os.system(f"{self.Windows_Color_Command}{self.Color_Pallet[Input_Color]}")

    def output_for_non_Windows_system(self, Input_Color) -> None:
        """ If the system is not windows, setting the color for it """
        if (self.Current_OS != "Windows"):
            os.system(f"{self.non_windows_colour_command}\"{self.Color_Pallet[Input_Color]}\"")

    def Check_if_Digit_Is_In_List(self, Input_Didgit:str) -> bool:
        if (Input_Didgit in self.opts_color_pallet) == True:
            return True
        return False

    def Color_Input_Error_Handling(self, Input_Color:str) -> str:
        """ Deal with potential errors that might occur during color input """
        if (len(Input_Color) == 1):
            if (self.Check_if_Digit_Is_In_List(Input_Color[0]) == False):
                Input_Color = f'{self.default_background}{self.default_foreground}'
            else:
                temp = Input_Color[0]
                Input_Color=f"{temp}{self.default_foreground}"
        elif (len(Input_Color) > 2):
            if (self.Check_if_Digit_Is_In_List(Input_Color[0]) == False):
                Input_Color[0] = self.default_background
            if (self.Check_if_Digit_Is_In_List(Input_Color[1]) == False):
                Input_Color[1] = self.default_foreground
            Input_Color=f"{Input_Color[0]}{Input_Color[1]}"

        elif (len(Input_Color) < 1):
            Input_Color = f'{self.default_background}{self.default_foreground}'
        else:
            return Input_Color
        return Input_Color

    def Display(self, Input_Color) -> None:
        """ If setting the color is true, changing the color for the required system """
        if (self.colorise_output == True):
            self.initialise_pallet_if_not()
            Input_Color = self.Color_Input_Error_Handling(Input_Color)
            self.output_for_non_Windows_system(Input_Color)
            self.output_for_windows_system(Input_Color)

    def init_for_non_windows(self) -> None:
        """ If the system is not windows, initialising pallet for it """
        if (self.Current_OS != "Windows") :
            g=0
            for i in self.opts_color_pallet:
                h=0
                for b in self.opts_color_pallet:
                    self.Color_Pallet[f"{i}{b}"]=f"\\e[{int(self.non_windows_colours[g])+10}m\\e[{int(self.non_windows_colours[h])}m"
                    h+=1
                g+=1

    def init_for_windows(self) -> None:
        """ If the system is windows, initialising the pallet for it """
        if (self.Current_OS == "Windows"):
            for i in self.opts_color_pallet:
                for b in self.opts_color_pallet:
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
        self.init_for_non_windows()
        self.init_for_windows()

    def test_colors(self, delay=0.05) -> None:
        """ This is a small function to test the output of the colors (avoid using if epileptic) """
        if (delay == 0):
            delay = 0.05
        for i in self.opts_for_testing_color_pallet:
            for b in self.opts_for_testing_color_pallet:
                self.Display(f'{i}{b}')
                print(f"The color is: {i}{b}")
                sleep(delay)

    def random_color(self) -> None:
        """ Change the color to a random choice (r) excluded """
        color2_found = False
        len_color = len(self.opts_for_testing_color_pallet)-2
        color1 = randint(0, len_color)
        while color2_found == False:
            color2 = randint(0, len_color)
            if color1 != color2:
                color2_found = True
        self.Display(f'{self.opts_for_testing_color_pallet[color1]}{self.opts_for_testing_color_pallet[color2]}')

    def random_foreground_color(self, background_color:str='0') -> None:
        """ Change the foreground color to a random choice (r) included """
        len_color = len(self.opts_for_testing_color_pallet)-1
        colours_identical = True
        color1 = randint(0, len_color)
        while colours_identical == True:
            color1 = randint(0, len_color)
            if color1 != background_color:
                colours_identical = False
        self.Display(f'{background_color}{self.opts_for_testing_color_pallet[color1]}')

    def intellicut(self, string:str, symb:str='%', skip_length:int=2) -> list[str,str]:
        """ Cut a string following certain rules """
        if (symb not in string):
            return string
        final_list = list()
        temp_string = str()
        skip = 0
        has_been_skipping = False
        for i in range(len(string)):
            if (skip > 0):
                skip -= 1
                temp_string+=string[i]
                # print(f"143 | in if    , temp_string = {temp_string}, skip = {skip}")
            elif skip == 0 and has_been_skipping == True:
                has_been_skipping = False
                final_list.append(temp_string)
                temp_string = str()
                temp_string+=string[i]
                # print(f"149 | in elif 1 , temp_string = {temp_string}, skip = {skip}")
            elif (string[i] == symb and string[i+1] == symb):
                temp_string+=string[i]
                skip=1
                # print(f"153 | in elif 2, temp_string = {temp_string}, skip = {skip}")
            elif (string[i] == symb and skip == 0):
                skip=skip_length
                has_been_skipping = True
                final_list.append(temp_string)
                # print(f"158 | in elif 3, temp_string = {temp_string}, skip = {skip}")
                temp_string = str()
                # print(f"153 | in elif 3, temp_string = {temp_string}, skip = {skip}")
            else:
                temp_string+=string[i]
                # print(f"163 | in else  , temp_string = {temp_string}, skip = {skip}")
        final_list.append(temp_string)
        return final_list

    def print_color(self, formated_string:str, symb:str='%') -> None:
        """ Change the color of the string based on key points"""
        processed_string = self.intellicut(formated_string, symb, 2)
        # print(f"processed_string = {processed_string}")
        self.initialise_pallet_if_not()
        for i in range(len(processed_string)):
            # print(f"processed_string[{i}] = {processed_string[i]}")
            if (processed_string[i] in self.Color_Pallet):
                # print("in if")
                self.Display(processed_string[i])
            else:
                # print("in else")
                print(processed_string[i], end='')
