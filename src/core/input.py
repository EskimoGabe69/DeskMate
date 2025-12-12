from enum import IntEnum, auto


class InputState(IntEnum):
    NOTHING = 0
    PRESSED = auto()
    HELD = auto()
    RELEASED = auto()


class MouseButton(IntEnum):
    LEFT = 0
    RIGHT = 1
    MIDDLE = 2


InputBuffer = list[InputState]
