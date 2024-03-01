import helper
import board
import car


class Game:
    """
    Add class description here
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        #You may assume board follows the API
        # implement your code here (and then delete the next line - 'pass')
        pass

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        # implement your code here (and then delete the next line - 'pass')
        pass

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        # implement your code here (and then delete the next line - 'pass')
        pass

if __name__== "__main__":
    #Your code here
    #All access to files, non API constructors, and such must be in this
    #section, or in functions called from this section.

    board_file_name = ""

    def get_board_file_name():
        return "board1.json"

    def read_json_board(board_file_name):
        board_config = helper.load_json(board_file_name)
        return board_config

    def valid_board_config(board_config):
        return True

    def create_cars_from_json_dict(board_config):
        cars_list =[]
        for json_dict_key in board_config:
            car_name = json_dict_key
            car_length = board_config[json_dict_key][0]
            car_location = board_config[json_dict_key][1]
            car_orientation = board_config[json_dict_key][2]
            temp_car = car.Car(car_name,car_length,car_location,car_orientation)
            cars_list.append(temp_car)
        return cars_list

    def add_cars_to_board(cars_list,game_board):
        for temp_car in cars_list:
            game_board.add_car(temp_car)

    while True:
        board_file_name = get_board_file_name()
        if not board_file_name:
            break

        board_config = read_json_board(board_file_name)

        if not valid_board_config(board_config):
            break

        cars_list = create_cars_from_json_dict(board_config)

        game_board = board.Board()
        print(game_board)

        add_cars_to_board(cars_list,game_board)
        print(game_board)

        break


