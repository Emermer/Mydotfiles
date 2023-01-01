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

def init_colors():
    return [["#212121", "#212121"],   #0  background
            ["#b3b3b3", "#b3b3b3"],   #1  light_gray
            ["#999999", "#999999"],   #2  lighter_gray
            ["#4c4c4c", "#4c4c4c"],   #3  light_dark_gray
            ["#3c3c3c", "#3c3c3c"],   #4  gray
            ["#2c2c2c", "#2c2c2c"],   #5  darker_gray
            ["#141414", "#141414"],   #6  dark_gray
            ["#0180d3", "#0180d3"],   #7  blue
            ["#015187", "#015187"],   #8  darker_blue
            ["#01d3d3", "#01d3d3"]]   #9 cyan

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
    Group("1", label="1"),
    Group("2", label="2"),
    Group("3", label="3"),
    Group("4", label="4 ", matches=[Match(wm_class=['Mailspring'])]),
    Group("5", label="5 ", matches=[Match(wm_class=['Steam', 'heroic', 'Lutris', 'GeForce NOW', 'lunarclient'])]),
    Group("6", label="6 ", matches=[Match(wm_class=['VirtualBox Machine', 'VirtualBox Manager', 'Virt-manager'])]),
    Group("7", label="7"),
    Group("8", label="8"),
    Group("9", label="9 ", matches=[Match(wm_class=['discord'])]),
    Group("0", label="10 ", matches=[Match(wm_class=['obs'])]),
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
    layout.Columns(**layout_border, margin=6, margin_on_single=0, border_width=2),
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
    fontsize=14,
    padding=2,
    background=colors[0]
)
screens = [
    Screen(
        top=bar.Bar([
            widget.GroupBox(rounded=False,
                highlight_method="block",
                margin_x=0,
                margin_y=5,
                padding_x=8,
                padding_y=7,
                this_current_screen_border=colors[7],
                this_screen_border=colors[4],
                inactive=colors[2],
                other_current_screen_border=colors[7],
                other_screen_border=colors[4],
                disable_drag=True,
                fontsize=16,
                font='Font Awesome 5 Free Solid'
                ),
                widget.Spacer(length=20
                ),
                widget.Sep(
                ),
                widget.Spacer(length=5
                ),
                widget.TaskList(border=colors[8],
                background=colors[6],
                icon_size=0,
                highlight_method="block",
                padding=10,
                padding_y=8,
                margin=-2,
                title_width_method = "uniform",
                rounded=False
                ),
                widget.Spacer(length=5
                ),
                widget.Sep(
                ),
                widget.Spacer(length=20
                ),
                widget.Systray(
                ),
                widget.TextBox('',
                font='Font Awesome 5 Free',
                fontsize=30,
                foreground=colors[5],
                padding=0
                ),
                widget.Cmus(play_color=colors[8],
                noplay_color=colors[1],
                background=colors[5]
                ),
                widget.TextBox('  ',
                fontsize=30,
                padding=-14,
                background=colors[5]
                ),
                widget.PulseVolume(
                background=colors[5]
                ),
                widget.TextBox(' ',
                font='Font Awesome 5 Free',
                fontsize=17,
                foreground=colors[7],
                background=colors[5]
                ),
                widget.Spacer(length=-2,
                background=colors[5]
                ),
                widget.Memory(measure_mem='G',
                background=colors[5],
                update_interval=2,
                format='{MemUsed: .0f}{mm} /{MemTotal: .0f}{mm}'
                ),
                widget.Spacer(length=10,
                background=colors[5]
                ),
                widget.TextBox(' ',
                font='JetBrainsMono Nerd Font',
                fontsize=24,
                foreground=colors[7],
                background=colors[5]
                ),
                widget.Spacer(length=-5,
                ),
                widget.CPU(format='{load_percent}%',
                background=colors[5],
                update_interval=2
                ),
                widget.TextBox('',
                font='Font Awesome 5 Free',
                fontsize=30,
                foreground=colors[6],
                background=colors[5],
                padding=0
                ),
                widget.Spacer(length=4,
                background=colors[6]
                ),
                widget.TextBox('',
                font='Font Awesome 5 Free Solid',
                fontsize=17,
                foreground=colors[7],
                background=colors[6],
                ),
                widget.Clock(format="%a %m/%d/%y",
                background=colors[6]
                ),
                widget.Spacer(length=4,
                background=colors[6]
                ),
                widget.TextBox('',
                font='Font Awesome 5 Free Solid',
                fontsize=17,
                foreground=colors[7],
                background=colors[6]
                ),
                widget.Clock(format="%I:%M:%S%p",
                background=colors[6]
                ),
                widget.Spacer(length=6,
                background=colors[6]
                ),
            ],
            30),
        ),
    Screen(
        top=bar.Bar([
            widget.GroupBox(rounded=False,
                highlight_method="block",
                margin_x=0,
                margin_y=5,
                padding_x=8,
                padding_y=7,
                this_current_screen_border=colors[7],
                this_screen_border=colors[4],
                inactive=colors[2],
                other_current_screen_border=colors[7],
                other_screen_border=colors[4],
                disable_drag=True,
                hide_unused=True,
                fontsize=16,
                font='Font Awesome 5 Free Solid'
                ),
                widget.Spacer(length=20
                ),
                widget.TextBox('',
                font='Font Awesome 5 Free',
                fontsize=30,
                foreground=colors[5],
                padding=0
                ),
                widget.Spacer(length=4,
                background=colors[5]
                ),
                widget.TextBox(' ',
                font='Font Awesome 5 Free',
                fontsize=17,
                foreground=colors[7],
                background=colors[5]
                ),
                widget.Memory(
                background=colors[5],
                update_interval=2,
                format='{MemUsed: .0f}{mm} /{MemTotal: .0f}{mm}'
                ),
                widget.Spacer(length=10,
                background=colors[5]
                ),
                widget.TextBox(' ',
                font='JetBrainsMono Nerd Font',
                fontsize=24,
                foreground=colors[7],
                background=colors[5]
                ),
                widget.Spacer(length=-10,
                background=colors[5]
                ),
                widget.CPU(format='{load_percent}% {freq_current}GHz',
                background=colors[5],
                update_interval=2
                ),
                widget.Spacer(length=10,
                background=colors[5]
                ),
                widget.TextBox('',
                font='Font Awesome 5 Free',
                fontsize=30,
                foreground=colors[6],
                background=colors[5],
                padding=0
                ),
                widget.Spacer(length=4,
                background=colors[6]
                ),
                widget.TextBox('',
                font='Font Awesome 5 Free Solid',
                fontsize=17,
                foreground=colors[7],
                background=colors[6],
                ),
                widget.Clock(format="%a %m/%d/%y",
                background=colors[6]
                ),
                widget.Spacer(length=4,
                background=colors[6]
                ),
                widget.TextBox('',
                font='Font Awesome 5 Free Solid',
                fontsize=17,
                foreground=colors[7],
                background=colors[6]
                ),
                widget.Clock(format="%I:%M:%S%p",
                background=colors[6]
                ),
                widget.Spacer(length=10,
                background=colors[6]
                ),
                widget.Sep(
                ),
                widget.Spacer(length=5
                ),
                widget.TaskList(border=colors[8],
                background=colors[6],
                icon_size=0,
                highlight_method="block",
                padding=10,
                padding_y=8,
                margin=-2,
                title_width_method = "uniform",
                rounded=False
                ),
                widget.Spacer(length=5
                ),
                widget.Sep(
                ),
                widget.Spacer(length=10,
                background=colors[6]
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
