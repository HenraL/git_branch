#!/bin/bash

BIN_NAME=prog
pyinstaller main.py colors.py constants.py --onefile -n $BIN_NAME
rm compiled/*
mv dist/$BIN_NAME compiled
rm -rf build
rm -rf dist
rm *.spec
rm -rf __pycache__
