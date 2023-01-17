###################################
## IMPORTS/AUTOSTART/DEFINITIONS ##
###################################

import os
import subprocess
from libqtile import bar, layout, widget, hook, qtile, config
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.backend import base

@hook.subscribe.startup_once
def autostart ():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

mod = "mod4"

###################################
############# COLORS ##############
###################################

colors = [["#141414", "#141414"],   #0  background
          ["#b3b3b3", "#b3b3b3"],   #1  light_gray
          ["#999999", "#999999"],   #2  lighter_gray
          ["#4c4c4c", "#4c4c4c"],   #3  light_dark_gray
          ["#3c3c3c", "#3c3c3c"],   #4  gray
          ["#2c2c2c", "#2c2c2c"],   #5  darker_gray
          ["#141414", "#141414"],   #6  dark_gray
          ["#0180d3", "#0180d3"],   #7  blue
          ["#015187", "#015187"],   #8  darker_blue
          ["#01d3d3", "#01d3d3"],   #9  cyan
          ["#ffffff", "#ffffff"],   #10 white
          ["#1a1a1a", "#1a1a1a"],   #10 lighter background
          ["#212121", "#212121"]]   #11 light background

###################################
########### KEYBINDINGS ###########
###################################

keys = [
    # Launch Apps
    Key([mod], "b", lazy.spawn("firefox"), desc="Launch Browser"),
    Key([mod], "Tab", lazy.spawn("kitty"), desc="Launch Terminal"),
    Key([mod], "t", lazy.spawn("pcmanfm"), desc="Launch File Manager"),
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Launch App Launcher"),
    Key([mod, "shift"], "e", lazy.spawn("rofi -show power-menu -modi power-menu:rofi-power-menu"), desc="Power Options"),
    Key([mod], "s", lazy.spawn("flameshot gui"), desc="Screenshot Tool"),
    Key([mod], "d", lazy.spawn("discord"), desc="Launch Discord"),
    Key([mod], "g", lazy.spawn("steam"), desc="Launch Steam"),
    Key([mod], "e", lazy.spawn("mailspring"), desc="Launch Mail App"),
    Key([mod], "m", lazy.spawn("virt-manager"), desc="Launch Virtual Machine Manager"),
    Key([mod], "o", lazy.spawn("/usr/bin/flatpak run --branch=stable --arch=x86_64 --command=obs com.obsproject.Studio"), desc="Launch OBS"),
    Key([mod], "escape", lazy.spawn("betterlockscreen -l blur"), desc="Lock Screen"),

    # Change focus/Move Focused Window/Resize Focused Window
    Key([mod], "h", lazy.layout.left(), desc="Move focus left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "u", lazy.layout.grow_left(), desc="Resize window left"),
    Key([mod, "shift"], "p", lazy.layout.grow_right(), desc="Resize window right"),
    Key([mod, "shift"], "i", lazy.layout.grow_down(), desc="Resize window down"),
    Key([mod, "shift"], "o", lazy.layout.grow_up(), desc="Resize window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Essential Keybinds
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "space", lazy.window.toggle_floating()),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
]

###################################
############## GROUPS #############
###################################

groups = [
    Group("1", label="1", matches=[Match(wm_class=['firefox'])]),
    Group("2", label="2"),
    Group("3", label="3"),
    Group("4", label="4", matches=[Match(wm_class=['libreoffice-startcenter', 'libreoffice-writer', 'libreoffice-draw', 'libreoffice-calc', 'libreoffice-impress', 'libreoffice-math'])]),
    Group("5", label="5", matches=[Match(wm_class=['VirtualBox Machine', 'VirtualBox Manager', 'Virt-manager'])]),
    Group("6", label="6", matches=[Match(wm_class=['discord'])]),
    Group("7", label="7", matches=[Match(wm_class=['MuseScore3', 'Spotify'])]),
    Group("8", label="8", matches=[Match(wm_class=['obs'])]),
    Group("9", label="9", matches=[Match(wm_class=['Steam', 'heroic', 'Lutris', 'GeForce NOW', 'lunarclient'])]),
    Group("0", label="10", matches=[Match(wm_class=['Mailspring'])])
    ]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = move focused window to group
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name)),
        ]
    )

###################################
########### SCRATCHPADS ###########
###################################

# Definitions
groups.append(ScratchPad("scratchpad", [
    DropDown("termsp", "kitty -T termsp", width=0.7, height=0.7, x=0.15, y=0.15, opacity=1),
    DropDown("bitwardensp", "bitwarden-desktop", width=0.7, height=0.7, x=0.15, y=0.15, opacity=1),
    DropDown("cmussp", "kitty -T cmussp -e cmus", width=0.7, height=0.7, x=0.15, y=0.15, opacity=1),
]))

