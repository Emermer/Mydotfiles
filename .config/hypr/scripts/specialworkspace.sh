#!/bin/bash
if pgrep -x "bitwarden" > /dev/null
then
    hyprctl dispatch togglespecialworkspace
else
    bitwarden-desktop &
    hyprctl dispatch togglespecialworkspace
fi
