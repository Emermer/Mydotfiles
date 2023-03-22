import os
import subprocess
from libqtile import bar, layout, widget, hook, qtile, config
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.backend import base

mod = "mod4" # mod4 = super key (windows key)
browser = "firefox"
fm = "pcmanfm"
term = "alacritty"

# Keybindings
keys = [
    Key([mod], "b", lazy.spawn([browser]), desc="Launch Browser"),
    Key([mod], "Tab", lazy.spawn([term]), desc="Launch Terminal"),
    Key([mod], "t", lazy.spawn([fm]), desc="Launch File Manager"),
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Launch App Launcher"),
    Key([mod, "shift"], "e", lazy.spawn("rofi -show power-menu -modi power-menu:rofi-power-menu"), desc="Power Options"),
    Key([mod], "s", lazy.spawn("flameshot gui"), desc="Screenshot Tool"),
    Key([mod], "d", lazy.spawn("webcord"), desc="Launch WebCord"),
    Key([mod], "g", lazy.spawn("steam"), desc="Launch Steam"),
    Key([mod], "v", lazy.spawn("virt-manager"), desc="Launch Virtual Machine Manager"),
    Key([mod], "e", lazy.spawn("emacsclient -c -a 'emacs'"), desc="Launch the Emacs client"),
    Key([mod], "a", lazy.spawn("/usr/bin/flatpak run --branch=stable --arch=x86_64 --command=bottles --file-forwarding com.usebottles.bottles"), desc="Launch Bottles"),
    Key([mod], "o", lazy.spawn("/usr/bin/flatpak run --branch=stable --arch=x86_64 --command=obs com.obsproject.Studio"), desc="Launch OBS"),
    Key([mod], "p", lazy.spawn("pavucontrol"), desc="Launch Volume Controller"),
    Key([mod], "m", lazy.spawn("mailspring"), desc="Launch Mailspring"),
    Key([mod], "escape", lazy.spawn("betterlockscreen -l blur"), desc="Lock Screen"),
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
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([mod], "space", lazy.window.toggle_floating(), desc="Toggle floating"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
]

# Groups
groups = [
    Group("1", label="1", matches=[Match(wm_class=['firefox'])]),
    Group("2", label="2"),
    Group("3", label="3"),
    Group("4", label="4", matches=[Match(wm_class=['libreoffice-writer', 'libreoffice-draw', 'libreoffice-calc', 'libreoffice-impress', 'libreoffice-math'])]),
    Group("5", label="5", matches=[Match(wm_class=['VirtualBox Machine', 'VirtualBox Manager', 'Virt-manager'])]),
    Group("6", label="6", matches=[Match(wm_class=['discord', 'WebCord'])]),
    Group("7", label="7", matches=[Match(wm_class=['MuseScore3', 'ableton live 11 lite.exe'])]),
    Group("8", label="8", matches=[Match(wm_class=['obs'])]),
    Group("9", label="9", matches=[Match(wm_class=['Steam', 'heroic', 'Lutris', 'GeForce NOW', 'lunarclient', 'Gimp-2.10'])]),
    ]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name)),
        ]
    )

# Scratchpads
groups.append(ScratchPad('scratchpad', [
    DropDown('termsp', 'alacritty -t termsp', width=0.7, height=0.7, x=0.15, y=0.15, opacity=1),
    DropDown('bitwardensp', "bitwarden-desktop", width=0.7, height=0.7, x=0.15, y=0.15, opacity=1),
    DropDown('cmussp', 'alacritty -t cmussp -e cmus', width=0.7, height=0.7, x=0.15, y=0.15, opacity=1),
]))

keys.extend([
    Key([mod], "z", lazy.group['scratchpad'].dropdown_toggle('termsp'), desc="Show terminal scratchpad"),
    Key([mod], "x", lazy.group['scratchpad'].dropdown_toggle('bitwardensp'), desc="Show bitwarden scratchpad"),
    Key([mod], "c", lazy.group['scratchpad'].dropdown_toggle('cmussp'), desc="Show cmus scratchpad"),
])

# Colors
colors = [["#141414", "#141414"],   #0  background
          ["#b3b3b3", "#b3b3b3"],   #1  light_gray
          ["#999999", "#999999"],   #2  lighter_gray
          ["#4c4c4c", "#4c4c4c"],   #3  light_dark_gray
          ["#3c3c3c", "#3c3c3c"],   #4  gray
          ["#2c2c2c", "#2c2c2c"],   #5  darker_gray
          ["#0180d3", "#0180d3"],   #6  blue
          ["#015187", "#015187"],   #7  darker_blue
          ["#01d3d3", "#01d3d3"],   #8  cyan
          ["#ffffff", "#ffffff"],   #9  white
          ["#1a1a1a", "#1a1a1a"],   #10 lighter background
          ["#212121", "#212121"]]   #11 light background

# Layout Border Theme
layout_border = dict(
    border_focus=colors[4],
    border_normal=colors[0],
)

# Layouts
layouts = [
    layout.Columns(**layout_border,
                   margin=8,
                   border_width=2,
                   border_on_single=True,
                   insert_position=1),
    ]

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

widget_defaults = dict(
    font="JetBrainsMonoMedium NF",
    fontsize=13,
    padding=2,
    background=colors[0]

# Bar
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
                this_current_screen_border=colors[6],
                this_screen_border=colors[5],
                inactive=colors[3],
                other_current_screen_border=colors[6],
                other_screen_border=colors[5],
                disable_drag=True,
                fontsize=14,
                borderwidth=1,
                ),
                widget.Spacer(length=6
                ),
                widget.TaskList(border=colors[11],
                background=colors[0],
                icon_size=0,
                fontsize=14,
                highlight_method="block",
                padding_y=7,
                margin=-1,
                title_width_method = "uniform",
                rounded=False
                ),
                widget.Spacer(length=6
                ),
                widget.Systray(
                ),
                widget.Spacer(length=6
                ),
                widget.Cmus(play_color=colors[8],
                noplay_color=colors[1]
                ),
                widget.Spacer(length=6
                ),
                widget.TextBox('',
                font='Font Awesome 5 Free',
                fontsize=17
                ),
                widget.PulseVolume(
                ),
                widget.Spacer(length=6
                ),
                widget.TextBox(' ',
                font='Font Awesome 5 Free',
                fontsize=17,
                foreground=colors[6]
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
                foreground=colors[6]
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
                foreground=colors[6]
                ),
                widget.Clock(format="%r %D"
                ),
                widget.Spacer(length=5
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
                this_current_screen_border=colors[6],
                this_screen_border=colors[5],
                inactive=colors[3],
                other_current_screen_border=colors[6],
                other_screen_border=colors[5],
                disable_drag=True,
                fontsize=14,
                borderwidth=1,
                ),
                widget.Spacer(length=6
                ),
                widget.TaskList(border=colors[11],
                background=colors[0],
                icon_size=0,
                fontsize=14,
                highlight_method="block",
                padding_y=6,
                margin=-1,
                title_width_method = "uniform",
                rounded=False
                ),
                widget.Spacer(length=6
                ),
                widget.TextBox('',
                font='Font Awesome 5 Free Solid',
                fontsize=17,
                foreground=colors[6]
                ),
                widget.Clock(format="%r %D"
                ),
                widget.Spacer(length=5
                ),
            ],
            28),
        )
    ]

# Autostart
@hook.subscribe.startup_once
def autostart ():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

# Other Settings
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "Qtile"
