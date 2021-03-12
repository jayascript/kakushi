#!/bin/sh

bg_color=#716799
text_color=#C2FFDF
htext_color=#F1568E
bg_transparent=#95800080
bg_no_color=#00716799

NUM_SCREENS=$(xrandr -q | grep " connected" | wc -l)
if [ NUM_SCREENS=="2" ]; then
    monitor="DP-1"
else
    monitor="eDP-1"
fi

#    xrandr --output eDP-1 --primary --mode 1920x1080 --pos 1360x0 --rotate normal --output DP-1 --mode 1360x768 --pos 0x0 --rotate normal --output DP-2 --off --output HDMI-1 --off
#fi
rofi -show run -lines 3 -eh 2 -width 100 -padding 500 -monitor "$monitor" -bw 0 -color-window "$bg_color, $bg_color, $bg_color" -color-normal "$bg_no_color, $text_color, $bg_no_color, $bg_no_color, $htext_color" -font "Monofur 18"
