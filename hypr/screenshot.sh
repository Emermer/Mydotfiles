#!/bin/bash
slurp | grim -g - $HOME/Pictures/screenshots/$(date +'screenshot_%F-%T.png') &&
wait &&
notify-send "Screenshot has been saved to $HOME/Pictures/screenshots"
