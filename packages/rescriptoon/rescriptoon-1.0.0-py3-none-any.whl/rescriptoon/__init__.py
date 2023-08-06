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
import logging
import os
import select
import time
import typing

import Xlib.display
from Xlib import X

from rescriptoon._actions import ToggleOverlayAction
from rescriptoon._keys import keysym_to_label
from rescriptoon._mapping import get_keycode_action_mapping
from rescriptoon._ui import SystemTrayUnavailable, TrayIcon

_TOONTOWN_ENGINE_WINDOW_NAME = "Toontown Rewritten"


def _x_walk_children_windows(
    parent_window: "Xlib.display.Window",
) -> typing.Iterator["Xlib.display.Window"]:
    yield parent_window
    for child_window in parent_window.query_tree().children:
        for subchild_window in _x_walk_children_windows(child_window):
            yield subchild_window


def _x_wait_for_event(xdisplay, timeout_seconds):
    """ Wait up to `timeout_seconds` seconds for a xevent.
        Return True, if a xevent is available.
        Return False, if the timeout was reached. """
    rlist = select.select(
        [xdisplay.display.socket],  # rlist
        [],  # wlist
        [],  # xlist
        timeout_seconds,  # timeout [seconds]
    )[0]
    return len(rlist) > 0


class Overlay:
    def __init__(self, display: Xlib.display.Display, toggle_keycode: int):
        self._xdisplay = display
        self._toggle_keycode = toggle_keycode
        self._keycode_mappings = get_keycode_action_mapping()
        if self._toggle_keycode in self._keycode_mappings:
            logging.warning(
                "ignoring mapping for toggle key %d (%s)",
                toggle_keycode,
                self._toggle_key_label,
            )
        self._keycode_mappings[self._toggle_keycode] = ToggleOverlayAction()
        self._active_key_registry = {}
        self._enabled = False
        self._engine_windows = None
        try:
            self._tray_icon = TrayIcon(display=self._xdisplay)
        except SystemTrayUnavailable:
            self._tray_icon = None

    @property
    def xdisplay(self) -> Xlib.display.Display:
        return self._xdisplay

    @property
    def engine_windows(self) -> typing.List["Xlib.display.Window"]:
        return self._engine_windows

    @property
    def _engine_windows_open(self) -> bool:
        for window in self._engine_windows:
            try:
                window.get_wm_state()
            except Xlib.error.BadWindow:
                logging.info("engine window %x is no longer available", window.id)
                return False
        return True

    def run(self) -> None:
        self._engine_windows = self._find_engine_windows()
        logging.debug("engine window ids %r", [hex(w.id) for w in self._engine_windows])
        if not self._engine_windows:
            raise Exception("no toontown window found")
        self._grab_key(self._toggle_keycode)
        print("key bindings:")
        for keycode, action in self._keycode_mappings.items():
            keysym: int = self._xdisplay.keycode_to_keysym(keycode, index=0)
            print("{}: {}".format(keysym_to_label(keysym), action.description,))
        self.enable()
        while self._engine_windows_open:
            while self.xdisplay.pending_events():
                self._handle_xevent(self.xdisplay.next_event())
            self._check_active_key_registry()
            # keep timeout low for _check_active_key_registry()
            # to be called frequently
            _x_wait_for_event(self.xdisplay, timeout_seconds=0.05)
        self._disable()

    def _draw_tray_icon(self) -> None:
        if self._tray_icon:
            self._tray_icon.draw(self.enabled)

    def _handle_xevent(self, xevent: Xlib.protocol.rq.Event) -> None:
        if isinstance(
            xevent, (Xlib.protocol.event.KeyPress, Xlib.protocol.event.KeyRelease)
        ):
            self._handle_xkeyevent(xevent)
        elif self._tray_icon and xevent.type == Xlib.X.ConfigureNotify:
            self._draw_tray_icon()

    def _handle_xkeyevent(
        self,
        xkeyevent: typing.Union[
            Xlib.protocol.event.KeyPress, Xlib.protocol.event.KeyRelease
        ],
    ) -> None:
        self._update_active_key_registry(xkeyevent)
        keycode_in = xkeyevent.detail
        try:
            action = self._keycode_mappings[keycode_in]
        except KeyError:
            keysym_in = self.xdisplay.keycode_to_keysym(keycode_in, index=0,)
            logging.warning(
                "received key event of unmapped key %d (%s)",
                keycode_in,
                keysym_to_label(keysym_in),
            )
            return
        action.execute(self, xkeyevent)

    @property
    def _toggle_keysym(self) -> int:
        return self._xdisplay.keycode_to_keysym(self._toggle_keycode, index=0)

    @property
    def _toggle_key_label(self) -> str:
        return keysym_to_label(self._toggle_keysym)

    def enable(self) -> None:
        for keycode in self._keycode_mappings.keys():
            if keycode != self._toggle_keycode:
                self._grab_key(keycode)
        self._enabled = True
        self._draw_tray_icon()
        logging.info(
            "rescriptoon is now enabled. press %s to disable.", self._toggle_key_label,
        )

    def _disable(self) -> None:
        for keycode in self._keycode_mappings.keys():
            if keycode != self._toggle_keycode:
                self._ungrab_key(keycode)
        self._enabled = False
        self._draw_tray_icon()

    def disable(self) -> None:
        self._disable()
        logging.info(
            "rescriptoon is now disabled. press %s to enable.", self._toggle_key_label,
        )

    @property
    def enabled(self) -> bool:
        return self._enabled

    def toggle(self) -> None:
        if self.enabled:
            self.disable()
        else:
            self.enable()

    def _grab_key(self, keycode):
        for window in self._engine_windows:
            window.grab_key(
                keycode,
                X.AnyModifier,
                # owner_events
                # https://stackoverflow.com/questions/32122360/x11-will-xgrabpointer-prevent-other-apps-from-any-mouse-event
                # False,
                True,
                X.GrabModeAsync,
                X.GrabModeAsync,
            )

    def _ungrab_key(self, keycode):
        for window in self._engine_windows:
            window.ungrab_key(keycode, X.AnyModifier)

    def _find_engine_windows(self) -> typing.List["Xlib.display.Window"]:
        return sorted(
            filter(
                lambda w: w.get_wm_name() == _TOONTOWN_ENGINE_WINDOW_NAME,
                _x_walk_children_windows(self.xdisplay.screen().root),
            ),
            # relative x
            # window managers reparent
            key=lambda w: w.query_tree().parent.get_geometry().x,
            # workaround to get absolute position:
            # http://science.su/stuff/so/print_frame_geometry_of_all_windows.py
        )

    def _update_active_key_registry(self, xkeyevent):
        # see self._check_active_key_registry
        keycode = xkeyevent.detail
        if isinstance(xkeyevent, Xlib.protocol.event.KeyPress):
            self._active_key_registry[keycode] = xkeyevent
        elif keycode in self._active_key_registry:
            del self._active_key_registry[keycode]

    def _check_active_key_registry(self):
        """
        WORKAROUND
        For an unknown reason some key release events don't get queued
        when multiple keys are being released simultaneously.
        So we keep a hashmap of supposedly currently pressed keys
        and periodically compare it with xdispaly.query_keymap().

        ref: https://stackoverflow.com/q/18160792/5894777
        """
        # https://tronche.com/gui/x/xlib/input/XQueryKeymap.html
        keymap = self.xdisplay.query_keymap()
        missed_releases = []
        for keycode, press_event in self._active_key_registry.items():
            byte_index = keycode >> 3
            bit_index = keycode & ((1 << 3) - 1)
            if not keymap[byte_index] & (1 << bit_index):
                logging.debug("missed release event of key %d", keycode)
                missed_releases.append(
                    Xlib.protocol.event.KeyRelease(
                        window=press_event.window,
                        detail=press_event.detail,
                        state=press_event.state,
                        root_x=press_event.root_x,
                        root_y=press_event.root_y,
                        event_x=press_event.event_x,
                        event_y=press_event.event_y,
                        child=press_event.child,
                        root=press_event.root,
                        time=X.CurrentTime,
                        same_screen=press_event.same_screen,
                    )
                )
        for release_event in missed_releases:
            self._handle_xkeyevent(release_event)
