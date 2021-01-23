#!/bin/bash

PERCENT=$(acpi | head -1 | grep -oh [0-9]*% | sed 's/%//')
PLUGGEDIN=$(acpi -a | grep -oh "[a-z]*-" | sed 's/-//')

if [ ${PLUGGEDIN} == 'off' ]; then
    if [ ${PERCENT} -le 15 ]; then
        XDG_RUNTIME_DIR=/run/user/$(id -u) paplay /home/jayascript/Media/Sounds/Store_Door_Chime-Mike_Koenig-570742973.wav &&
        XDG_RUNTIME_DIR=/run/user/$(id -u) notify-send 'WARNING: BATTERY LOW. CONNECT THE CHARGER.' -u critical
    else
        if [ ${PERCENT} -le 5 ]; then
            XDG_RUNTIME_DIR=/run/user/$(id -u) paplay /home/jayascript/Media/Sounds/Store_Door_Chime-Mike_Koenig-570742973.wav &&
            XDG_RUNTIME_DIR=/run/user/$(id -u) notify-send 'WARNING: BATTERY CRITICAL. HIBERNATING.' -u critical
        fi
    fi
fi
