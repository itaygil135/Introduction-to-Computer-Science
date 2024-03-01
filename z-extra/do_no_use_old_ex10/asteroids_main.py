from screen import Screen
import sys
import random
DEFAULT_ASTEROIDS_NUM = 5
import ship


class GameRunner:

    def __init__(self, asteroids_amount):
        self.__screen = Screen()
        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        self._x,self._y = self.starting_cordinates()
        self.my_ship = ship.Ship(self._x,self._y)
        self.__screen.draw_ship(self._x,self._y,self.my_ship.get_directions())

    def starting_cordinates(self):
        self._x = random.randint(self.__screen_min_x,self.__screen_max_x)
        self._y = random.randint(self.__screen_min_y,self.__screen_max_y)
        return (self._x, self._y)

    def new_spot_ship(self):
        x = self.__screen_min_x + ((self._x + self.my_ship.get_speed_x())%(self.__screen_max_x - self.__screen_min_x ))
        y = self.__screen_min_y + ((self._y + self.my_ship.get_speed_y())%(self.__screen_max_y - self.__screen_min_y))
        return self._x,self._y

    def run(self):
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        # You should not to change this method!
        self._game_loop()
        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def _game_loop(self):
        self.__screen.draw_ship(self._x, self._y, self.my_ship.get_directions())
        self_x,self_y = self.new_spot_ship()

        if self.__screen.is_right_pressed():
            self.my_ship.set_directions(-7)
        if self.__screen.is_left_pressed():
            self.my_ship.set_directions(7)



        #self.__screen.draw_ship(new_spot[0],new_spot[1], self.my_ship.get_directions())








def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
