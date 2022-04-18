#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## hello_world
## File description:
## constants.py
##

__Author__ = "Henry Letellier"
__Program_Name__ = "Git Branch"

import os
import src.constants as co
import src.colors as CO

class Git_Branch:
    """ The main class of the program """
    def __init__(self, my_constants) -> None:#, color_class
        """ The local globals of the class """
        self.system = my_constants.current_system
        self.argv = my_constants.argv
        self.argc = my_constants.argc
        self.available_commands = my_constants.available_commands
        self.full_commands = my_constants.full_commands
        self.answer = ""
        self.keep_running = True
        self.ci = CO.Color(my_constants)

    def is_only_blanks(self, string:str) -> bool:
        """ Cheeck if the whole string contains blanks """
        for i in string:
            if i != '\t' or i != ' ':
                return False
        return True

    def display_available_commands(self) -> None:
        """ Display the available commands """
        print("Available commands:")
        prev = self.get_first_element_of_dict(self.full_commands)
        print("\t-\t", end="")
        for i in self.full_commands:
            if self.full_commands[prev] != self.full_commands[i]:
                print(f":\n\t\t\t {self.full_commands[prev]}\n\n\t-\t'{i}' ", end="")
            elif self.full_commands[i] == self.full_commands[prev]:
                print(f"'{i}' ", end="")
            else:
                print(f"'{i}' ", end="")
            prev = i
        print(f":\n\t\t\t {self.full_commands[prev]}")
        print("\n")

    def display_sub_prog_help(self, prog_command:str) -> None:
        """ Display the help of a sub program (a global file registered in the database) """
        self.ci.random_foreground_color(self.ci.default_background)
        print(f"{prog_command}:")
        os.system(f"{prog_command} -h")

    def display_help(self) -> None:
        """ Display help for the program"""
        self.ci.Display('0E')
        print("HELP:\nMain section:\n")
        self.ci.random_foreground_color(self.ci.default_background)
        self.display_available_commands()
        self.ci.random_foreground_color(self.ci.default_background)
        print("BUILTIN OPTIONS:\n\t-\t-nc\n\t\t\trun program with the default colour.", end="")
        self.ci.random_foreground_color(self.ci.default_background)
        command_list = self.get_available_commands(self.full_commands)
        usr_answer = self.get_bool(f"Do you wish to display the help sections of all the available commands ({len(command_list)})? (y/n) : ", "Please enter y for yes or n for no.\n")
        if usr_answer == True:
            for i in command_list:
                self.display_sub_prog_help(self.full_commands[i])

        self.ci.Display("0A")
        # self.ci.print_color("%0A(%0Bc%0C) %0DCreated by Henry Letellier\n",'%')
        print("(c) Created by Henry Letellier\n")

    def get_arguments(self) -> str:
        """ Get potential arguments that would follow the command name """
        print("Press enter to not enter any arguments.")
        answer = input("Please enter the arguments you wish to use when running the command:")
        return answer

    def get_bool(self, question:str, error:str="Please enter y for yes or n for no.\n") -> bool:
        """ Ask a question to the User """
        cont = True
        while cont == True:
            answer = input(question)
            if (len(answer) > 0 and self.is_only_blanks(answer) == False):
                if answer.lower() == 'y' or answer.lower() == 'yes':
                    return True
                elif answer.lower() == 'n' or answer.lower() == 'no':
                    return False
                else:
                    print(f"{error}\nYou have entered: {answer}")
            else:
                print(f"{error}\nYou have entered: {answer}")
        return False

    def get_first_element_of_dict(self, dict_name:dict) -> str:
        """ Get the first element of a dictionary """
        for i in dict_name:
            return i

    def get_available_commands(self, command_list:list) -> list:
        """ Get the available commands """
        final_list = list()
        prev = self.get_first_element_of_dict(command_list)
        final_list.append(command_list[prev])
        for i in command_list:
            if command_list[prev] != command_list[i]:
                final_list.append(command_list[i])
            prev = i
        return final_list

    def get_full_command(self, usr_input:str) -> None:
        """ Check if the command exists """
        if self.full_commands[usr_input.lower()] == 'help':
            self.display_help()
        elif self.full_commands[usr_input.lower()] == "quit":
            self.keep_running = False
        elif (usr_input in self.full_commands) == True:
            args = self.get_arguments()
            self.run_command(usr_input, args)
        else:
            print("Command not found")
            print("\n")

    def get_first_part_of_the_command(self, usr_input:str, args:str='') -> str:
        """ Check if the command exists """
        if self.full_commands[usr_input.lower()] == 'help':
            self.display_help()
        elif self.full_commands[usr_input.lower()] == "quit":
            self.keep_running = False
        elif (usr_input in self.full_commands) == True:
            self.run_command(usr_input, args)
        else:
            print("Command not found")
            print("\n")

    def get_input(self, question:str) -> str:
        """ Ask a question to the User """
        cont = True
        while cont == True:
            self.answer = input(question)
            if (len(self.answer) > 0 and self.is_only_blanks(self.answer) == False):
                cont = False
        return self.answer

    def run_command(self, usr_input, arguments):
        """ Run the corresponding command """
        os.system(f"{self.full_commands[usr_input.lower()]}{arguments}")

    def list_to_string(self, list_name:list) -> str:
        """ Convert a list to a string """
        string = ""
        for i in list_name:
            string += f"{i} "
        return string

    def needs_no_colour(self) -> bool:
        """ Check if the program must be run without colour """
        if "-nc" in self.argv or "--no-color" in self.argv or "--no-colour" in self.argv:
            self.ci.no_color = True

    def main(self) -> None:
        """ The main function of the program """
        self.needs_no_colour()
        self.ci.init_pallet()
        self.ci.Display('0A')
        if self.system == 'Windows':
            print("This program has not been created for windows systems.")
            print("Therefore, you might experience some difficulties while using it")
        if self.argc == 2:
            self.keep_running = False
            self.ci.Display("0E")
            self.get_full_command(self.argv[1])
        elif self.argv > 2:
            self.keep_running = False
            self.ci.Display("0B")
            self.get_first_part_of_the_command(self.argv[1], self.list_to_string(self.argv[2:self.argc-1]))
        else:
            while self.keep_running == True:
                self.ci.Display('0A')
                print("Enter h for help")
                self.get_input("Enter your command:")
                self.get_full_command(self.answer)
        self.ci.random_foreground_color(self.ci.default_background)
        print("(c) Created by Henry Letellier")
        self.ci.Display('rr')


GI = Git_Branch(co)
GI.main()
