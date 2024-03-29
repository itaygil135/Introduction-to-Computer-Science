class Board:
    """
    Add a class description here.
    Write briefly about the purpose of the class
    """
    __BOARD_SIZE = 7
    __VERTICAL = 0
    __HORIZONTAL = 1
    __EMPTY_CELL = "-"

    def __init__(self):
        # implement your code and erase the "pass"
        # Note that this function is required in your Board implementation.
        # However, is not part of the API for general board types.
        self.__board =  \
            [[self.__EMPTY_CELL] * self.__BOARD_SIZE] * self.__BOARD_SIZE


    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        #The game may assume this function returns a reasonable representation
        #of the board for printing, but may not assume details about it.
        board_str = "[\n"
        for row in range(self.__BOARD_SIZE):
            board_str += "["
            for col in range (self.__BOARD_SIZE):
                board_str += self.__board[row][col] + ","
            board_str += "]\n"
        board_str += "]\n"
        return board_str


    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        #In this board, returns a list containing the cells in the square
        #from (0,0) to (6,6) and the target cell (3,7)
        pass

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        #From the provided example car_config.json file, the return value could be
        #[('O','d',"some description"),('R','r',"some description"),('O','u',"some description")]
        pass

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        #In this board, returns (3,7)
        pass

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        # implement your code and erase the "pass"
        row, col = coordinate
        print (row,col)
        if self.__board[row][col] == self.__EMPTY_CELL:
            return True
        return False


    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        #Remember to consider all the reasons adding a car can fail.
        #You may assume the car is a legal car object following the API.
        # implement your code and erase the "pass"
        coordinates = car.car_coordinates()
        if not coordinates:
            return False
        print (coordinates)
        if coordinates[0] < 0 or coordinates[0] > self.__BOARD_SIZE \
            or coordinates[1] < 0 or coordinates[1] > self.__BOARD_SIZE:
            return False
        last_row = coordinates[0]
        last_col = coordinates[1]
        if car.get_orientation() == self.__VERTICAL:
            last_row += car.get_length() -1
        if car.get_orientation() == self.__HORIZONTAL:
            last_col += car.get_length() -1
        if last_row >= self.__BOARD_SIZE or last_col >= self.__BOARD_SIZE:
            return False
        if car.get_orientation() == self.__VERTICAL:
            for temp_row in range(coordinates[0],last_row+1):
                if self.cell_content((temp_row,coordinates[1])):
                    return False
        if car.get_orientation() == self.__HORIZONTAL:
            for temp_col in range(coordinates[1],last_col+1):
                if self.cell_content((coordinates[0],[temp_col])):
                    return False

        if car.get_orientation() == self.__VERTICAL:
            for temp_row in range(coordinates[0], last_row + 1):
                self.__board[temp_row][coordinates[1]] = car.get_name()

        if car.get_orientation() == self.__HORIZONTAL:
            for temp_col in range(coordinates[1], last_col + 1):
                self.__board[coordinates[0]][temp_col] = car.get_name()



    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        # implement your code and erase the "pass"
        pass
