#!/bin/bash
if pgrep wlogout >/dev/null
then
    killall wlogout && wlogout
else
    wlogout
fi &
