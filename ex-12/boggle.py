#################################################################
# FILE : ex12.py
# WRITER : ilana gelman , ilana315061945 , 315061945
# WRITER : itay kahana, itaygil135, 316385962
# EXERCISE : intro2cs2 ex20 2020
# DESCRIPTION: A  program that represent boggle game
# STUDENTS I DISCUSSED THE EXERCISE WITH:-
# WEB PAGES I USED:-
#################################################################
from logic import Logic
from gui import GUI


class BoggleController:
    def __init__(self):
        """
        this is the class that control the game and communicate
        between the logic and the GUI
        """
        self._logic = Logic()
        self._gui = GUI(self._logic.get_board(),
                        self._logic.get_commands_list())

        # create and set commands to the board's buttons
        for coordinate in self._gui.get_board_button_coordinates():
            action = self.create_button_action(coordinate)
            self._gui.set_board_button_command(coordinate, action)

        # create and set commands to the commands buttons (e.g start/again)
        for command_text in self._gui.get_commands_buttons_text():
            action = self.create_button_action(command_text)
            self._gui.set_commands_buttons_command(command_text, action)

        # update the gui with the initial data
        self._refresh_user_display()

    def _refresh_user_display(self):
        """
        getting the relevant information from the logic an than sending it to the GUI
        :return:None
        """
        # set  game's data :  score and guessed word
        self._gui.set_display(self._logic.get_display(),
                              self._logic.get_score())

        # update found words
        self._gui.set_found_words(self._logic.get_found_words())
        # update the board's buttons colors so they will be hide or displayed
        # based on the game state
        self._gui.set_board_buttons_state(self._logic.get_board_button_state())

        # update the commands button state and label
        self._gui.set_commands_buttons_state(self._logic.get_commands_state(),
                                             self._logic.get_start_end_text())

        # in case of new game - restart the timer
        self._gui.set_timer_display(self._logic.get_should_reset_timer(),
                                    self._logic.get_game_time())

        #  in case of new game - reload new or existing board
        self._gui.reload_board(self._logic.get_should_reload_board(),
                               self._logic.get_board())

    def create_button_action(self, coordinate):
        """
        this function creates a commands for the buttons
        :param coordinate:  a unique key in the dictionary
        :return: function which is a command  for this key
        """
        def fun():
            """
            this function send the button press to the logic and than after
            getting the essential information from the logic relocate it
            to the GUI which will refresh the display
            :return: None
            """
            # forward the button pressed to the boggle logic
            self._logic.type_in(coordinate)
            # update the GUI
            self._refresh_user_display()
        return fun

    def run(self):
        self._gui.run()


if __name__ == "__main__":
    BoggleController().run()
