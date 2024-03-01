import tkinter
from typing import Dict

FRAME_WIDTH = 40
LABEL_WIDTH = 20
BOARD_BUTTON_WIDTH = 8
COMMAND_BUTTON_WIDTH = 14
FONT_SIZE = 20

BUTTON_HOVER_COLOR = "gray"
BUTTON_REGULAR_COLOR = "lightgray"
LABEL_REGULAR_COLOR = "lightblue"
REGULAR_COLOR = "lightgray"
FRAME_COLOR = "gray"
BUTTON_STYLE = {"font": ("Courier", FONT_SIZE),
                "borderwidth": 1,
                "bg": BUTTON_REGULAR_COLOR,
                "fg": "black",
                "activebackground": BUTTON_REGULAR_COLOR,
                "activeforeground": "blue",
                "relief": tkinter.RAISED}
LABEL_STYLE = {"font": ("Calibri", FONT_SIZE),
               "borderwidth": 1,
               "bg": LABEL_REGULAR_COLOR,
               "fg": "black",
               "relief": tkinter.RAISED}


class GUI:
    _board_buttons: Dict[str, tkinter.Button] = {}   # dict of board's buttons
    _commands_buttons: Dict[str, tkinter.Button] = {}  # dict of commands' buttons

    def __init__(self, board, commands_list):
        self.seconds_remained = 0
        self._main_window = tkinter.Tk()
        self._main_window.title("boggle")
        self._main_window.resizable(False, False)

        self._outer_frame = tkinter.Frame(self._main_window,
                                          highlightbackground="blue",
                                          highlightthickness=3)
        self._outer_frame.pack(side=tkinter.RIGHT)

        self._word_label = tkinter.Label(self._outer_frame,
                                         **LABEL_STYLE,
                                         width=FRAME_WIDTH)

        self._word_label.pack(side=tkinter.TOP, fill=tkinter.BOTH)

        # create internal frame that will contain the score
        self._score_frame = tkinter.Frame(self._outer_frame,
                                          width=FRAME_WIDTH,
                                          highlightbackground="lightblue",
                                          highlightthickness=1)
        self._score_frame.pack(side=tkinter.TOP,
                               fill=tkinter.BOTH,
                               expand=True)

        # define the score label
        self._score_label = tkinter.Label(self._score_frame,
                                          **LABEL_STYLE,
                                          width=LABEL_WIDTH,
                                          text="score:")
        # 'load' the button to the screen (in the outer_frame)
        self._score_label.pack(side=tkinter.LEFT,
                               fill=tkinter.BOTH,
                               expand=True)

        self._score_label_value = tkinter.Label(self._score_frame,
                                                **LABEL_STYLE,
                                                width=LABEL_WIDTH,
                                                text="0")
        # 'load' the button to the screen (in the outer_frame)
        self._score_label_value.pack(side=tkinter.RIGHT,
                                     fill=tkinter.BOTH,
                                     expand=True)

        # create an internal frame that will contain the time
        self._time_frame = tkinter.Frame(self._outer_frame,
                                         width=FRAME_WIDTH,
                                         highlightbackground="black",
                                         highlightthickness=1)
        self._time_frame.pack(side=tkinter.TOP,
                              fill=tkinter.BOTH,
                              expand=True)

        # define the clock text label
        self._clock_label = tkinter.Label(self._time_frame,
                                          **LABEL_STYLE,
                                          width=LABEL_WIDTH,
                                          text="time:")
        # 'load' the clock text label to the screen (in the outer_frame)
        self._clock_label.pack(side=tkinter.LEFT,
                               fill=tkinter.BOTH,
                               expand=True)
        # create the clock value button
        self._clock_label_value = tkinter.Label(self._time_frame,
                                                **LABEL_STYLE,
                                                width=LABEL_WIDTH,
                                                text="")
        # 'load' the clock value label to the screen (in the outer_frame)
        self._clock_label_value.pack(side=tkinter.RIGHT,
                                     fill=tkinter.BOTH,
                                     expand=True)

        # create an internal frame that will contain the board
        self._board_frame = tkinter.Frame(self._outer_frame,
                                          highlightbackground="gray",
                                          highlightthickness=1)
        self._board_frame.pack(side=tkinter.TOP,
                               fill=tkinter.BOTH,
                               expand=True)

        # create the board buttons
        self._create_board_buttons_in_board_frame(board)

        # create an internal frame that will contain the commands
        self._commands_frame = tkinter.Frame(self._outer_frame,
                                             highlightbackground="gray",
                                             highlightthickness=1)
        self._commands_frame.pack(side=tkinter.TOP,
                                  fill=tkinter.BOTH,
                                  expand=True)

        # create the board buttons
        self._create_buttons_in_command_frame(commands_list)
        # hide the button that will be used to call the logic when the time is over
        self._commands_buttons["end time"].config(state=tkinter.DISABLED)
        self._commands_buttons["end time"].pack_forget()

        # create and load the "start/play-again" text label
        self._play_again_label = tkinter.Label(self._outer_frame,
                                               width=FRAME_WIDTH,
                                               **LABEL_STYLE)
        self._play_again_label.pack(fill=tkinter.BOTH)

        self._words_frame = tkinter.Frame(self._main_window,
                                          highlightbackground=REGULAR_COLOR,
                                          highlightthickness=1)
        self._words_frame.pack(side=tkinter.LEFT)

        # load picture for butty
        photo = tkinter.PhotoImage(file="boggle.png")
        self._photo = photo.subsample(2)
        button2 = tkinter.Label(self._words_frame,
                                image=self._photo)
        button2.pack(side=tkinter.TOP)

        # Define a label for the found words list.
        found_words_label = tkinter.Label(self._words_frame,
                                          text="Found words",
                                          font=("Courier", FONT_SIZE))
        found_words_label.pack()
        # its another feature of GUI (like label for example)
        # which display multiple lines
        self._listbox = tkinter.Listbox(self._words_frame, height=9,
                                        width=15,
                                        bg="lightgrey",
                                        fg="black",
                                        activestyle='dotbox',
                                        font="Helvetica")
        self._listbox.pack(side=tkinter.LEFT)

        # when the placed id filled on the listbox its creates slider
        self._scrollbar = tkinter.Scrollbar(self._words_frame)
        self._scrollbar.pack(side=tkinter.RIGHT,
                             fill=tkinter.BOTH)
        self._listbox.config(yscrollcommand=self._scrollbar.set)
        self._scrollbar.config(command=self._listbox.yview)

    #  --------------    timer related functions   ------------------

    def set_timer_display(self, should_reset_timer, game_time):
        """
        this function restart the time of the game back to 3:00 min
        each time its get the indication for doing that
        :param should_reset_timer: boolean parameter
        :param game_time: the beginning time
        :return: None
        """
        if should_reset_timer:
            self.timer(game_time)

    def timer(self, remaining=None):
        """
        this function count and update ob display board the time (counting down)
        :param remaining: the time that remain in sec
        :return: None
        """
        if remaining is not None:
            self.seconds_remained = remaining

        if self.seconds_remained <= 0:
            self._clock_label_value.configure(text="time over!")
            self._commands_buttons["end time"].config(state=tkinter.NORMAL)
            self._commands_buttons["end time"].invoke()
            self._commands_buttons["end time"].config(state=tkinter.DISABLED)
        else:
            minutes = str(int(self.seconds_remained) // 60)
            seconds = str(int(self.seconds_remained) % 60)
            if len(seconds) == 1:
                seconds = "0" + seconds
            self._clock_label_value.configure(text=minutes+":"+seconds)
            self.seconds_remained = self.seconds_remained - 1
            self._main_window.after(1000, self.timer)

    #  --------------    user display related functions   ------------------

    def set_display(self, word_display_text, score):
        """
        this function update the display of the current score and the guessed word
        :param word_display_text:
        :param score: score
        :return: None
        """
        self._word_label["text"] = word_display_text
        self._score_label_value["text"] = str(score)

    def set_found_words(self, words):
        """
        this function clear and load again the list of founds words
        '-instead of remember each placed is been and which inx
         we remove every thing and add all each time-'
        :param words: the list of founds words
        :return: None
        """
        self._listbox.delete(0, tkinter.END)
        for i in range(len(words)):
            self._listbox.insert(i + 1, words[i])

    def reload_board(self, should_reload_board, board):
        """
        this function is called each time the user pressed 'start'
        and it update the GUI for a new game board
        :param should_reload_board: boolean parameter
        :param board: the new game board
        :return: None
        """
        if should_reload_board:
            for row in range(len(board)):
                for col in range(len(board[0])):
                    self._board_buttons[(row, col)].configure(text=
                                                              board[row][col])

    #  --------------    board buttons related functions   ------------------

    def _create_board_buttons_in_board_frame(self, board):
        """
        this function create a grid inside a frame and creates i
        inside the grid the buttons board
        :param board: the game board
        :return: None
        """
        # create the grid
        for i in range(len(board)):
            tkinter.Grid.columnconfigure(self._board_frame, i, weight=1)
        for i in range(len(board[0])):
            tkinter.Grid.rowconfigure(self._board_frame, i, weight=1)

        # First create 16 buttons for the board cubes, so the coordinate at
        # the board and at the grid will be the same
        for row in range(len(board)):
            for col in range(len(board[0])):
                self._make_button(board[row][col], row, col)

    def _make_button(self, button_text, row, col):
        """
        this function create a single button and locate it on the grid
        :param button_text: the text (empty string)
        :param row: row on the grid
        :param col: col on the grid
        :return: None
        """
        button = tkinter.Button(self._board_frame,
                                text=button_text,
                                **BUTTON_STYLE,
                                width=BOARD_BUTTON_WIDTH,
                                state=tkinter.DISABLED)

        button.grid(row=row,
                    column=col,
                    sticky=tkinter.NSEW)
        # update dictionary when the coordinate is the key,
        # and the button is the value
        self._board_buttons[(row, col)] = button

        def _on_enter(event):
            button['background'] = BUTTON_HOVER_COLOR

        def _on_leave(event):
            button['background'] = BUTTON_REGULAR_COLOR

        button.bind("<Enter>", _on_enter)
        button.bind("<Leave>", _on_leave)

    def set_board_button_command(self, coordinate, action):
        """
        this function set a command to each button on the board
        :param coordinate: the key of the button on the board
        :param action: command to be set
        :return: None
        """
        self._board_buttons[coordinate].configure(command=action)

    def set_board_buttons_state(self, enable_board_buttons):
        """
        this function gets each time the indication if the board buttons (the buttons of the letters)
        should be locked or not and do it
        :param enable_board_buttons: indication if the board buttons should be locked
        :return: None
        """
        for button in self._board_buttons.values():
            if enable_board_buttons:
                button.config(state=tkinter.NORMAL)
            else:
                button.config(state=tkinter.DISABLED)

    def get_board_button_coordinates(self):
        """
        returns the list of all the coordinates on the board
        :return: list of coordinates
        """
        return list(self._board_buttons.keys())

    #  --------------    commands buttons related functions   ------------------

    def _create_buttons_in_command_frame(self, command_list):
        """
        this function creates th buttons of the game command
        :param command_list: a list of the game command
        :return: None
        """
        for command_text in command_list:
            button = tkinter.Button(self._commands_frame,
                                    text=command_text,
                                    width=COMMAND_BUTTON_WIDTH,
                                    **BUTTON_STYLE)
            button.pack(side=tkinter.LEFT)
            self._commands_buttons[command_text] = button

    def set_commands_buttons_command(self, command_text, action):
        """
        this function set a command to each  command button
        :param command_text: the keys of the game command button
        :param action: the command to be set
        :return: None
        """
        self._commands_buttons[command_text].configure(command=action)

    def set_commands_buttons_state(self, commands_state, start_end_text):
        """
        this function lock/unlock the commands buttons, and display relevant message
        this function gets a list of tuples. each tuple has two values on the first
        is his command and on the second is the state which its supposed to be
        :param commands_state: list of tuples
        :param start_end_text: message to be display
        :return: None
        """
        # enable or disable commands' buttons and display the relevant text
        for cmd in commands_state:
            if cmd[1]:
                self._commands_buttons[cmd[0]].config(state=tkinter.NORMAL)
            else:
                self._commands_buttons[cmd[0]].config(state=tkinter.DISABLED)
        self._play_again_label.configure(text=start_end_text)

    def get_commands_buttons_text(self):
        """
        returns the list of all the keys on the game command button
        :return: list of keys
        """
        return list(self._commands_buttons.keys())

    def run(self):
        self._main_window.mainloop()


if __name__ == "__main__":
    pass
