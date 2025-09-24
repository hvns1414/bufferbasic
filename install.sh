#!/bin/bash
echo "Updating pip..."
python3 -m pip install --upgrade pip

echo "Installing colorama..."
pip3 install colorama

echo "Installing optparse..."
pip3 install optparse

echo "Installing socket..."
pip3 install socket

echo
echo "Installation complete."
