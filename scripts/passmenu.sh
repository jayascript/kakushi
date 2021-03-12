#!/usr/bin/env bash

bg_color=#ffffff
text_color=#F1568E

first_alternating_row_color=#f8f8f2
second_alternating_row_color=#ffffff

active_text_color=#42395d
active_bg_color=#ffb8d1

shopt -s nullglob globstar

typeit=0
if [[ $1 == "--type" ]]; then
	typeit=1
	shift
fi

prefix=${PASSWORD_STORE_DIR-~/.password-store}
password_files=( "$prefix"/**/*.gpg )
password_files=( "${password_files[@]#"$prefix"/}" )
password_files=( "${password_files[@]%.gpg}" )

password=$(printf '%s\n' "${password_files[@]}" | rofi -color-window "$bg_color, $bg_color, $bg_color" -color-normal "$first_alternating_row_color, $text_color, $second_alternating_row_color, $active_bg_color, $active_text_color" -font "Monofur 18" -dmenu -p "Password")

[[ -n $password ]] || exit

if [[ $typeit -eq 0 ]]; then
	pass show -c "$password" 2>/dev/null
else
	pass show "$password" | { IFS= read -r pass; printf %s "$pass"; } |
		xdotool type --clearmodifiers --file -
fi
