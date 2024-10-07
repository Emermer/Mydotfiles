#!/bin/bash
xrandr --output HDMI-A-1 --primary &
swaybg -m fill -i $HOME/Pictures/Background/cleanmountainbackground.jpg &
gtklock -M HDMI-A-1 &
waybar &
dunst &
/usr/bin/lxpolkit &
thunar --daemon &
nm-applet --indicator &
/usr/lib/kdeconnectd &
gammastep -c $HOME/.config/gammastep/gammastep.conf &
openrgb -c 0000FF &
swayidle -w \
    timeout 480 'hyprctl dispatch dpms off' \
    resume '{
    hyprctl dispatch dpms on;
    gtklock -M HDMI-A-1;
    sleep 5;
    xrandr --output HDMI-A-1 --primary;
}'
