#!/bin/bash
picom -b &
warpd &
nm-applet &
feh --randomize --bg-fill ~/Pictures/wallpapers/pc/current/*
setxkbmap -model pc105 -layout us
# xrandr --output DisplayPort-2 --mode 1920x1080 --rate 144
