#!/bin/bash
WS_NAME="$1"
APP="${2:-$1}"

if pgrep -x "$WS_NAME" > /dev/null
then
    hyprctl dispatch togglespecialworkspace name:$WS_NAME
else
    $APP &
    hyprctl dispatch togglespecialworkspace name:$WS_NAME
fi
