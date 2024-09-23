import win32api
import pydirectinput
import time

pydirectinput.PAUSE=0.01

class Keys:
    TAB = 9
    KEY_0 = 48
    KEY_1 = 49
    KEY_2 = 50
    KEY_3 = 51
    KEY_4 = 52
    KEY_5 = 53
    KEY_6 = 54
    KEY_7 = 55
    KEY_8 = 56
    KEY_9 = 57
    A = 65
    B = 66
    C = 67
    D = 68
    E = 69
    F = 70
    G = 71
    H = 72
    I = 73
    J = 74
    K = 75
    L = 76
    M = 77
    N = 78
    O = 79
    P = 80
    Q = 81
    R = 82
    S = 83
    T = 84
    U = 85
    V = 86
    W = 87
    X = 88
    Y = 89
    Z = 90
    F1 = 112
    F2 = 113
    F3 = 114
    F4 = 115
    F5 = 116
    F6 = 117
    F7 = 118
    F8 = 119
    F9 = 120
    F10 = 121
    F11 = 122
    F12 = 123
    LEFT_SHIFT = 160
    RIGHT_SHIFT = 161

_KEY_STATE = {}
def is_key_trigger(key: Keys):
    state = win32api.GetKeyState(key)
    old_state = _KEY_STATE.get(key, 0)
    # Pressed.
    if state < 0 and state != old_state:
        _KEY_STATE[key] = state# & 0x01
        return True
    return False


def send_key_trigger(key: Keys):
    pydirectinput.press('5')
    pydirectinput.press('a')
    pydirectinput.press('pagedown')
    for _ in range(53-16):
        pydirectinput.press('up')
    for _ in range(3):
        pydirectinput.press('right')

def send_key_release(key: Keys):
    pass