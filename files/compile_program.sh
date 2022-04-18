#!/bin/bash
##
## EPITECH PROJECT, 2021
## git_branch (Workspace)
## File description:
## compile_program.sh
##

SCRIPT_FOLD="src"
FOLD="_git_branch_"
BIN_NAME="git_branch"
PROG_FILES="main.py $SCRIPT_FOLD/colors.py $SCRIPT_FOLD/constants.py"
echo -e "\e[1;32mCompiling the program...\n$PROG_FILES\e[0m"
echo -e "\e[1;32mCleaning destination folder\e[0m"
rm install_prog/linux/*
cd $FOLD
echo -e "\e[1;32mCompiling the program\e[1;36m"
pyinstaller $PROG_FILES --onefile -n $BIN_NAME
cd ..
echo -e "\e[1;32mCopying the compiled program\e[0m"
mv $FOLD/dist/$BIN_NAME install_prog/linux
echo -e "\e[1;32mCleaning the crumbs\e[0m"
rm -rf $FOLD/build
rm -rf $FOLD/dist
rm -rf $FOLD/__pycache__
rm $FOLD/*.spec
echo -e "\e[1;32mFinished!\e[0m"
