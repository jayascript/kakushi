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
# Modified by Jaya Z. Moore (https://jayascript.xyz)

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

import os, subprocess

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, KeyChord, Screen, Match
from libqtile.lazy import lazy

from screeninfo import get_monitors

# Set global vars
mod = "mod4"
term = "alacritty"
home = os.path.expanduser('~')
num_screens = len(get_monitors())
sink = int(subprocess.check_output(
            "pactl list sinks | head -1 | grep -oh [0-9]*",
            shell = True).decode().strip())

# Run on login
lazy.spawn(home + "/.scripts/rate.sh")
lazy.spawn(home + "/.scripts/monitor_setup.sh")

# Set global colorscheme
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
    ["#5A5475", "#5A5475"], # Background: 5A5475
]

# Set global widget vars
widget_defaults = dict(
    font = 'Monofur',
    fontsize = 14,
    foreground = fairyfloss[0],
    padding = 3,
)
extension_defaults = widget_defaults.copy()

# Set global layout vars
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
         font = "Raleway",
         fontsize = 12,
         sections = ["1", "2", "3", "4", "5"],
         section_fontsize = 14,
         bg_color = "42395D",
         active_bg = "FFB8D1",
         active_fg = "42395D",
         inactive_bg = "8077A8",
         inactive_fg = "C2FFDF",
         padding_y = 5,
         section_top = 10,
         panel_width = 320
         ),
    #layout.Floating(**layout_theme)
]

# Drag floating layouts
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

# Set global group vars
group_names = [
    ("main", {
        'label': "🧁 TOP",
        'layout': 'monadtall',
        'matches': [
            Match(wm_class=['keepassxc'])
        ],
        'spawn': [
            'pavucontrol'
        ]
        }
     ),
    ("household", {
        'label': "🏠 FAM",
        'layout': 'monadtall',
        'spawn': [
         #   'mmex',
        ]
        }
    ),
    ("system", {
        'label': "💻 SYS",
        'layout': 'matrix',
        'spawn': [
            f'{term}',
        ]
        }
    ),
    ("development", {
        'label': "👩‍💻 DEV",
        'layout': 'monadtall',
        }
    ),
    ("productivity", {
        'label': "⏲️ CAL",
        'layout': 'monadtall',
        'matches': [
            Match(wm_class=['Gnome-pomodoro'])
        ],
        'spawn': [
            'gnome-pomodoro',
            f'{term} -e calcurse'
        ]
        }
    ),
    ("internet", {
        'label': "🌐 WWW",
        'layout': 'monadtall',
        'matches': [
            Match(wm_class=['Brave-browser',
                            'Chromium',
                            'LibreWolf',
                            'Pale moon',
                            'qutebrowser',
                            'Tor Browser',
                            ]
                  )
        ],
        'spawn': 'brave-browser',
        }
    ),
    ("email", {
        'label': "📫 BOX",
        'layout': 'monadtall',
        'matches': [
            Match(wm_class=['Thunderbird', 'ProtonMail Bridge'])
        ],
        'spawn': [
            #'protonmail-bridge',
            #f'{term} -e neomutt',
        ],
        }
    ),
    ("filesystem", {
        'label': "📁 DOC",
        'layout': 'monadtall',
        'matches': [
            Match(wm_class=['Org.gnome.Nautilus', 'Nextcloud'])
        ],
        'spawn': [
            f'{term} -e ranger',
            'nextcloud'
        ]
        }
    ),
    ("social", {
        'label': "💬 SOC",
        'layout': 'monadtall',
        'matches': [
            Match(wm_class=['Wire', 'Slack', 'discord'])
        ],
        'spawn': [
            #'wire-desktop',
            #'slack'
        ]
        }
    ),
    ("media", {
        'label': "🎵 ENT",
        'layout': 'monadtall',
        'matches': [
            Match(wm_class=['vlc', 'FreeTube'])
        ],
        'spawn': [
            #'freetube',
            #'vlc'
        ]
        }
    ),
]

group_names_fx= [
    ("news", {
        'label': "🔥 NEW",
        'layout': 'monadtall',
        'spawn': [
            f'{term} -e newsboat',
            f'{term} -e castero',
        ]
        }
     ),
    ("school", {
        'label': "🎓 LRN",
        'layout': 'monadtall',
        'matches': [
            Match(wm_class=['Firefox',
                            'Anki'
                            ])
        ],
        'spawn': [
            #'firefox',
            'anki',
        ]
        }
     ),
    ("writing", {
        'label': "📝 PEN",
        'layout': 'monadtall',
        }
     ),
]

# playerctl media control functions
def playpause(qtile):
    qtile.cmd_spawn("playerctl play-pause")

def playnext(qtile):
    qtile.cmd_spawn("playerctl next")

def playprev(qtile):
    qtile.cmd_spawn("playerctl previous")

def stopplay(qtile):
    qtile.cmd_spawn("playerctl stop")

# pactl media control functions
def volumeup(qtile, sink=sink):
    qtile.cmd_spawn(f"pactl set-sink-volume {sink} +5%")

def volumedown(qtile, sink=sink):
    qtile.cmd_spawn(f"pactl set-sink-volume {sink} -5%")

def mutevolume(qtile, sink=sink):
    qtile.cmd_spawn(f"pactl set-sink-mute {sink} toggle")

def mutemic(qtile, sink=sink):
    qtile.cmd_spawn(f"pactl set-source-mute {sink} toggle")

