# pylint: disable=protected-access
from rescriptoon._actions import RewriteKeyEventAction
from rescriptoon._mapping import get_keycode_action_mapping
from Xlib import XK


def test_get_keycode_action_mapping():
    mapping = get_keycode_action_mapping()
    assert isinstance(mapping[25], RewriteKeyEventAction)
    # pylint: disable=no-member; false positive for XK.*
    assert mapping[25]._keysym == XK.XK_Up
