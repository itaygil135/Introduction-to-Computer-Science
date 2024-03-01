import tkinter
#from functools import partial
from typing import Callable, Dict, List, Any

FRAME_WIDTH = 40
LABEL_WIDTH = 20
BOARD_BUTTON_WIDTH = 8
COMMAND_BUTTON_WIDTH = 10
FONT_SIZE = 20
BUTTON_HOVER_COLOR = "gray"
BUTTON_REGUALR_COLOR = "lightgray"
REGUALR_COLOR = "lightgray"
BUTTOM_ACTIVE_COLOR = "slateblue"
BUTTON_STYLE = { "font": ("Courier", FONT_SIZE),
                 "borderwidth":1,
                 "relief": tkinter.RAISED}

class GUI:
    _board_buttons: Dict[str, tkinter.Button] = {}  #dict of board's buttons
    _commands_buttons: Dict[str, tkinter.Button]={} #dict of commands' buttons

    def __init__(self, board, commands_list):
        self.remaining = 0
        self._main_window = tkinter.Tk()
        self._main_window.title("boggle")
        self._main_window.resizable(False,False)
        self._outer_frame = tkinter.Frame(self._main_window, bg=REGUALR_COLOR,
                                         highlightbackground="blue",
                                         highlightthickness=5)
        self._outer_frame.pack()

        self._word_label = tkinter.Label(self._outer_frame,
                                         font = ("Courier", FONT_SIZE),
                                         bg=REGUALR_COLOR,
                                         width=FRAME_WIDTH,
                                         relief='ridge')
        self._word_label.pack(side=tkinter.TOP, fill=tkinter.BOTH)

        #create internal frame that will contain the score
        self._score_frame = tkinter.Frame(self._outer_frame,
                                          width=FRAME_WIDTH,
                                          bg="lightblue",
                                          highlightbackground ="lightblue",
                                          highlightthickness=1)
        self._score_frame.pack(side=tkinter.TOP,
                               fill = tkinter.BOTH,
                               expand=True)

        # define the score label
        self._score_label = tkinter.Label(self._score_frame,
                                          font=("Courier", FONT_SIZE),
                                          bg=REGUALR_COLOR,
                                          width=LABEL_WIDTH,
                                          relief='ridge',
                                          text="score:")
        # 'load' the button to the screen (in the outer_frame)
        self._score_label.pack(side=tkinter.LEFT,
                               fill=tkinter.BOTH,
                               expand=True)

        self._score_label_value = tkinter.Label(self._score_frame,
                                                font=("Courier", FONT_SIZE),
                                                bg=REGUALR_COLOR,
                                                width=LABEL_WIDTH,
                                                relief='ridge',
                                                text="0" )
        # 'load' the button to the screen (in the outer_frame)
        self._score_label_value.pack(side=tkinter.RIGHT,
                                     fill=tkinter.BOTH,
                                     expand=True)

        # create an internal frame that will contain the time
        self._time_frame = tkinter.Frame(self._outer_frame,
                                         width=FRAME_WIDTH,
                                         bg="black",
                                         highlightbackground ="black",
                                         highlightthickness=1)
        self._time_frame.pack(side=tkinter.TOP,
                              fill = tkinter.BOTH,
                              expand=True)

        # define the clock text label
        self._clock_label = tkinter.Label(self._time_frame,
                                          font=("Courier", FONT_SIZE),
                                          bg=REGUALR_COLOR,
                                          width=LABEL_WIDTH,
                                          relief='ridge',
                                          text="time:")
        # 'load' the clock text label to the screen (in the outer_frame)
        self._clock_label.pack(side=tkinter.LEFT,
                               fill=tkinter.BOTH,
                               expand=True)
        # create the clock value button
        self._clock_label_value = tkinter.Label(self._time_frame,
                                                font=("Courier", FONT_SIZE),
                                                bg=REGUALR_COLOR,
                                                width=LABEL_WIDTH,
                                                relief='ridge',
                                                text="")
        # 'load' the clock value label to the screen (in the outer_frame)
        self._clock_label_value.pack(side=tkinter.RIGHT,
                                     fill=tkinter.BOTH,
                                     expand=True)

        # create an internal frame that will contain the board
        self._board_frame = tkinter.Frame(self._outer_frame,
                                          bg="red",
                                          highlightbackground ="red",
                                          highlightthickness=5)
        self._board_frame.pack(side=tkinter.TOP,
                               fill = tkinter.BOTH,
                               expand=True)

        # create the board buttons
        self._create_board_bottons_in_board_frame(board)

        #create an internal frame that will contain the commands
        self._commands_frame = tkinter.Frame(self._outer_frame,
                                             bg="yellow",
                                             highlightbackground ="yellow",
                                             highlightthickness=5)
        self._commands_frame.pack(side=tkinter.TOP,
                                  fill = tkinter.BOTH,
                                  expand=True)

        # create the board buttons
        self._create_bottons_in_command_frame(commands_list)
        self._commands_buttons["end time"].config(state=tkinter.DISABLED)
        self._commands_buttons["end time"].pack_forget()

        # create and load the "start/play-again" text label
        self._play_again_label = tkinter.Label(self._outer_frame,
                                         width=FRAME_WIDTH,
                                         **BUTTON_STYLE,
                                         bg=REGUALR_COLOR,
                                         fg="black",
                                         activebackground=REGUALR_COLOR,
                                         activeforeground=BUTTOM_ACTIVE_COLOR)
        self._play_again_label.pack(fill = tkinter.BOTH)


    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self._clock_label_value.configure(text="time's up!")
            self._commands_buttons["end time"].config(state=tkinter.NORMAL)
            self._commands_buttons["end time"].invoke()
            self._commands_buttons["end time"].config(state=tkinter.DISABLED)
        else:
            self._clock_label_value.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self._main_window.after(1000, self.countdown)

    def run(self):
        self._main_window.mainloop()

    def set_display(self, word_display_text, score):
        self._word_label["text"]=word_display_text
        self._score_label_value["text"] = str(score)

    def set_timer_display(self, should_reset_timer, game_time):
        if should_reset_timer:
            self.countdown(game_time)

    def relaod_board(self, should_reload_board, board):
        if should_reload_board:
            for row in range(len(board)):
                for col in range(len(board[0])):
                    self._board_buttons[(row,col)].configure(text=board[row][col])

    def update_board_buttons_state(self, enable_board_buttons):
        for button in self._board_buttons.values():
            if enable_board_buttons:
                button.config(state=tkinter.NORMAL)
            else:
                button.config(state=tkinter.DISABLED)

    def update_commands_buttoms_state(self, commands_state, start_end_text):
        # enable or disable commands' buttons and display the relevant text
        for cmd in commands_state:
            if cmd[1]:
                self._commands_buttons[cmd[0]].config(state=tkinter.NORMAL)
            else:
                self._commands_buttons[cmd[0]].config(state=tkinter.DISABLED)
        self._play_again_label.configure(text=start_end_text)


    def set_board_button_command(self, coordinate, action):
        self._board_buttons[coordinate].configure(command=action)

    def set_commands_buttons_command(self, command_text, action):
        self._commands_buttons[command_text].configure(command=action)

    def get_board_button_coordinates(self):
        return list(self._board_buttons.keys())

    def get_commands_buttons_text(self):
        return list(self._commands_buttons.keys())

    def _create_board_bottons_in_board_frame(self, board):
        #create the grid
        for i in range(len(board)):
            tkinter.Grid.columnconfigure(self._board_frame, i, weight=1)
        for i in range(len(board[0])):
            tkinter.Grid.rowconfigure(self._board_frame, i, weight=1)

        # First create 16 buttons for the board cubes, so the coordinate at
        # the board and at the grid will be the same
        for row in range(len(board)):
            for col in range(len(board[0])):
                self._make_button(board[row][col], row, col)

    def _make_button(self, button_text, row, col, rowspan:int=1,columnspan=1):
        button = tkinter.Button(self._board_frame,
                                text=button_text,
                                **BUTTON_STYLE,
                                width=BOARD_BUTTON_WIDTH,
                                bg=BUTTON_REGUALR_COLOR,
                                state=tkinter.DISABLED)

        button.grid(row=row,
                    column=col,
                    rowspan=rowspan,
                    columnspan=columnspan,
                    sticky=tkinter.NSEW)
        #create/update dictionary when the coordinate is the key,
        # and the button is the value
        self._board_buttons[(row,col)] = button

        def _on_enter(event:Any):
            button['background'] = BUTTON_HOVER_COLOR

        def _on_leave(event:Any):
            button['background'] = BUTTON_REGUALR_COLOR

        button.bind("<Enter>", _on_enter)
        button.bind("<Leave>", _on_leave)


    def _create_bottons_in_command_frame(self,command_list):
        for command_text in command_list:
            button = tkinter.Button(self._commands_frame,
                                    text=command_text,
                                    width=COMMAND_BUTTON_WIDTH,
                                    **BUTTON_STYLE)
            button.pack(side=tkinter.LEFT)
            self._commands_buttons[command_text] = button

if __name__ == "__main__":
    pass

