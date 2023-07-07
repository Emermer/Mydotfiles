#!/bin/bash
if pgrep wlogout >/dev/null
then
    killall wlogout
else
    wlogout --protocol layer-shell -b 5 -T 400 -B 400
fi &
