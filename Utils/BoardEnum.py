from enum import Enum


class BoardEnum(Enum):
    EMPTY = '⬜'
    FILL = '⬛'
    BLOCK = '❌'

    def __str__(self):
        return self.value
