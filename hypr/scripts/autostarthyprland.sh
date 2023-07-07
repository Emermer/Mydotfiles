#!/bin/bash
gtklock &
waybar &
dunst &
/usr/bin/lxpolkit &
emacs --daemon &
nm-applet --indicator &
/usr/lib/kdeconnectd &
swaybg -m fill -i $HOME/Pictures/Background/cleanmountainbackground.jpg &
gammastep -c $HOME/.config/gammastep/gammastep.conf &
swayidle -w \
    timeout 300 'gtklock -s $HOME/.config/gtklock/style.css' \
    timeout 600 'systemctl suspend'
