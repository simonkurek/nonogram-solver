class AskUser:
    __size: int
    __columns: list
    __rows: list

    def about_size(self) -> int:
        self.__size = int(input("Enter the size of the board: "))
        return self.__size

    def about_columns_entry(self) -> list:
        self.__columns = self.__get_entries("columns")
        return self.__columns

    def about_rows_entry(self) -> list:
        self.__rows = self.__get_entries("rows")
        return self.__rows

    def __get_entries(self, forWhat) -> list:
        result_list = []
        for _ in range(self.__size):
            numbers_string = input(
                f"Enter numbers for {forWhat} (split by ','): ")
            numbers_str_list = numbers_string.split(",")
            numbers_int_list = [int(x) for x in numbers_str_list]
            result_list.append(numbers_int_list)
        return result_list
