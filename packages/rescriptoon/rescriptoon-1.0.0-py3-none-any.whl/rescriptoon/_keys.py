"""
rescriptoon
Copyright (C) 2018-2019 Fabian Peter Hammerle <fabian@hammerle.me>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import enum
import typing

from Xlib import XK


class USKeyCode(enum.Enum):
    w = 25
    e = 26
    i = 31
    o = 32
    ctrl_left = 37
    a = 38
    s = 39
    d = 40
    f = 41
    j = 44
    k = 45
    l = 46
    semicolon = 47
    grave = 49
    v = 55
    n = 57
    slash = 61
    space = 65


_KEYSYM_LABELS = {
    # pylint: disable=no-member; false positive
    XK.XK_Control_L: "left ctrl",
    XK.XK_Control_R: "right ctrl",
    XK.XK_Delete: "delete",
    XK.XK_Down: "↓",
    XK.XK_Left: "→",
    XK.XK_Right: "←",
    XK.XK_Up: "↑",
    XK.XK_space: "␣",
}


def keysym_to_label(keysym: int) -> typing.Optional[str]:
    return _KEYSYM_LABELS.get(keysym, XK.keysym_to_string(keysym))


def invert_string_to_keysym(keysym: int) -> typing.Optional[str]:
    """
    Surprisingly, XK.keysym_to_string does not invert XK.string_to_keysym:
    >>> XK.keysym_to_string(XK.XK_grave)
    '`'
    >>> XK.string_to_keysym("`")
    0
    >>> XK.string_to_keysym("grave")
    96
    >>> string_to_keysym_inverted(keysym=XK.XK_grave)
    'grave'
    """
    for string, ksym in vars(XK).items():
        if keysym == ksym:
            assert string.startswith("XK_")
            return string[3:]
    return None
