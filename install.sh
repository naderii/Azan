#!/bin/bash

# Update package list and install system dependencies
sudo apt-get update

# Install Python and pip if they are not already installed
sudo apt-get install -y python3 python3-pip

# Install dependencies listed in requirements.txt
pip3 install -r requirements.txt

# Install PyInstaller
pip3 install pyinstaller

# Create executable file from the Python script
pyinstaller --onefile main.py

echo "All dependencies have been installed and the executable has been created successfully."
echo "You can find the executable in the 'dist' directory."
