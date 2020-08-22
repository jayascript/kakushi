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

mod = "mod4"
term = guess_terminal()
home = os.path.expanduser('~')

lazy.spawn(home + "/.scripts/rate.sh")

keys = [
    # Logout and restart
    Key([mod, "control"], "r",  lazy.restart(),     desc="Restart qtile"),
    Key([mod, "control"], "q",  lazy.shutdown(),    desc="Log out of session"),

    # From tych0: Note that this doesn't use mod: that's intentional in case
    # mod gets hosed (which happens if you unplug and replug your usb keyboard
    # sometimes, or on ubuntu upgrades). This way you can still log back out
    # and in gracefully.
    Key(["shift", "mod1"], "q", lazy.shutdown()),

    # Spawn terminal
    Key([mod], "Return",        lazy.spawn(term),   desc="Launch terminal"),

    # Switch between windows in current stack
    Key([mod], "l",             lazy.layout.down()),
    Key([mod], "h",             lazy.layout.up()),

    # Move windows up or down in current stack
    Key([mod, "shift"], "l",    lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h",    lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    Key([mod], "Tab",           lazy.next_layout(), desc="Toggle layouts"),
    Key([mod], "q",             lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "l", lazy.to_screen(0)),
    Key([mod, "control"], "h", lazy.to_screen(1)),

    # Run scripts
    Key([mod], "d", lazy.spawn(home + "/.scripts/rofi.sh"), desc="Run a program using rofi"),
    Key([mod, "shift"], "x", lazy.spawn(home + "/.scripts/lock.sh")),
]

# groups = [Group(i) for i in "asdfuiop"]
# New group definition from Derek Taylor (@DistroTube)
def init_group_names():
    return [
        ("MAIN", {'layout': 'stack'}),
        ("SYS", {'layout': 'matrix'}),
        ("DEV", {'layout': 'stack'}),
        ("PROD", {'layout': 'stack'}),
        ("WWW", {'layout': 'stack'}),
        ("MAIL", {'layout': 'stack'}),
        ("DOC", {'layout': 'stack'}),
        ("ENT", {'layout': 'stack'}),
        ("CHAT", {'layout': 'stack'}),
    ]

def init_groups():
    return [Group(name, **kwargs) for name, kwargs in group_names]

if __name__ in ["config", "__main__"]:
    group_names = init_group_names()
    groups = init_groups()

for i, (name, kwargs) in enumerate(group_names, 1):
    # Switch to another group
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
    # Send current window to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))

# Layout definition from Derek Taylor (@DistroTube)
layout_theme = {"border_width": 2,
                "margin": 6,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
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
