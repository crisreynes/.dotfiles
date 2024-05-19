#!/bin/bash
warpd &
nm-applet &
feh --randomize --bg-fill ~/Pictures/wallpapers/pc/current/*
setxkbmap -model pc105 -layout us
# xrandr --rate 144
picom -b &
