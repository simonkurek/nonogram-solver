from Board.Board import Board


class BoardBuilder:

    @staticmethod
    def create():
        return BoardBuilder()

    def with_size(self, size):
        self.size = size
        return self

    def build(self):
        board = []
        for i in range(self.size):
            board.append([])
            for _ in range(self.size):
                board[i].append('o')
        return Board(board)
