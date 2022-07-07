# MACROPAD Hotkeys: Blender

from adafruit_hid.keycode import Keycode

app = {
    'name' : 'Websites',
    'order': 1,
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x0A3B66, 'SD', [Keycode.CONTROL, 't', 'slashdot.com\n']),
        (0x0A3B66, 'buiR', [Keycode.CONTROL, 't', 'buienradar.nl\n']),
        (0x0A3B66, 'trello', [Keycode.CONTROL, 't', 'trello.com\n']),
        # 2nd row ----------
        (0x0A3B66, 'nu', [Keycode.CONTROL, 't', 'www.nu.nl\n']),
        (0x0A3B66, 'GitH ', [Keycode.CONTROL, 't', 'github.com\n']),
        (0x0A3B66, 'BitB', [Keycode.CONTROL, 't', 'bitbucket.org\n']),
        # 3rd row ----------
        (0x0A3B66, 'sixdots', [Keycode.CONTROL, 't', 'six-dots.app\n']),
        (0x0A3B66, 'googD', [Keycode.CONTROL, 't', 'drive.google.com/drive/my-drive\n']),
        (0x0A3B66, 'gMail', [Keycode.CONTROL, 't', 'www.gmail.com\n']),
        # 4th row ----------
        (0x0A3B66, 'hackaD', [Keycode.CONTROL, 't', 'www.hackaday.com\n']),
        (0x0A3B66, 'tweakS', [Keycode.CONTROL, 't', 'www.tweakers.com\n']),
        (0x0A3B66, 'Close X', [Keycode.CONTROL, 'w'])
    ]
}
