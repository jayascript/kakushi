#!/bin/sh

bg_color=#716799
text_color=#C2FFDF
htext_color=#F1568E
bg_transparent=#95800080
bg_no_color=#00716799

rofi -show run -lines 3 -eh 2 -width 100 -padding 500 -monitor "eDP-1" -bw 0 -color-window "$bg_color, $bg_color, $bg_color" -color-normal "$bg_no_color, $text_color, $bg_no_color, $bg_no_color, $htext_color" -font "Raleway 18"
