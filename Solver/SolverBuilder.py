from Board.BoardBuilder import BoardBuilder
from BoardInfo.BoardInfo import BoardInfo
from Board.Board import Board
from Solver.Solver import Solver
from Solver.Utils.EntriesEnumarate import EntriesEnumarate


class SolverBuilder:

    @staticmethod
    def create():
        return SolverBuilder()

    def __build_board(self, board_size: int) -> Board:
        return BoardBuilder() \
            .create() \
            .with_size(board_size) \
            .build()

    def with_board_info(self, board_info: BoardInfo):
        self.__board_info = board_info
        self.__board = self.__build_board(board_info.get_size())
        self.__entries_enumarate = EntriesEnumarate(board_info)
        return self

    def build(self):
        return Solver(self.__board_info, self.__board, self.__entries_enumarate)
