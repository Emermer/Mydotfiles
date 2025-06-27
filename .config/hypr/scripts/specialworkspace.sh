#!/bin/bash
if pgrep -x "bitwarden" > /dev/null
then
    hyprctl dispatch togglespecialworkspace bitwarden
else
    bitwarden-desktop &
    hyprctl dispatch togglespecialworkspace bitwarden
fi
