# pylint: disable=protected-access
from rescriptoon._cli import _DEFAULT_TOGGLE_KEYCODE


def test__default_toggle_keycode():
    assert _DEFAULT_TOGGLE_KEYCODE == 49
