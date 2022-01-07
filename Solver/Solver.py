from Board.Board import Board
from BoardInfo.BoardInfo import BoardInfo
from Solver.ISolver import ISolver
from Solver.Utils.EntriesEnumarate import EntriesEnumarate
from Utils.BoardEnum import BoardEnum


class Solver(ISolver):

    def __init__(self, board_info: BoardInfo, board: Board, ent_enum: EntriesEnumarate):
        self.__board_info = board_info
        self.__board = board
        self.__ent_enum = ent_enum

    def solve(self) -> list:
        print(self.__board_info)
        # fill obvious rows and columns
        self.__board = self.__fill_entries_if_size_equals(
            self.__board_info, self.__board)
        self.__board = self.__fill_entries_if_size_equals_sum(
            self.__board_info, self.__board)
        print(self.__board)

    def __fill_entries_if_size_equals(self, board_info: BoardInfo, board: Board) -> Board:
        for tidx, tentries in enumerate(self.__ent_enum.get_entries_types()):
            for i, entry in enumerate(tentries):
                if len(entry) == 1:
                    if entry[0] == board_info.get_size():
                        board.fill_entry(
                            self.__ent_enum.get_entries_types_names()[tidx], i)
        return board

    def __fill_entries_if_size_equals_sum(self, board_info: BoardInfo, board: Board) -> Board:
        for tidx, tentries in enumerate(self.__ent_enum.get_entries_types()):
            for i, entry in enumerate(tentries):
                entry_sum = sum(entry) + len(entry) - 1
                if entry_sum == board_info.get_size() and len(entry) != 1:
                    data = []
                    for value in entry:
                        for _ in range(value):
                            data.append(BoardEnum.FILL)
                        if value != entry[-1]:
                            data.append(BoardEnum.BLOCK)
                    board.fill_entry(
                        self.__ent_enum.get_entries_types_names()[tidx], i, data)
        return board
