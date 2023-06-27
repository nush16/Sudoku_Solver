#!/bin/bash

# Install Pygame if not already installed
if ! command -v pygame &> /dev/null
then
    echo "Pygame not found. Installing..."
    # Use the package manager of your choice to install Pygame
    # For example, on Ubuntu-based systems: sudo apt-get install python-pygame
fi

# Run the Sudoku solver
python -c 'import pygame; exec(open("app.py").read())'