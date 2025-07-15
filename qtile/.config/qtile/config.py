import os
import subprocess
from libqtile import bar, hook, layout, qtile, widget
from libqtile.config import Click, Drag, DropDown, Group, Key, KeyChord, Match, Screen, ScratchPad
from libqtile.lazy import lazy
from pathlib import Path

mod = "mod4"
terminal = "kitty"
browser = "flatpak run io.gitlab.librewolf-community"
home = str(Path.home())
emacs = "emacsclient -c -a 'emacs'"


# dracula colors
colors = [
    "#282A36", # BACKGROUND
    "#44475A", # SELECTION
    "#F8F8F2", # FOREGROUND
    "#6272A4", # COMMENT
    "#8BE9FD", # CYAN
    "#50FA7B", # GREEN
    "#FFB86C", # ORANGE
    "#FF79C6", # PINK
    "#BD93F9", # PURPLE
    "#FF5555", # RED
    "#F1FA8C"  # YELLOW
]

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    #Key(
    #    [mod, "shift"],
    #    "Return",
    #    lazy.layout.toggle_split(),
    #    desc="Toggle between split and unsplit sides of stack",
    #),
    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-")),
    # Launch programs
    Key([mod, "shift"], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch browser"),
    Key([mod], "e", lazy.spawn("rofi -modi emoji -show emoji"), desc="Launch rofi-emoji"),
    Key([mod], "d", lazy.spawn("rofi -show drun"), desc="Launch rofi"),
    KeyChord([mod], "p", [
        KeyChord([], "f", [
            Key([], "f", lazy.spawn("flameshot full --path " + home + "/Pictures/screenshots/")),
            Key([], "s", lazy.spawn("flameshot gui --path " + home + "/Pictures/screenshots/")),
        ]),
        Key([], "e", lazy.spawn(emacs), desc="Launch emacs"),
        # picom
        Key([], "p", lazy.spawn("toggle-picom.sh"), desc= "Toggle transparency")
    ]),
    #ScratchPad
    Key([mod], "Return", lazy.group["scratchpad"].dropdown_toggle("term")),
    Key([mod], "m", lazy.group["scratchpad"].dropdown_toggle("music")),
    Key([mod], "v", lazy.group["scratchpad"].dropdown_toggle("pulsemixer")),
    # Power
    KeyChord([mod], "x", [
        Key([], "s", lazy.spawn("shutdown now")),
        Key([], "r", lazy.spawn("reboot"))
    ]),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


#groups = [Group(i) for i in "1234567890"]
groups = [

    Group("1", matches=[
            Match(wm_class="Eclipse"),
            Match(wm_class="jetbrains-idea-ce"),
            Match(wm_class="VSCodium")
        ]
    ),
    Group("2", matches=[
            Match(wm_class="librewolf"),
            Match(wm_class="org.mozilla.firefox"),
            Match(wm_class="Chromium-browser")
        ], layout="max"
    ),
    Group("3", matches=[
            Match(wm_class="soffice"),
            Match(wm_class="Logseq"),
            Match(wm_class="Anki")
        ]
    ),
    Group("4", matches=[
            Match(wm_class="TelegramDesktop"),
            Match(wm_class="discord"),
            Match(wm_class="WebCord")
        ], layout="max"
    ),
    Group("5", matches=[
            Match(wm_class="Mailspring")
        ]
    ),
    Group("6", matches=[
            Match(wm_class="VirtualBox Manager"),
            Match(wm_class="Virt-manager")
        ]
    ),
    Group("7", matches=[
            Match(wm_class="qBittorrent")
        ]
    ),
    Group("8"),
    Group("9", matches=[
            Match(wm_class="steam"),
            Match(wm_class="PrismLauncher")
        ]
    ),
    Group("0", matches=[
            Match(wm_class="mpv"),
            Match(wm_class="FreeTube")
        ], layout="max"
    )
]


for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod + shift + group number = switch to & move focused window to group
            #Key(
            #    [mod, "shift"],
            #    i.name,
            #    lazy.window.togroup(i.name, switch_group=True),
            #    desc="Switch to & move focused window to group {}".format(i.name),
            #),
            #
            # mod + shift + group number = move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name)
            ),
        ]
    )

groups.append(
    ScratchPad("scratchpad", [
            DropDown("term", terminal,
                     width=0.9, height=0.8,  x=0.05, y=0.09, opacity=1.0,
                     on_focus_lost_hide=True),
            DropDown("music", terminal + " cmus",
                    width=0.9, height=0.8, x=0.05, y=0.09, opacity=1.0,
                    on_focus_lost_hide=True),
            DropDown("pulsemixer", terminal + " pulsemixer",
                    width=0.9, height=0.8, x=0.05, y=0.09, opacity=1.0,
                    on_focus_lost_hide=True)
            ]
    )
)

layout_theme = {
    "margin": 6,
    "border_normal": colors[0],
    "border_focus": colors[5],
    "border_width": 2
}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme)
    #layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=13,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(this_current_screen_border=colors[8], active=colors[2], inactive=colors[1], block_highlight_text_color=colors[10], highlight_method="block", urgent_border=colors[9]),
                widget.Sep(foreground=colors[3]),
                widget.CurrentLayoutIcon(foreground=colors[2]),
                widget.Sep(foreground=colors[3]),
                widget.WindowName(foreground=colors[5], max_chars=64),
                widget.Cmus(paused_color=colors[10], playing_color=colors[7], stopped_color=colors[3], width=256, foreground=colors[2], scroll=True, scroll_clear=True, scroll_delay=0.5, scroll_step=3),
                widget.Sep(foreground=colors[3]),
                widget.Systray(),
                widget.Sep(foreground=colors[3]),
                widget.Battery(discharge_char='v', foreground=colors[2], format="{char} {percent:2.0%}", low_background=colors[10], low_foreground=colors[9], low_percentage=0.2) if os.environ.get('QTILE_DEVICE_TYPE', 'DESKTOP') == 'LAPTOP' else widget.CPU(),
                widget.Sep(foreground=colors[3]),
                #widget.Battery(),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Clock(foreground=colors[2], format="%Y-%m-%d %a %H:%M"),
            ],
            24,
            background=colors[0]
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run([script])

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=colors[6],
    border_width=2,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="Xdg-desktop-portal-gtk"),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "Qtile"
