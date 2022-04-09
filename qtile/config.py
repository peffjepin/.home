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
from libqtile.config import (
    Click,
    Drag,
    Group,
    Key,
    Match,
    Screen,
    ScratchPad,
    DropDown,
)
from libqtile.lazy import lazy
from libqtile.log_utils import logger

logger.warning("Executing Qtile config.")
mod = "mod4"
terminal = "kitty"

MOD = [mod]
MODSHIFT = [mod, "shift"]
MODCTRL = [mod, "control"]
NOMOD = []

keys = [
    # change window focus
    Key(MOD, "h", lazy.layout.left()),
    Key(MOD, "l", lazy.layout.right()),
    Key(MOD, "j", lazy.layout.down()),
    Key(MOD, "k", lazy.layout.up()),
    Key(MOD, "space", lazy.layout.next()),
    Key(MOD, "Right", lazy.next_screen()),
    Key(MOD, "Left", lazy.next_screen()),

    # shuffle windows
    Key(MODSHIFT, "h", lazy.layout.shuffle_left()),
    Key(MODSHIFT, "l", lazy.layout.shuffle_right()),
    Key(MODSHIFT, "j", lazy.layout.shuffle_down()),
    Key(MODSHIFT, "k", lazy.layout.shuffle_up()),

    # change window size
    Key(MODCTRL, "h", lazy.layout.grow_left()),
    Key(MODCTRL, "l", lazy.layout.grow_right()),
    Key(MODCTRL, "j", lazy.layout.grow_down()),
    Key(MODCTRL, "k", lazy.layout.grow_up()),

    # cycle layouts
    Key(MOD, "Tab", lazy.next_layout()),

    # Restart / quit qtile
    Key(MODCTRL, "r", lazy.restart()),
    Key(MODCTRL, "q", lazy.shutdown()),

    # Spawn/kill applications
    Key(MOD, "r", lazy.spawncmd()),
    Key(MOD, "x", lazy.window.kill()),
    Key(NOMOD, "F1", lazy.group["scratchpad"].dropdown_toggle("term")),
]


theme = {
    "border_width": 3,
    "border_focus": os.environ["COLORSCHEME_ORANGE_L"],
    "border_normal": os.environ["COLORSCHEME_BG_L"],
    "margin": 0,
}

layouts = [
    layout.Columns(**theme),
    layout.Max(**theme),
    layout.MonadTall(**theme),
    layout.Matrix(**theme),
]

groups = [
    Group(name="DEV", spawn=terminal, layout="monadtall"),
    Group(name="WEB", spawn="firefox"),
    Group(name="SYS"),
    Group(name="GRID", layouts=[layout.Matrix(**theme)]),
]

group_key_map = {
    "w": "WEB",
    "d": "DEV",
    "s": "SYS",
    "g": "GRID",
}

for k, v in group_key_map.items():
    keybinds = [
        # mod1 + letter of group = switch to group
        Key(MOD, k, lazy.group[v].toscreen()),
        # mod1 + shift + letter of group to switch
        Key(MODSHIFT, k, lazy.window.togroup(v, switch_group=False)),
    ]
    keys.extend(keybinds)

sp = ScratchPad("scratchpad", [DropDown("term", terminal, height=0.6)])
groups.append(sp)

widget_defaults = dict(
    font="Fira Code",
    fontsize=16,
    padding=6,
)
extension_defaults = widget_defaults.copy()


def create_widgets():
    return [
        widget.GroupBox(
            active=os.environ["COLORSCHEME_FG_L"],
            inactive=os.environ["COLORSCHEME_FG_L"],
            foreground=os.environ["COLORSCHEME_FG_L"],
            background=None,
            border_width=0,
            center_aligned=True,
            font="Fira Code",
            fontshadow=os.environ["COLORSCHEME_BG_D"],
            fontsize=None,
            highlight_method="block",
            this_current_screen_border=os.environ["COLORSCHEME_ORANGE_D"],
            this_screen_border=os.environ["COLORSCHEME_ORANGE_D"],
            other_current_screen_border=os.environ["COLORSCHEME_BLUE_D"],
            other_screen_border=os.environ["COLORSCHEME_BLUE_D"],
            padding_y=0,
            padding_x=10,
            rounded=False,
        ),
        widget.Spacer(10),
        widget.TextBox("Layout:"),
        widget.CurrentLayout(),
        widget.Spacer(),
        widget.Prompt(),
        widget.Clock(format="%a %B %d %I:%M %p"),
    ]


bar_config = {
    "size": 30,
    "background": os.environ["COLORSCHEME_BG_M"],
    "margin": 0,
    "opacity": 1,
}

screens = [
    Screen(
        wallpaper="~/.config/background",
        wallpaper_mode="fill",
        top=bar.Bar(widgets=create_widgets(), **bar_config),
    ),
    Screen(
        wallpaper="~/.config/background",
        wallpaper_mode="fill",
        top=bar.Bar(widgets=create_widgets(), **bar_config),
    ),
]
# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod],
        "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size(),
    ),
    Click([mod], "Button2", lazy.window.toggle_floating()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the
        # wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="display"),
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
