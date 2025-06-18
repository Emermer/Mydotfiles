#!/bin/bash
IMG=~/Pictures/screenshots/$(date +'screenshot_%F-%T').png
if pgrep slurp >/dev/null
then
    killall slurp
else
    grim -g "$(slurp -d)" $IMG && wl-copy < $IMG && notify-send "Screenshot has been copied to clipboard and saved to ~/Pictures/screenshots!"
fi
