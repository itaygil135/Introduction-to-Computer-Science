import boggle_board_randomizer

START_PLAY_TEXT = "to start play press  'start'"
PLAYING_TEXT = "enjoy your game"
WON_PLAY_AGAIN_TEXT = "you won. to play again press 'again'"
LOOSE_PLAY_AGAIN_TEXT = "time over. to play again press 'again'"
GAME_TIME = 10

NEW_GAME=0
GAME_STARTED=1
GAME_ENDED=2


class Boggle:
    def __init__(self):
        self._board = boggle_board_randomizer.randomize_board()
        self._board = [ [" "]*len(self._board[0]) for _ in range(len(self._board))]
        self._state=NEW_GAME
        self._current_display=""
        self._is_starting_new_game = False  # indicate if a new game should start now
        self._is_playing = False # indicate a game was started
        self._game_state_ended = False
        self._commands_list=["start","clear","send","again","end time"]
        self._commands_state= [("start",True),
                               ("clear",False),
                               ("send",False),
                               ("again",False),
                               ("end time",False)]
        self._start_end_text = START_PLAY_TEXT
        self._time_remaining = GAME_TIME
        self._path=[]
        self._score = 0

    def get_should_reset_timer_display(self):
        return self._is_starting_new_game

    def get_should_reload_board(self):
        return self._is_starting_new_game

    def get_board(self):
        return self._board

    def get_commands_list(self):
        return self._commands_list

    def get_score(self):
        return self._score

    def get_game_time(self):
        return GAME_TIME

    def get_display(self):
        return self._current_display

    def get_board_button_state(self):
        # if the game is active, activate the board buttons as well
        return self._is_playing

    def get_commands_state(self):
        return self._commands_state

    def get_start_end_text(self):
        return self._start_end_text

    def type_in(self, coordinate):
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

    def _do_command(self, coordinate):
        if coordinate == "clear":
            self._do_clear()
        elif coordinate == "start":
            self._do_start()
        elif coordinate == "send":
            self._do_send()
        elif coordinate == "again":
            self._do_again()
        elif coordinate == "end time":
            self._do_end_time()

    def _do_start(self):
        self._is_starting_new_game = True # refresh the time and board for the new game
        self._is_playing = True # mark that game started
        self._start_end_text = PLAYING_TEXT
        self._time_remaining = GAME_TIME
        self._do_clear()
        self._score = 0
        self._board = boggle_board_randomizer.randomize_board()
        self._commands_state = [("start", False), ("clear", True),
                                ("send", True), ("again", False),
                                ("end time", False)]

    def _do_game_ended(self):
        self._commands_state = [("start", False), ("clear", False),
                                ("send", False), ("again", True),
                                ("end time", False)]
        self._is_playing = False
        self._game_state_ended = False
        self._commands_state = [("start",True), ("clear",False),
                                ("send",False), ("again",False),
                                ("end time",False)]


    def _do_again(self):
        pass


    def _do_send(self):
        pass

    def _do_clear(self):
        self._path=[]
        self._current_display = ""

    def _do_board_button_selected(self, coordinate):
        self._current_display += self._board[coordinate[0]][coordinate[1]]
        self._path.append(coordinate)

    def _do_end_time(self):
        self._time_remaining = 0
        self._game_state_ended = True
        self._start_end_text = LOOSE_PLAY_AGAIN_TEXT





