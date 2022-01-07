from BoardInfo.BoardInfo import BoardInfo


class BoardInfoBuilder:
    __size: int
    __columns: list
    __rows: list

    @staticmethod
    def create():
        return BoardInfoBuilder()

    def with_size(self, size: int):
        self.__size = size
        return self

    def with_columns(self, columns: list):
        self.__columns = columns
        return self

    def with_rows(self, rows: list):
        self.__rows = rows
        return self

    def build(self):
        if self.__size is None:
            raise ValueError("Size is not set")
        if len(self.__columns) == 0:
            raise ValueError("Columns is not set")
        if len(self.__rows) == 0:
            raise ValueError("Rows is not set")
        return BoardInfo(self.__size, self.__columns, self.__rows)
