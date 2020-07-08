# Raspberry PI Autonomous Vehicle

Initial list of requirements to run the Python program that controls the Raspberry PI

Make sure the operating system is updated 
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install build-essential

# Python (version and libraries)
Check Python version  
$ python -V
If Python 3.8.0 is not installed, then follow the instructions from https://installvirtual.com/how-to-install-python-3-8-on-raspberry-pi-raspbian/ 

Install RPi.GPIO. This package provides a class to control the GPIO on a Raspberry Pi.
$ pip install RPi.GPIO
$ sudo pip install setuptools --upgrade

# How to run the program
$ python RobotWithXbox.py 

# Operating System Version
The program and installation instructions have been tested on "Raspbian GNU/Linux 10 (buster)"
Check the Operating System version
$ cat /etc/os-release