# Keybindings
keys.extend([
    Key([mod], "z", lazy.group['scratchpad'].dropdown_toggle('termsp')),
    Key([mod], "x", lazy.group['scratchpad'].dropdown_toggle('bitwardensp')),
    Key([mod], "c", lazy.group['scratchpad'].dropdown_toggle('cmussp')),
])

###################################
############# LAYOUTS #############
###################################

# Default window border style
layout_border = dict(
    border_focus=colors[4],
    border_normal=colors[6],
)

layouts = [
    layout.Columns(**layout_border, margin=6, margin_on_single=0,  border_width=2),
    ]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(
        **layout_border,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

# Make picture in picture mode open with specific dimensions
to_position = config.Match(title="Picture-in-Picture")
@hook.subscribe.client_managed
def _(win: base.WindowType) -> None:
    if isinstance(win, base.Window):
        if win.match(to_position):
            win.cmd_set_position_floating(1960, 125)
            win.cmd_set_size_floating(1280, 720)

###################################
######## BAR CONFIGURATION ########
###################################

widget_defaults = dict(
    font="JetBrainsMonoMedium NF",
    fontsize=13,
    padding=2,
    background=colors[0]
)
screens = [
    Screen(
        top=bar.Bar([
            widget.Spacer(length=10
            ),
            widget.GroupBox(rounded=True,
                highlight_method="block",
                margin_x=1,
                margin_y=3,
                padding_x=8,
                padding_y=3,
                this_current_screen_border=colors[7],
                this_screen_border=colors[5],
                inactive=colors[3],
                other_current_screen_border=colors[7],
                other_screen_border=colors[5],
                disable_drag=True,
                fontsize=14,
                borderwidth=1,
                ),
                widget.Spacer(length=10
                ),
                widget.TaskList(border=colors[5],
                background=colors[0],
                icon_size=0,
                fontsize=14,
                highlight_method="block",
                padding_y=7,
                margin=-1,
                title_width_method = "uniform",
                rounded=True
                ),
                widget.Spacer(length=6
                ),
                widget.Cmus(play_color=colors[9],
                noplay_color=colors[1]
                ),
                widget.Spacer(length=2
                ),
                widget.TextBox('',
                font='Font Awesome 5 Free',
                fontsize=17
                ),
                widget.PulseVolume(
                ),
                widget.Spacer(length=10
                ),
                widget.TextBox(' ',
                font='Font Awesome 5 Free',
                fontsize=17,
                foreground=colors[7]
                ),
                widget.Spacer(length=-2
                ),
                widget.Memory(measure_mem='G',
                update_interval=2,
                format=' {MemUsed:.1f}{mm}'
                ),
                widget.Spacer(length=10
                ),
                widget.TextBox(' ',
                font='JetBrainsMono Nerd Font',
                fontsize=24,
                foreground=colors[7]
                ),
                widget.Spacer(length=-5,
                ),
                widget.CPU(format='{load_percent:.0f}%',
                update_interval=2
                ),
                widget.Spacer(length=10
                ),
                widget.TextBox('',
                font='Font Awesome 5 Free Solid',
                fontsize=17,
                foreground=colors[7]
                ),
                widget.Clock(format="%T %m/%d/%y"
                ),
                widget.Spacer(length=5
                ),
                widget.Systray(
                ),
                widget.Spacer(length=10
                ),
            ],
            size=30,
            ),
        ),
    Screen(
        top=bar.Bar([
            widget.Spacer(length=10
            ),
            widget.GroupBox(rounded=True,
                highlight_method="block",
                margin_x=1,
                margin_y=3,
                padding_x=8,
                padding_y=3,
                this_current_screen_border=colors[7],
                this_screen_border=colors[5],
                inactive=colors[3],
                other_current_screen_border=colors[7],
                other_screen_border=colors[5],
                disable_drag=True,
                fontsize=14,
                borderwidth=1,
                ),
                widget.Spacer(length=10
                ),
                widget.TaskList(border=colors[5],
                background=colors[0],
                icon_size=0,
                fontsize=14,
                highlight_method="block",
                padding_y=6,
                margin=-1,
                title_width_method = "uniform",
                rounded=True
                ),
                widget.Spacer(length=6
                ),
                widget.TextBox('',
                font='Font Awesome 5 Free Solid',
                fontsize=17,
                foreground=colors[7]
                ),
                widget.Clock(format="%T %m/%d/%y"
                ),
                widget.Spacer(length=5
                ),
            ],
            28),
        )
    ]

###################################
########## OTHER SETTINGS #########
###################################

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "Qtile"


# The following file contains comments that are the copyright and licensing
# information from the default qtile config. Copyright (c) 2010 Aldo Cortesi, 
# 2010, 2014 dequis, 2012 Randall Ma, 2012-2014 Tycho Andersen, 2012 Craig Barne, 
# 2013 horsik, 2013 Tao Sauvage
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
