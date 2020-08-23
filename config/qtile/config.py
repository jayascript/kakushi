##########################################################
#     ,-----.  ,---------. .-./`)   .---.       .-''-.   #
#   .'  .-,  '.\          \\ .-.')  | ,_|     .'_ _   \  #
#  / ,-.|  \ _ \`--.  ,---'/ `-' \,-./  )    / ( ` )   ' #
# ;  \  '_ /  | :  |   \    `-'`"`\  '_ '`) . (_ o _)  | #
# |  _`,/ \ _/  |  :_ _:    .---.  > (_)  ) |  (_,_)___| #
# : (  '\_/ \   ;  (_I_)    |   | (  .  .-' '  \   .---. #
#  \ `"/  \  )  \ (_(=)_)   |   |  `-'`-'|___\  `-'    / #
#   '. \_/``"/)  ) (_I_)    |   |   |        \\       /  #
#     '-----' `-'  '---'    '---'   `--------` `'-..-'   #
#                                                        #
##########################################################

# A customized config.py file for Qtile (https://www.qtile.org)
# Modified by jayascript (https://jayascript.xyz)

# The following comments are the copyright and licensing information from the
# default config:

# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from screeninfo import get_monitors

# Set global vars
mod = "mod4"
term = guess_terminal()
home = os.path.expanduser('~')

fairyfloss = [
    ["#42395D", "#42395D"], # 0
    ["#A8757B", "#A8757B"], # 1
    ["#FF857F", "#FF857F"], # 2
    ["#E6C000", "#E6C000"], # 3
    ["#AE81FF", "#AE81FF"], # 4
    ["#716799", "#716799"], # 5
    ["#C2FFDF", "#C2FFDF"], # 6
    ["#F8F8F2", "#F8F8F2"], # 7
    ["#75507B", "#75507B"], # 8
    ["#FFB8D1", "#FFB8D1"], # 9
    ["#F1568E", "#F1568E"], # 10
    ["#D5A425", "#D5A425"], # 11
    ["#C5A3FF", "#C5A3FF"], # 12
    ["#8077A8", "#8077A8"], # 13
    ["#C2FFFF", "#C2FFFF"], # 14
    ["#F8F8F0", "#F8F8F0"], # 15
]

# Run scripts on login
lazy.spawn(home + "/.scripts/rate.sh")

# Map keybindings
keys = [
    # Logout and restart
    Key(
        [mod, "control"], "r",
        lazy.restart(),
        desc="Refresh Qtile"
    ),
    Key(
        [mod, "shift"], "q",
        lazy.shutdown(),
        desc="Log out of session"
    ),
    Key(
        ["shift", "mod1"], "q",
        lazy.shutdown(),
        desc="From tych0: logout keybinding in case mod4 gets hosed"
    ),

    # Spawn and kill
    Key(
        [mod], "Return",
        lazy.spawn(term),
        desc="Launch terminal"
    ),
    Key(
        [mod], "d",
        lazy.spawn(home + "/.scripts/rofi.sh"),
        desc="Run a program using rofi"
    ),
    Key(
        [mod, "shift"], "x",
        lazy.spawn(home + "/.scripts/lock.sh"),
        desc="Lock the screen"
    ),
    Key(
        [mod], "q",
        lazy.window.kill(),
        desc="Kill focused window"
    ),

    # Change layout
    Key(
        [mod], "Tab",
        lazy.next_layout(),
        desc="Toggle layouts"
    ),
    Key(
        [mod, "shift"], "space",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc="Switch which side main pane occupies monadtall"
    ),

    # Focus monitors
    Key(
        [mod], "p",
        lazy.to_screen(0),
        desc="Switch focus to output primary (monitor 1)"
    ),
    Key(
        [mod], "s",
        lazy.to_screen(1),
        desc="Switch focus to output secondary (monitor 2)"
    ),

    # Focus windows
    Key(
        [mod], "k",
        lazy.layout.down(),
        desc="Move focus down in current stack pane"
    ),
    Key(
        [mod], "j",
        lazy.layout.up(),
        desc="Move focus up in current stack pane"
    ),
    Key(
        [mod], "space",
        lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"
    ),

    # Move windows
    Key(
        [mod, "shift"], "k",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down(), # treetab
        desc="""Move window down in current stack;
                move window down a section in treetab"""
    ),
    Key(
        [mod, "shift"], "j",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up(), # treetab
        desc="""Move window up in current stack;
                move window up a section in treetab"""
    ),

    # Resize windows
    Key(
        [mod], "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen"
    ),
    Key(
        [mod], "l",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc="""Expand window (monadtall);
                increase number in master pane (tile)"""
    ),
    Key(
        [mod], "h",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc="""Shrink window (monadtall);
                decrease number in master pane (tile)"""
    ),
    Key(
        [mod], "m",
        lazy.layout.maximize()
    ),
    Key(
        [mod], "n",
        lazy.layout.normalize(),
        desc="Reset window size ratios"
    ),

    # Launch terminal apps (SUPER + ALT + KEY)
    Key(
        [mod, "mod1"], "b",
        lazy.spawn(term + " -e bpytop"),
        desc="Launch bpytop"
    ),
    Key(
        [mod, "mod1"], "c",
        lazy.spawn(term + " -e calcurse"),
        desc="Launch calcurse"
    ),
    Key(
        [mod, "mod1"], "l",
        lazy.spawn(term + " -e lynx"),
        desc="Launch lynx terminal browser"
    ),
    Key(
        [mod, "mod1"], "n",
        lazy.spawn(term + " -e newsboat"),
        desc="Launch newsboat"
    ),
    Key(
        [mod, "mod1"], "t",
        lazy.spawn("/opt/tor-browser_en-US/Browser/start-tor-browser"),
        desc="Launch Tor browser"
    ),
    Key(
        [mod, "mod1"], "v",
        lazy.spawn(term + " -e vifm"),
        desc="Launch Vi[m] File Manager"
    ),
]

