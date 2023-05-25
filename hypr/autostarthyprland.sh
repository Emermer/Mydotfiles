#!/bin/bash
gtklock &
waybar &
dunst &
#/usr/bin/polkit-dumb-agent &
/usr/bin/lxpolkit &
emacs --daemon &
swaybg -m fill -i $HOME/Pictures/Background/cleanmountainbackground.jpg &
gammastep -c $HOME/.config/gammastep/gammastep.conf &
swayidle -w timeout 480 'gtklock'
