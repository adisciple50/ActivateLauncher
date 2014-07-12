#!/bin/sh

# source here: http://heritagerobotics.wordpress.com/2012/11/20/compiling-pygame-for-python-3-2-in-xubuntu/
# and tweaked by me (Jason Crockett).
# tested on xubuntu 14.04 and works.

sudo apt-get install gksu # expected behavior should ask the user to do what is needed

cd ~
sudo apt-get install -y mercurial
hg clone https://bitbucket.org/pygame/pygame
cd pygame

sudo apt-get install python3-dev python3-numpy libsdl-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libportmidi-dev libavformat-dev libswscale-dev libjpeg-dev libfreetype6-dev
python3 setup.py build
gksu python3 setup.py install

echo "this is my favourate ide"

firefox -open-tab "http://www.jetbrains.com/pycharm/download/"