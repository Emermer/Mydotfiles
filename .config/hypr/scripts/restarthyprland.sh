#!/bin/bash
killall hypridle; hypridle &
killall waybar; sleep 0.2; waybar &
pypr reload || pypr &