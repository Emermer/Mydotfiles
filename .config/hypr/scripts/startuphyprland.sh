#!/bin/bash
xrandr --output HDMI-A-1 --primary &
swaybg -m fill -i $HOME/Pictures/Background/cleanmountainbackground.jpg &
gsettings set org.gnome.desktop.interface cursor-theme simple-and-soft-cursor &
hyprctl setcursor simple-and-soft-cursor 24 &
hyprlock &
waybar &
dunst &
/usr/bin/lxpolkit &
/usr/bin/pypr &
hypridle &
nm-applet --indicator &
/usr/lib/kdeconnectd &
gammastep -c $HOME/.config/gammastep/gammastep.conf &
openrgb -c 0000FF -m static &
~/.config/nextcloud/start.sh &