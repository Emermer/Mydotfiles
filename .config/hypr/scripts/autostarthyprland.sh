#!/bin/bash
xrandr --output HDMI-A-1 --primary &
swaybg -m fill -i $HOME/Pictures/Background/cleanmountainbackground.jpg &
gsettings set org.gnome.desktop.interface cursor-theme simple-and-soft-cursor
hyprctl setcursor simple-and-soft-cursor 24
gtklock -M HDMI-A-1 &
waybar &
dunst &
/usr/bin/lxpolkit &
nm-applet --indicator &
/usr/lib/kdeconnectd &
gammastep -c $HOME/.config/gammastep/gammastep.conf &
openrgb -c 0000FF &
thunar &
sleep 0.5
killall thunar
thunar --daemon &
~/.config/nextcloud/start.sh &
swayidle -w \
    timeout 480 'true' \
    lock 'hyprctl dispatch dpms off' \
    resume '{
    hyprctl dispatch dpms on;
    gtklock -M HDMI-A-1;
    sleep 5;
    xrandr --output HDMI-A-1 --primary;
}'
