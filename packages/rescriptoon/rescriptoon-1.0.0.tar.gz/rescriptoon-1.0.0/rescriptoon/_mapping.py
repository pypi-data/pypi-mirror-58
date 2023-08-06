import typing

from Xlib import XK

from rescriptoon._actions import LowThrowAction, RewriteKeyEventAction, SelectGagAction
from rescriptoon._keys import USKeyCode

_DEFAULT_KEYCODE_ACTION_MAPPING = {
    # pylint: disable=no-member; false positive for XK.*
    USKeyCode.w: RewriteKeyEventAction(keysym=XK.XK_Up, target_engine_index=0),
    USKeyCode.a: RewriteKeyEventAction(keysym=XK.XK_Left, target_engine_index=0),
    USKeyCode.s: RewriteKeyEventAction(keysym=XK.XK_Down, target_engine_index=0),
    USKeyCode.d: RewriteKeyEventAction(keysym=XK.XK_Right, target_engine_index=0),
    USKeyCode.ctrl_left: RewriteKeyEventAction(
        keysym=XK.XK_Control_L, target_engine_index=0
    ),
    USKeyCode.v: LowThrowAction(target_engine_index=0),
    USKeyCode.o: RewriteKeyEventAction(keysym=XK.XK_Up, target_engine_index=1),
    USKeyCode.k: RewriteKeyEventAction(keysym=XK.XK_Left, target_engine_index=1),
    USKeyCode.l: RewriteKeyEventAction(keysym=XK.XK_Down, target_engine_index=1),
    USKeyCode.semicolon: RewriteKeyEventAction(
        keysym=XK.XK_Right, target_engine_index=1
    ),
    USKeyCode.slash: RewriteKeyEventAction(
        keysym=XK.XK_Control_L, target_engine_index=1
    ),
    USKeyCode.n: LowThrowAction(target_engine_index=1),
    USKeyCode.space: RewriteKeyEventAction(keysym=XK.XK_Control_L),
    # TODO replace gag_name with enum
    USKeyCode.e: SelectGagAction(
        gag_name="elephant trunk",
        target_engine_index=0,
        column_index=4,
        factor_y=-0.047,
    ),
    USKeyCode.i: SelectGagAction(
        gag_name="elephant trunk",
        target_engine_index=1,
        column_index=4,
        factor_y=-0.047,
    ),
    USKeyCode.f: SelectGagAction(
        gag_name="foghorn", target_engine_index=0, column_index=5, factor_y=-0.047
    ),
    USKeyCode.j: SelectGagAction(
        gag_name="foghorn", target_engine_index=1, column_index=5, factor_y=-0.047
    ),
}


def get_keycode_action_mapping() -> typing.Dict:
    return {
        us_keycode.value: action
        for us_keycode, action in _DEFAULT_KEYCODE_ACTION_MAPPING.items()
    }
