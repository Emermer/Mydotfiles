#!/bin/bash
wlr-randr --output HDMI-A-1 --pos 0,0 --mode 1920x1080@143.981Hz --scale 1 --preferred --output DP-2 --pos 1920,30 --mode 1680x1050@59.883Hz --scale 1 &
nm-applet &
dunst &
emacs --daemon &
