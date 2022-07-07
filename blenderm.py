# MACROPAD Hotkeys: Universal Numpad

from adafruit_hid.keycode import Keycode

app = {
    'name' : 'Blender M',
    'order': 3,
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x0A3B66, 'Rot  ', ['r']),
        (0x0A3B66, 'Move ', ['g']),
        (0x0A3B66, 'Scale', ['s']),
        # 2nd row ----------
        (0x004166, 'x    ', ['x']),
        (0x004166, 'y    ', ['y']),
        (0x004166, 'z    ', ['z']),
        # 3rd row ----------
        (0x663F00, '-    ', ['-']),
        (0x663F00, '     ', []),
        (0x663F00, '+    ', []),
        # 4th row ----------
        (0x004166, '10   ', ['10']),
        (0x004166, '45   ', ['45']),
        (0x004166, '90   ', ['90'])
    ]
}
