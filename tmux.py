# MACROPAD Hotkeys: Tmux

from adafruit_hid.keycode import Keycode

app = {
    'name' : 'tmux',
    'order': 5,
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x663F00, 'newT', [Keycode.CONTROL, Keycode.ALT, 't']),
        (0x000000, '     ', []),
        (0x663F00, 'closeT', [Keycode.CONTROL, 'd']),
        # 2nd row ----------
        (0x004166, 'new', ['tmux new -s ']),
        (0x004166, 'list', ['tmux ls\n']),
        (0x004166, 'attach', ['tmux a -t ']),
        # 3rd row ----------
        (0x663F00, 'listw', [Keycode.CONTROL, 'b', 'w']),
        (0x663F00, 'createw ', [Keycode.CONTROL, 'b', 'c']),
        (0x663F00, 'killw', [Keycode.CONTROL, 'b', '&']),
        # 4th row ----------
        (0x004166, 'nextw ', [Keycode.CONTROL, 'b', 'n']),
        (0x004166, 'prefw', [Keycode.CONTROL, 'b', 'p']),
        (0x004166, 'detach', [Keycode.CONTROL, 'b', 'd']),

    ]
}
