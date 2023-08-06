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

import typing

import Xlib.display


def _get_system_tray(
    display: Xlib.display.Display,
) -> typing.Optional["Xlib.display.Window"]:
    tray: "Xlib.display.Window" = display.get_selection_owner(
        display.intern_atom("_NET_SYSTEM_TRAY_S{}".format(display.get_default_screen()))
    )
    if tray != Xlib.X.NONE:
        return tray
    return None


class SystemTrayUnavailable(Exception):
    pass


def _add_window_to_system_tray(
    display: Xlib.display.Display, window: "Xlib.display.Window"
) -> None:
    system_tray = _get_system_tray(display)
    if not system_tray:
        raise SystemTrayUnavailable()
    display.send_event(
        system_tray,
        Xlib.display.event.ClientMessage(
            client_type=display.intern_atom("_NET_SYSTEM_TRAY_OPCODE"),
            window=system_tray.id,
            data=(32, (Xlib.X.CurrentTime, 0, window.id, 0, 0,),),
        ),
    )


class TrayIcon:
    def __init__(self, display: "Xlib.display.Display"):
        self._display = display
        screen = display.screen()
        self._window = screen.root.create_window(
            # x, y
            -1,
            -1,
            # width, height
            1,
            1,
            # border width
            0,
            screen.root_depth,
            event_mask=Xlib.X.StructureNotifyMask,
        )
        self._window.set_wm_class("RescriptoonTrayIcon", "Rescriptoon")
        self._graphics_context = self._window.create_gc()
        colormap = screen.default_colormap
        self._color_enabled = colormap.alloc_named_color("green").pixel
        self._color_disabled = colormap.alloc_named_color("red").pixel
        _add_window_to_system_tray(display=display, window=self._window)

    def draw(self, enabled: bool) -> None:
        dim = self._window.get_geometry()
        self._graphics_context.change(
            foreground=self._color_enabled if enabled else self._color_disabled
        )
        self._window.fill_rectangle(self._graphics_context, 0, 0, dim.width, dim.height)
