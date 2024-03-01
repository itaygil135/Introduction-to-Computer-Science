import boggle_board_randomizer
import ex12_utils

START_PLAY_TEXT = "to start play press  'start'"
PLAYING_TEXT = "enjoy your game  :-)"
LOOSE_PLAY_AGAIN_TEXT = "time over!  to play again press 'start'"
GAME_TIME = 180


class Logic:
    def __init__(self):
        # get board in order to get its size
        self._board = boggle_board_randomizer.randomize_board()
        # empty the board before starting the game
        self._board = [[" "]*len(self._board[0])
                       for _ in range(len(self._board))]
        self._words_dict = ex12_utils.load_words_dict("boggle_dict.txt")
        self._current_display = ""
        self._is_playing = False  # indicate a game was started and the user is playing
        self._is_starting_new_game = False  # indicate if a new game should start now
        self._game_state_ended = False
        self._commands_list = ["start", "clear", "send", "end time"]
        self._commands_state = [("start", True), ("clear", False),
                                ("send", False), ("end time", False)]
        self._start_end_text = START_PLAY_TEXT
        self._time_remaining = GAME_TIME
        self._path = []
        self._found_words = list()
        self._score = 0

    def get_display(self):
        """
        this function returns the the word that the user is now guessing
        :return: an  current guessed word
        """
        return self._current_display

    def get_score(self):
        """
        this function returns the current score
        :return: the score
        """
        return self._score

    def get_start_end_text(self):
        """
        :return:message on the board
        """
        return self._start_end_text

    def get_found_words(self):
        """
        the list of the words that the user already found on the board
        (after that it will arrive to the GUI and the GUI will display it on the screen)
        :return:
        """
        return self._found_words

    def get_should_reset_timer(self):
        """
        this function return the indication if we need to do a reset for the timer
        (only when a new game started)
        :return: the indication
        """
        return self._is_starting_new_game

    def get_game_time(self):
        """
        this function returns the beginning tome of a game
        :return: beginning time
        """
        return GAME_TIME

    def get_should_reload_board(self):
        """
        this function returns te indication if we need to switch the board (only when a new game started)
        :return: the indication
        """
        return self._is_starting_new_game

    def get_board(self):
        """
        :return the game board
        """
        return self._board

    def get_board_button_state(self):
        # if the game is active, activate the board buttons as well
        return self._is_playing

    def get_commands_list(self):
        """
        this function returns the list of the game commands,
         so the GUI will create buttons for them
        :return: list of commands
        """
        return self._commands_list

    def get_commands_state(self):
        """
        this function returns the info on each game command
        which will determinate if button is open or locked
        :return: list of tuples
        """
        return self._commands_state

    def type_in(self, coordinate):
        """
        this function handle the button press of the user
        :param coordinate: the key of the button pressed in a case that its a board button
        it's the coordinate in the board, in a case of command it will be a the command name
        :return:
        """
        # turn off the flag that is used just for restarting the clock and
        # reloading a new board for a new game
        self._is_starting_new_game = False
        # handle the pressed button
        if coordinate in self._commands_list:
            self._do_command(coordinate)
        else:
            self._do_board_button_selected(coordinate)
        # in case game ended - update the active commands buttons
        if self._game_state_ended:
            self._do_game_ended()

    def _do_board_button_selected(self, coordinate):
        """
        this function do handle the press of a key on the board
        (just when the key belongs to board_buttons)
        1 - update the user guessed word so far and the path of it
        :param coordinate: the key o button pressed which is the coordinate on the board
        :return: None
        """
        self._current_display += self._board[coordinate[0]][coordinate[1]]
        self._path.append(coordinate)

    def _do_command(self, coordinate):
        """
        thi function call the relevant function per command
        :param coordinate: the key of command
        :return: None
        """
        if coordinate == "clear":
            self._do_clear()
        elif coordinate == "start":
            self._do_start()
        elif coordinate == "send":
            self._do_send()
        elif coordinate == "end time":
            self._do_end_time()

    def _do_start(self):
        """
        this function initiate a new game
        :return: None
        """
        self._is_starting_new_game = True  # refresh the time and board for the new game
        self._is_playing = True  # mark that game started
        self._start_end_text = PLAYING_TEXT
        self._time_remaining = GAME_TIME
        self._found_words = list()
        self._do_clear()
        self._score = 0
        self._board = boggle_board_randomizer.randomize_board()
        self._commands_state = [("start", False), ("clear", True),
                                ("send", True), ("end time", False)]

    def _do_send(self):
        """
        this function handle press on send button:
        1- check if the word is in valid path
        2 - check if the word has not been found before
        3 - if its valid the function calculate the score of the user
            and add the word to the list of the founded words
        4 - in any case clear the guessed word on  the screen and the path
        :return: None
        """
        word = ex12_utils.is_valid_path(self._board,
                                        self._path,
                                        self._words_dict)
        if word is not None and word not in self._found_words:
            self._score += (len(word)**2)
            self._found_words.append(word)
        self._do_clear()

    def _do_clear(self):
        """
        clear the the path to an empty list
        and the guessed word  display to an empty string
        :return: None
        """
        self._path = []
        self._current_display = ""

    def _do_end_time(self):
        """
        this function is called by the method "invoke" which happening automatically
        when the tine the game is over
        :return: None
        """
        self._time_remaining = 0
        self._game_state_ended = True
        self._start_end_text = LOOSE_PLAY_AGAIN_TEXT

    def _do_game_ended(self):
        """
        this function do all the relevant actions when a game is over
        :return: None
        """
        self._is_playing = False
        self._game_state_ended = False
        self._commands_state = [("start", True), ("clear", False),
                                ("send", False), ("end time", False)]
