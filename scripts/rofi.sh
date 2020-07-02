#!/bin/sh

# purple #800080
# blue-grey #2f343f
bg_color=#2f343f
text_color=#e5e5e5
htext_color=#ff69b4
bg_transparent=#95800080
bg_no_color=#00800080

rofi -show run -lines 3 -eh 2 -width 100 -padding 800 -monitor "eDP-1" -bw 0 -color-window "$bg_transparent, $bg_transparent, $bg_transparent" -color-normal "$bg_no_color, $text_color, $bg_no_color, $bg_no_color, $htext_color" -font "Raleway 18"
