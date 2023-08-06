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

from rescriptoon._actions import SelectGagAction


@pytest.mark.parametrize(
    ("column_index", "factor_y", "gag_name", "target_engine_index", "description"),
    [
        (
            4,
            -0.047,
            "elephant trunk",
            None,
            "select elephant trunk in battle @ all engines",
        ),
        (4, -0.047, "elephant trunk", 0, "select elephant trunk in battle @ engine #0"),
        (4, -0.047, "elephant trunk", 1, "select elephant trunk in battle @ engine #1"),
        (5, -0.047, "foghorn", 0, "select foghorn in battle @ engine #0"),
    ],
)
def test_description(
    column_index, factor_y, gag_name, target_engine_index, description
):
    action = SelectGagAction(
        column_index=column_index,
        factor_y=factor_y,
        gag_name=gag_name,
        target_engine_index=target_engine_index,
    )
    assert action.description == description
