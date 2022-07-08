# MACROPAD Hotkeys: Universal Numpad

from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
from consumer import Toolbar

app = {
    'name' : 'Media',
    'order': 2,
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, '', ['']),
        (0x000000, '' , ['']),
        (0x000000, '', ['']),
        # 2nd row ----------
        (0xFF0000, 'Bright-', [Toolbar(ConsumerControlCode.BRIGHTNESS_DECREMENT)]),
        (0x000000, '', ['']),
        (0x00FF00, 'Bright+', [Toolbar(ConsumerControlCode.BRIGHTNESS_INCREMENT)]),
        # 3rd row ----------
        (0xFF0000, 'Pref', [Toolbar(ConsumerControlCode.SCAN_PREVIOUS_TRACK)]),
        (0x0000FF, 'Play/Pause', [Toolbar(ConsumerControlCode.PLAY_PAUSE)]),
        (0x00FF00, 'Next', [Toolbar(ConsumerControlCode.SCAN_NEXT_TRACK)]),
        # 4th row ----------
        (0xFF0000, 'Vol-   ', [Toolbar(ConsumerControlCode.VOLUME_DECREMENT)]),
        (0x0000FF, 'Mute   ', [Toolbar(ConsumerControlCode.MUTE)]),
        (0x00FF00, 'Vol+   ', [Toolbar(ConsumerControlCode.VOLUME_INCREMENT)])
    ]
}
