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

import argparse
import logging

import Xlib.display
from Xlib import XK, X

import rescriptoon
from rescriptoon._keys import USKeyCode, invert_string_to_keysym

_DEFAULT_TOGGLE_KEYCODE: int = USKeyCode.grave.value

_VERBOSITY_LEVELS = [logging.WARNING, logging.INFO, logging.DEBUG]


def main() -> None:
    display = Xlib.display.Display()
    argparser = argparse.ArgumentParser(
        description="Attach rescriptoon to running Toontown Rewritten engines.",
    )
    default_toggle_keysym = display.keycode_to_keysym(_DEFAULT_TOGGLE_KEYCODE, index=0)
    argparser.add_argument(
        "--toggle",
        "-t",
        metavar="KEYSYM_NAME",
        dest="toggle_keysym_name",
        default=invert_string_to_keysym(default_toggle_keysym),
        help="key to turn extended keyboard controls on / off."
        + " any keysym name may be used"
        + " (see XStringToKeysym & X11/keysymdef.h, "
        + " default: %(default)s)",
    )
    argparser.add_argument(
        "--verbose",
        "-v",
        action="count",
        dest="verbosity",
        default=0,
        help="repeat to further increase verbosity",
    )
    args = argparser.parse_args()
    logging.basicConfig(
        format="%(asctime)s %(levelname)s: %(message)s",
        datefmt="%H:%I:%S",
        level=_VERBOSITY_LEVELS[min(args.verbosity, len(_VERBOSITY_LEVELS) - 1)],
    )
    toggle_keysym = XK.string_to_keysym(args.toggle_keysym_name)
    if toggle_keysym == X.NoSymbol:
        raise ValueError(
            "controls toggle: unknown keysym name '{}'".format(args.toggle_keysym_name)
        )
    rescriptoon.Overlay(
        display=display, toggle_keycode=display.keysym_to_keycode(toggle_keysym)
    ).run()
