#!/bin/bash

scrot /tmp/screen.png
convert /tmp/screen.png -scale 10% -scale 1000% /tmp/screen.png
i3lock -t -f -i /tmp/screen.png -n
rm /tmp/screen.png
