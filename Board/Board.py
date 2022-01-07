from Utils.BoardEnum import BoardEnum


class Board:
    def __init__(self, board):
        self.__board = board
        self.size = len(board)

    def get_board(self):
        return self.__board

    def __str__(self):
        result_str = ""
        for row in self.__board:
            for col in row:
                result_str += str(col)
            result_str += "\n"
        return result_str

    def fill_entry(self, type_of_entry: str, which_entry: int, with_values: list = []):
        if len(with_values) == 0:
            with_values = [BoardEnum.FILL] * self.size
        if type_of_entry == 'row':
            self.fill_row(which_entry, with_values)
        elif type_of_entry == 'col':
            self.fill_col(which_entry, with_values)
        else:
            raise Exception("Unknown type of entry")

    def fill_row(self, which_row: int, with_values: list = []):
        self.__board[which_row] = with_values

    def fill_col(self, which_col: int, with_values: list = []):
        for i, row in enumerate(self.__board):
            row[which_col] = with_values[i]
