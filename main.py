from AskUser.AskUser import AskUser
from BoardInfo.BoardInfoBuilder import BoardInfoBuilder
from BoardInfo.BoardInfo import BoardInfo
from Solver.ISolver import ISolver
from Solver.Solver import Solver
from Solver.SolverBuilder import SolverBuilder


def get_data_about_board() -> BoardInfo:
    ask_user = AskUser()
    board_info: BoardInfo = \
        BoardInfoBuilder() \
        .create() \
        .with_size(
            ask_user.about_size()
        ) \
        .with_columns(
            ask_user.about_columns_entry()
        ) \
        .with_rows(
            ask_user.about_rows_entry()
        ) \
        .build()
    return board_info


def fabric_simple_8_square_board() -> BoardInfo:
    return BoardInfoBuilder() \
        .create() \
        .with_size(8) \
        .with_columns([[1], [3], [4, 3], [8], [8], [4, 3], [3], [1]]) \
        .with_rows([[2], [4], [4], [6], [6], [8], [2], [4]]) \
        .build()
    # .with_columns([[1], [3], [5, 1], [8], [8], [5, 1], [3], [1]]) \


def run():
    #board_info = get_data_about_board()
    board_info = fabric_simple_8_square_board()
    solver: ISolver = \
        SolverBuilder \
        .create() \
        .with_board_info(board_info) \
        .build()
    solver.solve()


if __name__ == "__main__":
    run()