# light backlight control functions
def backlightup(qtile):
    qtile.cmd_spawn("sudo light -A 10")

def backlightup_fine(qtile):
    qtile.cmd_spawn("sudo light -A 5")

def backlightdown(qtile):
    qtile.cmd_spawn("sudo light -U 10")

def backlightdown_fine(qtile):
    qtile.cmd_spawn("sudo light -U 5")

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
    Key(
        [mod, "shift"], "p",
        lazy.spawn(home + "/.scripts/passmenu.sh"),
        desc="Launch passmenu"
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
        [mod, "mod1"], "g",
        lazy.spawn(term + " -e gourmet"),
        desc="Launch gourmet"
    ),
    Key(
        [mod, "mod1"], "m",
        lazy.spawn(term + " -e neomutt"),
        desc="Launch neomutt"
    ),
    Key(
        [mod, "mod1"], "n",
        lazy.spawn(term + " -e newsboat"),
        desc="Launch newsboat"
    ),
    Key(
        [mod, "mod1"], "p",
        lazy.spawn(term + " -e podboat"),
        desc="Launch podboat"
    ),
    Key(
        [mod, "mod1"], "r",
        lazy.spawn(term + " -e ranger"),
        desc="Launch ranger"
    ),
    Key(
        [mod, "mod1"], "v",
        lazy.spawn(term + " -e vifm"),
        desc="Launch Vi[m] File Manager"
    ),

    # Launch browser mode
    KeyChord([mod], "b", [
        Key([], "b", lazy.spawn("brave-browser")),
        Key([], "c", lazy.spawn("chromium")),
        Key([], "f", lazy.spawn("firefox")),
        Key([], "i", lazy.spawn(home + "/apps/LibreWolf-84.0.2-1.x86_64.AppImage")),
        Key([], "l", lazy.spawn(term + " -e lynx")),
        Key([], "p", lazy.spawn("palemoon")),
        Key([], "q", lazy.spawn("qutebrowser")),
        Key([], "t", lazy.spawn("/opt/tor-browser_en-US/Browser/start-tor-browser")),
    ], mode="Browsers: (b) brave; (c) chromium; (f) firefox; (i) librewolf; " \
            "(l) lynx; (p) palemoon; (q) qutebrowser; (t) tor;"),

    # playerctl controls
    Key(
        [], "XF86AudioPlay",
        lazy.function(playpause),
    ),
    Key(
        [], "XF86AudioNext",
        lazy.function(playnext),
    ),
    Key(
        [], "XF86AudioPrev",
        lazy.function(playprev),
    ),
    Key(
        [], "XF86AudioStop",
        lazy.function(stopplay),
    ),

    # pactl controls
    Key(
        [], "XF86AudioRaiseVolume",
        lazy.function(volumeup),
    ),
    Key(
        [], "XF86AudioLowerVolume",
        lazy.function(volumedown),
    ),
    Key(
        [], "XF86AudioMute",
        lazy.function(mutevolume),
    ),
    Key(
        [], "XF86AudioMicMute",
        lazy.function(mutemic),
    ),

    # light controls
    Key(
        [], "XF86MonBrightnessUp",
        lazy.function(backlightup),
    ),
    Key(
        [], "XF86MonBrightnessDown",
        lazy.function(backlightdown),
    ),
    Key(
        [mod], "XF86MonBrightnessUp",
        lazy.function(backlightup_fine),
    ),
    Key(
        [mod], "XF86MonBrightnessDown",
        lazy.function(backlightdown_fine),
    ),
]

for i, (name, kwargs) in enumerate(group_names, 0):
    # Switch to another group
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
    # Send current window to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))

function_keys = ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8"]
for i, (name, kwargs) in enumerate(group_names_fx, 0):
    key = function_keys[i]
    # Switch to another group
    keys.append(Key([mod], key, lazy.group[name].toscreen()))
    # Send current window to another group
    keys.append(Key([mod, "shift"], key, lazy.window.togroup(name)))

def init_groups():
    return [Group(name, **kwargs) for name, kwargs in group_names] + [Group(name, **kwargs) for name, kwargs in group_names_fx]

def set_widgets():
    sep = widget.Sep(
        linewidth = 0,
        padding = 50,
    )
    widgets = [
        widget.CurrentLayoutIcon(
            foreground = fairyfloss[0],
            padding=5,
        ),
        widget.CurrentLayout(
            fmt = "{}",
            foreground = fairyfloss[0],
            padding=5,
        ),
        widget.Chord(
            fmt = "{}",
            foreground = fairyfloss[0],
            padding=5,
        ),
        widget.GroupBox(
            active = fairyfloss[10], # Active window font color
            highlight_method = "block",
            inactive = fairyfloss[0], # Inactive window font color
            other_current_screen_border = fairyfloss[9],
            other_screen_border = fairyfloss[9],
            this_current_screen_border = fairyfloss[15], # Active and focused
            this_screen_border = fairyfloss[9],
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
            directory = home + '/Media/Pictures/Wallpapers/kawaii',
            random_selection = True,
            fmt = "",
        )
    ]
    return widgets


if __name__ in ["config", "__main__"]:
    groups = init_groups()

    if num_screens == 2:
        screens = [
            Screen(bottom=bar.Bar(set_widgets(), 30, background=fairyfloss[9])),
            Screen(bottom=bar.Bar(set_widgets(), 30, background=fairyfloss[9])),
        ]
    else:
        screens = [
            Screen(bottom=bar.Bar(set_widgets(), 30, background=fairyfloss[9]))
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
