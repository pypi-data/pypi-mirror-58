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

from rescriptoon._actions import RewriteKeyEventAction


@pytest.mark.parametrize(
    ("keysym", "target_engine_index", "description"),
    [
        (None, None, "forward to all engines"),
        (None, 0, "forward to engine #0"),
        (None, 1, "forward to engine #1"),
        # pylint: disable=no-member; false positive
        (XK.XK_Up, None, "send ↑ to all engines"),
        (XK.XK_Delete, 0, "send delete to engine #0"),
        (XK.XK_Control_L, 1, "send left ctrl to engine #1"),
    ],
)
def test_description(keysym, target_engine_index, description):
    action = RewriteKeyEventAction(
        keysym=keysym, target_engine_index=target_engine_index
    )
    assert action.description == description
