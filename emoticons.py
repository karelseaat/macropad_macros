# MACROPAD Hotkeys: Universal Numpad

from adafruit_hid.keycode import Keycode

app = {
    'name' : 'Emoticons',
    'order': 2,
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0xFF0000, 'smile', ['😀😃😄😁😆😅']),
        (0xFF0000, 'love ', ['😍🥰😘😗😙😚']),
        (0xFF0000, 'sad  ', ['😏😒😞😔😟😕']),
        # 2nd row ----------
        (0x00FF00, 'fun  ', ['😋😛😝😜🤪🤨']),
        (0x00FF00, 'mad  ', ['😤😠😡🤬🤯😳']),
        (0x00FF00, 'think', ['🤔🤭🤫🤥😵🤐']),
        # 3rd row ----------
        (0x0000FF, 'compu ', ['⌚️📱📲💻⌨️🖥']),
        (0x0000FF, 'compu2', ['🖨🖱🖲🕹🗜💽']),
        (0x0000FF, '$$$   ', ['💶🪙💰💳💎⚖️']),
        # 4th row ----------
        (0xFF00FF, 'knife', ['🔪🗡⚔️🛡🚬⚰️']),
        (0xFF00FF, 'ninja', ['🤌🥷🛒💸🏎🛵']),
        (0xFF00FF, 'food ', ['🥞🧇🥓🥩🍗🍖'])
    ]
}
