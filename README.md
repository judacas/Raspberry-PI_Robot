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
$ python programName.py

# Operating System Version
The program and installation instructions have been tested on "Raspbian GNU/Linux 10 (buster)"  
Check the Operating System version  
$ cat /etc/os-release  


# How it was going to work
so if you look at the stl models you can see that I had two ultrasonic sensors on each side perpendicular from each other.
The reason for that is because I not only wanted to follow the wall but to know the actual distance to the wall no matter the orientation of the robot
The end goal was to be able to actually map the edges of a room, hence why we need to not only follow the edge but know the exact ditance
if you were to only use one then if the robot wasn't perpendicular to the wall it wouldn't give you the closest distance to the well
yes I know I could've just used a gyroscope with one ultrasonic and done some simpler trig but I'm stubborn and wanted to restrrict myself to no gyroscopes.
I never got to finish this project either because classes started up but now I have to do a follower robot for one of my classes here at USF so I'm thinking
about just continuing this project and submitting that.
