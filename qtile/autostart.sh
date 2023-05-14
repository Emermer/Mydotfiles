#!/bin/bash
xrandr --output DP-2 --mode 1680x1050 --pos 1920x30 --rotate normal --output HDMI-1 --primary --mode 1920x1080 --rate 144 --pos 0x0 --rotate normal &
feh --no-fehbg --bg-fill /home/emermer/Pictures/Background/cleanmountainbackground.jpg
xset r rate 250 25 &
picom &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
nm-applet &
dunst &
emacs --daemon &
xautolock -time 8 -locker "betterlockscreen -l blur" &
if pgrep redshift-gtk >/dev/null
then
    echo redshift already running
else
    redshift-gtk -c $HOME/.config/redshift/redshift.conf
fi &
