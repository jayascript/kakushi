#!/bin/sh
# Taken from: https://github.com/jlevers/dotfiles/blob/master/induvidual_scrot.sh

xdpyinfo -ext XINERAMA | sed '/^  head #/!d;s///' |
while IFS=' :x@,' read i w h x y; do
    import -window root -crop ${w}x$h+$x+$y $HOME/tmp/head_$i.png
done
