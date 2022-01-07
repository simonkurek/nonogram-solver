from abc import ABC, abstractmethod

from BoardInfo.BoardInfo import BoardInfo


class ISolver(ABC):

    @abstractmethod
    def solve(self, board_info: BoardInfo) -> list:
        pass
