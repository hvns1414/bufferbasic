@echo off
echo Installing required packages individually...
python -m pip install --upgrade pip

echo Installing colorama...
pip install colorama

echo Installing optparse...
pip install optparse

echo Installing socket...
pip install socket

echo.
echo Installation complete.
pause
