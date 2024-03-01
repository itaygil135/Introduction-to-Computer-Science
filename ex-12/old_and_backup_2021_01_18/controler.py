from typing import Callable
from boggle import Boggle
from gui import GUI


class BoggleController:
    def __init__(self):
        self._boggle = Boggle()
        self._gui = GUI(self._boggle.get_board(),
                        self._boggle.get_commands_list())

        # set commands to the board's buttons
        for coordinate in self._gui.get_board_button_coordinates():
            action = self.create_button_action(coordinate)
            self._gui.set_board_button_command(coordinate, action)

        # set commands to the commands buttons (e.g start/again)
        for command_text in self._gui.get_commands_buttons_text():
            action = self.create_button_action(command_text)
            self._gui.set_commands_buttons_command(command_text, action)

        # update the gui with the initial data
        self._update_gui()


    def _update_gui(self):
        # set  game's data :  score and guessed word
        self._gui.set_display(self._boggle.get_display(),
                              self._boggle.get_score())

        # update the board's buttons colors so they will be hide or displayed
        # based on the game state
        self._gui.update_board_buttons_state(self._boggle.get_board_button_state())

        # update the commands button state and label
        self._gui.update_commands_buttoms_state(self._boggle.get_commands_state(),
                                                self._boggle.get_start_end_text())

        # in case of new game - restart the timer
        self._gui.set_timer_display(self._boggle.get_should_reset_timer_display(),
                                    self._boggle.get_game_time())

        #  in case of new game - reload new or existing board
        self._gui.relaod_board(self._boggle.get_should_reload_board(),
                               self._boggle.get_board())


    def create_button_action(self, coordinate):
        def fun():
            # forward the button pressed to the boggle logic
            self._boggle.type_in(coordinate)
            # update the GUI
            self._update_gui()
        return fun

    def run(self):
        self._gui.run()


if __name__ =="__main__":
    BoggleController().run()

'''




        #  create a variable named my_cube_action that holds a fucntion that will be called once the button is pressed
        #my_cube_action = self.create_cube_button_action()  # create the variable
        #self._gui.set_cube_button_command(my_cube_action)  # connect the variable to the button

        #
        #my_clock_action = self.create_clock_button_action()
        #self._gui.set_clock_button_command(my_clock_action)


    #  this is the fucntion that actually will be called once the button is pressed
    def my_action(self,text):
        print("here is my text  ", text)
        #self._boggle.type_in(button_text)
        #self._gui.set_display(self._boggle.get_display())

    #
    def create_cube_button_action(self):
        def fun(txt):
            #txt = self._gui.get_cube_button_text()
            self.my_action(txt)
            # self._boggle.type_in(button_text)
            #self._gui.set_display(self._boggle.get_display())
        return fun
        
        
        

    def create_clock_button_action(self):
        def fun(txt):
            self._boggle.clock_logic(txt)
        return fun
'''