from BoardInfo.BoardInfo import BoardInfo


class EntriesEnumarate:

    def __init__(self, board_info: BoardInfo):
        self.__columns = board_info.get_columns()
        self.__rows = board_info.get_rows()
        self.__entries_types = [self.__columns, self.__rows]
        self.__entries_types_names = ['col', 'row']

    def get_columns(self):
        return self.__columns

    def get_rows(self):
        return self.__rows

    def get_entries_types(self):
        return self.__entries_types

    def get_entries_types_names(self):
        return self.__entries_types_names
