class BoardInfo:
    __size: int
    __columns: list
    __rows: list

    def __init__(self, size: int, columns: list, rows: list):
        self.__size = size
        self.__columns = columns
        self.__rows = rows

    def get_size(self):
        return self.__size

    def get_columns(self):
        return self.__columns

    def get_rows(self):
        return self.__rows

    def __str__(self):
        return f"BoardInfo: size: {self.__size}, columns: {self.__columns}, rows: {self.__rows}"