# groups = [Group(i) for i in "asdfuiop"]
# New group definition from Derek Taylor (@DistroTube)
def name_groups():
    return [
        ("MAIN", {'layout': 'monadtall'}),
        ("SYS", {'layout': 'matrix'}),
        ("DEV", {'layout': 'monadtall'}),
        ("PROD", {'layout': 'monadtall'}),
        ("WWW", {'layout': 'monadtall'}),
        ("MAIL", {'layout': 'monadtall'}),
        ("DOC", {'layout': 'monadtall'}),
        ("ENT", {'layout': 'monadtall'}),
        ("CHAT", {'layout': 'monadtall'}),
    ]

def init_groups():
    return [Group(name, **kwargs) for name, kwargs in group_names]

if __name__ in ["config", "__main__"]:
    group_names = name_groups()
    groups = init_groups()

for i, (name, kwargs) in enumerate(group_names, 1):
    # Switch to another group
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
    # Send current window to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))

# Layout definition from Derek Taylor (@DistroTube)
layout_theme = {"border_width": 3,
                "margin": 10,
                "border_focus": "FFB8D1",
                "border_normal": "42395D"
                }

layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Tile(shift_windows=True, **layout_theme),
    #layout.Stack(num_stacks=2),
    layout.TreeTab(
         font = "Ubuntu",
         fontsize = 10,
         sections = ["FIRST", "SECOND"],
         section_fontsize = 11,
         bg_color = "141414",
         active_bg = "90C435",
         active_fg = "000000",
         inactive_bg = "384323",
         inactive_fg = "a0a0a0",
         padding_y = 5,
         section_top = 10,
         panel_width = 320
         ),
    #layout.Floating(**layout_theme)
]


widget_defaults = dict(
    font = 'raleway',
    fontsize = 15,
    foreground = fairyfloss[0],
    padding = 3,
)
extension_defaults = widget_defaults.copy()

def set_widgets():
    sep = widget.Sep(
        linewidth = 0,
        padding = 50,
    )
    widgets = [
        widget.CurrentLayoutIcon(
            foreground = fairyfloss[0],
        ),
        widget.CurrentLayout(
            fmt = "《{}》",
            foreground = fairyfloss[0],
        ),
        sep,
        widget.GroupBox(
            active = fairyfloss[6], # Active window font color
            highlight_method = "block",
            inactive = fairyfloss[1], # Inactive window font color
            other_current_screen_border = fairyfloss[0],
            other_screen_border = fairyfloss[0],
            this_current_screen_border = fairyfloss[4],
            this_screen_border = fairyfloss[5],
        ),
        sep,
        widget.Spacer(length=bar.STRETCH),
        widget.Clock(format='%Y-%m-%d %a %H:%M:%S'),
        widget.Systray(),
        widget.BatteryIcon(),
        widget.Battery(
            format = "{percent:2.0%}",
            low_percentage = 0.1,
            notify_below = 0.1,
        ),
        widget.QuickExit(
            countdown_start = 10,
            default_text = "[ Logout ]",
        ),
        widget.Wallpaper(
            directory = home + '/Pictures/Wallpapers/kawaii',
            random_selection = True,
            fmt = "",
        )
    ]
    return widgets

# Multiple monitors
num_screens = len(get_monitors())

if num_screens == 2:
    screens = [
        Screen(bottom=bar.Bar(set_widgets(), 30, background=fairyfloss[9])),
        Screen(bottom=bar.Bar(set_widgets(), 30, background=fairyfloss[9])),
    ]
else:
    screens = [
        Screen(bottom=bar.Bar(set_widgets(), 30, background=fairyfloss[9]))
    ]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
