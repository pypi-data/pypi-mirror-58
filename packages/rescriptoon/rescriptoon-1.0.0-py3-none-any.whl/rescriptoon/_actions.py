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

import abc
import logging
import random
import time
import typing

import Xlib.protocol.event
import Xlib.X
import Xlib.XK

from rescriptoon._keys import keysym_to_label

_XKEYEVENT_TYPE = typing.Union[
    Xlib.protocol.event.KeyPress, Xlib.protocol.event.KeyRelease
]


class _Action:
    @abc.abstractmethod
    def execute(self, overlay: "rescriptoon.Overlay", xkeyevent: _XKEYEVENT_TYPE):
        raise NotImplementedError()

    @abc.abstractproperty
    def description(self) -> str:
        raise NotImplementedError()


class EngineAction(_Action):
    def __init__(self, target_engine_index: typing.Optional[int] = None):
        self._target_engine_index = target_engine_index

    @abc.abstractmethod
    def execute_on_window(
        self,
        overlay: "rescriptoon.Overlay",
        xkeyevent: _XKEYEVENT_TYPE,
        engine_window: "Xlib.display.Window",
    ):
        raise NotImplementedError()

    def execute(
        self, overlay: "rescriptoon.Overlay", xkeyevent: _XKEYEVENT_TYPE,
    ):
        if self._target_engine_index is None:
            for target_window in overlay.engine_windows:
                self.execute_on_window(overlay, xkeyevent, target_window)
        elif self._target_engine_index >= len(overlay.engine_windows):
            logging.warning("target engine index out of bounds")
        else:
            self.execute_on_window(
                overlay, xkeyevent, overlay.engine_windows[self._target_engine_index]
            )

    @property
    def _engine_label(self) -> str:
        if self._target_engine_index is None:
            return "all engines"
        return "engine #{}".format(self._target_engine_index)


class CenterClickAction(EngineAction):
    def __init__(self, target_engine_index: int, factor_x: float, factor_y: float):
        super().__init__(target_engine_index=target_engine_index,)
        self._button = Xlib.X.Button1
        self._factor_x = factor_x
        self._factor_y = factor_y

    def execute_on_window(
        self,
        overlay: "rescriptoon.Overlay",
        xkeyevent: _XKEYEVENT_TYPE,
        engine_window: "Xlib.display.Window",
    ):
        engine_geometry = engine_window.get_geometry()
        smaller_dimension = min(engine_geometry.width, engine_geometry.height)
        attr = dict(
            window=engine_window,
            detail=self._button,
            state=xkeyevent.state,
            event_x=int(engine_geometry.width / 2 + smaller_dimension * self._factor_x),
            event_y=int(
                engine_geometry.height / 2 + smaller_dimension * self._factor_y
            ),
            # apparently root_x & root_y do not need to correspond with event_x/y.
            # attributes are still required to be set.
            root_x=0,  # xkeyevent.root_x,
            root_y=0,  # xkeyevent.root_y,
            child=xkeyevent.child,
            root=xkeyevent.root,
            time=xkeyevent.time,  # X.CurrentTime
            same_screen=xkeyevent.same_screen,
        )
        if isinstance(xkeyevent, Xlib.protocol.event.KeyPress):
            button_event = Xlib.protocol.event.ButtonPress(**attr)
        else:
            button_event = Xlib.protocol.event.ButtonRelease(**attr)
        engine_window.send_event(button_event)


class SelectGagAction(CenterClickAction):

    X_OFFSET = -0.286
    X_FACTOR = 0.081

    def __init__(
        self,
        target_engine_index: int,
        column_index: int,
        factor_y: float,
        gag_name: str,
    ):
        super().__init__(
            target_engine_index=target_engine_index,
            factor_x=self.X_OFFSET + self.X_FACTOR * column_index,
            factor_y=factor_y,
        )
        self._gag_name = gag_name

    @property
    def description(self) -> str:
        return "select {} in battle @ {}".format(self._gag_name, self._engine_label)


def _send_rewritten_xkeyevent(
    event_template: _XKEYEVENT_TYPE,
    window: "Xlib.display.Window",
    event_type: typing.Optional[typing.Type] = None,
    keycode=None,
) -> _XKEYEVENT_TYPE:
    if not event_type:
        event_type = type(event_template)
    window.send_event(
        event_type(
            window=window,
            detail=keycode if keycode else event_template.detail,
            state=event_template.state,
            root_x=event_template.root_x,
            root_y=event_template.root_y,
            event_x=event_template.event_x,
            event_y=event_template.event_y,
            child=event_template.child,
            root=event_template.root,
            time=event_template.time,  # X.CurrentTime
            same_screen=event_template.same_screen,
        )
    )


class RewriteKeyEventAction(EngineAction):
    def __init__(
        self,
        target_engine_index: typing.Optional[int] = None,
        keysym: typing.Optional[int] = None,
    ):
        super().__init__(target_engine_index=target_engine_index,)
        self._keysym = keysym

    def execute_on_window(
        self,
        overlay: "rescriptoon.Overlay",
        xkeyevent: _XKEYEVENT_TYPE,
        engine_window: "Xlib.display.Window",
    ):
        _send_rewritten_xkeyevent(
            event_template=xkeyevent,
            window=engine_window,
            keycode=overlay.xdisplay.keysym_to_keycode(self._keysym)
            if self._keysym is not None
            else xkeyevent.detail,
        )

    @property
    def description(self) -> str:
        if self._keysym is None:
            return "forward to {}".format(self._engine_label)
        return "send {} to {}".format(keysym_to_label(self._keysym), self._engine_label)


class LowThrowAction(EngineAction):

    _THROW_KEYSYM = Xlib.XK.XK_Delete  # pylint: no-member

    def execute_on_window(
        self,
        overlay: "rescriptoon.Overlay",
        xkeyevent: _XKEYEVENT_TYPE,
        engine_window: "Xlib.display.Window",
    ):
        if isinstance(xkeyevent, Xlib.protocol.event.KeyRelease):
            return
        keycode = overlay.xdisplay.keysym_to_keycode(self._THROW_KEYSYM)
        _send_rewritten_xkeyevent(
            event_template=xkeyevent,
            window=engine_window,
            keycode=keycode,
            event_type=Xlib.protocol.event.KeyPress,
        )
        time.sleep(random.uniform(0.04, 0.08))
        _send_rewritten_xkeyevent(
            event_template=xkeyevent,
            window=engine_window,
            keycode=keycode,
            event_type=Xlib.protocol.event.KeyRelease,
        )

    @property
    def description(self) -> str:
        return "low throw @ {}".format(self._engine_label)


class ToggleOverlayAction(_Action):
    def execute(self, overlay: "rescriptoon.Overlay", xkeyevent: _XKEYEVENT_TYPE):
        if isinstance(xkeyevent, Xlib.protocol.event.KeyPress):
            overlay.toggle()

    @property
    def description(self) -> str:
        return "enable/disable rescriptoon"
