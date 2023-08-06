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

from rescriptoon._actions import LowThrowAction


@pytest.mark.parametrize(
    ("target_engine_index", "description"),
    [
        (None, "low throw @ all engines"),
        (0, "low throw @ engine #0"),
        (1, "low throw @ engine #1"),
    ],
)
def test_description(target_engine_index, description):
    action = LowThrowAction(target_engine_index=target_engine_index)
    assert action.description == description
