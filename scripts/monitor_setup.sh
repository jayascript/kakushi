#!/bin/sh

NUM_SCREENS=$(xrandr -q | grep " connected" | wc -l)
if [ NUM_SCREENS=="2" ]; then
    xrandr --output eDP-1 --primary --mode 1920x1080 --pos 1360x0 --rotate normal --output DP-1 --mode 1360x768 --pos 0x0 --rotate normal --output DP-2 --off --output HDMI-1 --off
fi
