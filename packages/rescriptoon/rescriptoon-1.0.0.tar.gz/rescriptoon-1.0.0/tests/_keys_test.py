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

import pytest

from Xlib import XK

# pylint: disable=protected-access
import rescriptoon._keys


def test_us_keycode():
    us_keycode = rescriptoon._keys.USKeyCode.w
    assert us_keycode.name == "w"
    assert us_keycode.value == 25


@pytest.mark.parametrize(
    ("keysym", "label"),
    [
        # pylint: disable=no-member; false positive
        (XK.XK_Control_L, "left ctrl"),
        (XK.XK_Control_R, "right ctrl"),
        (XK.XK_Delete, "delete"),
        (XK.XK_Down, "↓"),
        (XK.XK_Left, "→"),
        (XK.XK_Right, "←"),
        (XK.XK_Up, "↑"),
        (XK.XK_a, "a"),
        (XK.XK_grave, "`"),
        (XK.XK_s, "s"),
        (XK.XK_semicolon, ";"),
        (XK.XK_slash, "/"),
        (XK.XK_space, "␣"),
        (XK.XK_w, "w"),
    ],
)
def test_keysym_to_label(keysym, label):
    assert rescriptoon._keys.keysym_to_label(keysym) == label


@pytest.mark.parametrize(
    "keysym",
    [
        # pylint: disable=no-member
        XK.XK_w,
        XK.XK_grave,
        XK.XK_semicolon,
        XK.XK_plus,
    ],
)
def test_invert_string_to_keysym(keysym):
    string = rescriptoon._keys.invert_string_to_keysym(keysym)
    assert string
    assert XK.string_to_keysym(string) == keysym


@pytest.mark.parametrize("string", ["w", "grave", "semicolon", "plus"])
def test_invert_string_to_keysym_2(string):
    keysym = XK.string_to_keysym(string)
    assert keysym != XK.NoSymbol
    assert rescriptoon._keys.invert_string_to_keysym(keysym) == string
