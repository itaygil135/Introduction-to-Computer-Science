#################################################################
# FILE : ex10.py
# WRITER : ilana gelman , ilana315061945 , 315061945
# WRITER : itay kahana, itaygil135, 316385962
# EXERCISE : intro2cs2 ex10 2020
# DESCRIPTION: A simple program that represent asteroid game
# STUDENTS I DISCUSSED THE EXERCISE WITH:-
# WEB PAGES I USED:-
#################################################################

from screen import Screen
import sys
import random
from ship import Ship
from math import *
from asteroid import Asteroid
from torpedo import Torpedo


DEFAULT_ASTEROIDS_NUM = 5
SCORE_DICT = {1: 100, 2: 50, 3: 20}
START_AST_SPEED = [1, 2, 3, 4, -1, -2, -3, -4]


def _set_torpedo_speed(ship):
    """
    this function calculate the initial speed for the torpedo based on
    the speed of given ship
    :param ship: the ship to be used in order to calculate torpedo speed
    :return: the speed of the torpedo
    """
    speed_x = ship.get_speed_x() + 2 * cos(
        radians(ship.get_directions()))
    speed_y = ship.get_speed_y() + 2 * sin(
        radians(ship.get_directions()))
    return speed_x, speed_y


def _create_new_small_asteroids(cur_ast, torpedo):
    """
    this function creates new smaller asteroids after torpedo collide
    asteroid
    :param cur_ast:the collided asteroid
    :param torpedo: collided torpedo
    :return: two new asteroids
    """
    speed_x = (torpedo.get_speed_x() + cur_ast.get_speed_x()) / sqrt(
        ((cur_ast.get_speed_x()) ** 2) + (
                (cur_ast.get_speed_y()) ** 2))
    speed_y = (torpedo.get_speed_y() + cur_ast.get_speed_y()) / sqrt(
        ((cur_ast.get_speed_x()) ** 2) + (
                (cur_ast.get_speed_y()) ** 2))
    new_asteroid_1 = Asteroid(cur_ast.get_placed_x(),
                              cur_ast.get_placed_y(),
                              speed_x, speed_y,
                              cur_ast.get_ast_size())
    speed_x_2 = speed_x * (-1)
    speed_y_2 = speed_y * (-1)
    new_asteroid_2 = Asteroid(cur_ast.get_placed_x(),
                              cur_ast.get_placed_y(),
                              speed_x_2, speed_y_2,
                              cur_ast.get_ast_size())
    return new_asteroid_1, new_asteroid_2




class GameRunner:

    def __init__(self, asteroids_amount):
        """
        game runner constructor. for each game create screen,torpedo list,
        asteroid list and ship.
        :param asteroids_amount: number of asteroids for this game
        """
        self.__screen = Screen()
        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        self._torpedo_list = []
        self._x, self._y = self.__starting_coordinates()
        self.my_ship = Ship(self._x, self._y)
        self._astro_list = []  # active asteroids on the screen
        self._new_asteroid_list = []  # asteroid to be added after intersection
        self._removed_asteroid = []  # asteroid to  remove after intersection
        self._score = 0
        self.__create_asteroids(asteroids_amount)

    def __end_game(self, title, message):
        """
        this method display massage to the user and end the game
        :param title: the title of the massage
        :param message: the body of the massage
        :return:
        """
        self.__screen.show_message(title, message)
        self.__screen.end_game()
        sys.exit()

    def __create_asteroids(self, asteroids_amount):
        """
        this method creates the asteroids for this game.for each asteroid
        verify there is no intersection with the ship.
        in case of intersection the asteroid is located at new place
        :param asteroids_amount: number of asteroids to create
        :return: None
        """
        for rock in range(asteroids_amount):
            place_ast_x, place_ast_y = self.__starting_coordinates()
            cur_rock = Asteroid(place_ast_x, place_ast_y,
                                random.choice(START_AST_SPEED),
                                random.choice(START_AST_SPEED))

            while cur_rock.has_intersection(self.my_ship):
                place_ast_x, place_ast_y = self.__starting_coordinates()
                cur_rock.update_placed(place_ast_x, place_ast_y)

            self.__screen.register_asteroid(cur_rock, cur_rock.get_ast_size())
            self._astro_list.append(cur_rock)

    def __starting_coordinates(self):
        """
        this method calculate random values for starting coordinates x,y
        :return: the calculated coordinates
        """
        holder_x = random.randint(self.__screen_min_x, self.__screen_max_x)
        holder_y = random.randint(self.__screen_min_y, self.__screen_max_y)
        return holder_x, holder_y

    def __new_spot(self, obj):
        """
        this method calculates object's new spot based on object movement
        rules.
        :param obj: the object to calculate it new spot
        :return: the new location x,y
        """
        location_x = \
            self.__screen_min_x + \
            ((obj.get_placed_x() + obj.get_speed_x() - self.__screen_min_x)
             % (self.__screen_max_x - self.__screen_min_x))
        location_y =\
            self.__screen_min_y +\
            ((obj.get_placed_y() + obj.get_speed_y() - self.__screen_min_y)
             % (self.__screen_max_y - self.__screen_min_y))
        obj.update_placed(location_x, location_y)

    def __create_torpedo(self):
        """
        this method creates new torpedo
        :return: None
        """
        speed_t_x, speed_t_y = _set_torpedo_speed(self.my_ship)
        torpedo = Torpedo(self.my_ship.get_placed_x(),
                          self.my_ship.get_placed_y()
                          , speed_t_x, speed_t_y,
                          self.my_ship.get_directions())
        self.__screen.register_torpedo(torpedo)
        self._torpedo_list.append(torpedo)

    def _ship_smashed(self, cur_ast):
        """
        this method handle smash with ship:
        1.show massage on the screen
        2. remove asteroid
        3.update ship life
        :param cur_ast:  the asteroid that smashed with ship
        :return: True if no life left to the ship
                 False otherwise
        """
        self.__screen.show_message("Crashed!!!",
                                   "your ship has crashed with an asteroid")
        self.__screen.unregister_asteroid(cur_ast)
        self._astro_list.remove(cur_ast)
        self.__screen.remove_life()
        return self.my_ship.reduce_life()

    def asteroid_smashed(self, cur_ast, torpedo):
        """
        this method handle asteroid collisions, based on asteroid size,
        two smaller asteroids may be created.
        the smashed asteroid  and the torpedo will be destroyed
        this function will update the screen and will store the new/removed
        asteroids in a temporary list, to be removed from the game asteroids
        list later.
        :param cur_ast: the smashed asteroid
        :param torpedo: the smashed torpedo
        :return: None
        """
        if cur_ast.update_size():
            new_asteroid_1, new_asteroid_2 = _create_new_small_asteroids(
                cur_ast, torpedo)
            self.__screen.register_asteroid(new_asteroid_1,
                                            cur_ast.get_ast_size())
            self.__screen.register_asteroid(new_asteroid_2,
                                            cur_ast.get_ast_size())
            self._new_asteroid_list.append(new_asteroid_1)
            self._new_asteroid_list.append(new_asteroid_2)

        self._removed_asteroid.append(cur_ast)
        self.__screen.unregister_asteroid(cur_ast)
        self._torpedo_list.remove(torpedo)
        self.__screen.unregister_torpedo(torpedo)

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
        """
        this is main function of the game,draws all the objects on the screen
        handle collision between objects, handle torpedo life.
        exit in case of:
        1.all asteroids were smashed
        2.ship was smashed
        3.user select to end the game
        :return: None
        """
        if len(self._astro_list) == 0:
            self.__end_game("end of the game you won", "no asteroids left")

        if self.__screen.should_end():
            self.__end_game("end of the game", "you chose to quit")

        self.__remove_expired_torpedoes()
        self.__draw_ship()
        self.__handle_key_press()
        self.__draw_all_torpedoes()
        if self.__check_asteroid_collisions():
            self.__end_game("end of the game",
                            "you lost! you lost all your life")

        for torpedo in self._torpedo_list:
            self.__new_spot(torpedo)
        self.__new_spot(self.my_ship)

    def __check_asteroid_collisions(self):
        """
        this method check and handle collision between asteroid and ship
        and asteroid and torpedo.
        this function boolean value indicating if ship was totally smashed
        :return: True in case the ship was totally smashed and its life ended
                 False in case the ship is still alive
        """
        any_crash = False
        for cur_ast in self._astro_list:
            self.__screen.draw_asteroid(cur_ast, cur_ast.get_placed_x(),
                                        cur_ast.get_placed_y())
            if cur_ast.has_intersection(self.my_ship):
                if self._ship_smashed(cur_ast):
                    return True
                continue

            if self.__is_asteroid_crashed(cur_ast):
                any_crash = True
                continue
            self.__new_spot(cur_ast)

        if any_crash:
            self.__update_asteroids_list()
        return False

    def __update_asteroids_list(self):
        """
        this method update the asteroid list of the game, it removes the
        crashed asteroid and add the small asteroid that was created
        :return: None
        """
        self._astro_list = self._astro_list + self._new_asteroid_list
        self._new_asteroid_list = []
        for item in self._removed_asteroid:
            self._astro_list.remove(item)
        self._removed_asteroid = []

    def __is_asteroid_crashed(self, cur_ast):
        """
        this method handle collision between one asteroid and any torpedo
        :param cur_ast: asteroid to be checked
        :return: True if was intersection
                False otherwise
        """
        for torpedo in self._torpedo_list:
            if cur_ast.has_intersection(torpedo):
                self._score = self._score + SCORE_DICT[
                    cur_ast.get_ast_size()]
                self.__screen.set_score(self._score)
                self.asteroid_smashed(cur_ast, torpedo)
                return True
        return False

    def __draw_ship(self):
        """
        this method draws ship on the screen
        :return: None
        """
        self.__screen.draw_ship(self.my_ship.get_placed_x(),
                                self.my_ship.get_placed_y(),
                                self.my_ship.get_directions())

    def __draw_all_torpedoes(self):
        """
        this method draws all torpedoes on the screen
        :return: None
        """
        for torpedo in self._torpedo_list:
            self.__screen.draw_torpedo(torpedo, torpedo.get_placed_x(),
                                       torpedo.get_placed_y(),
                                       torpedo.get_directions())

    def __remove_expired_torpedoes(self):
        """
        this method removes all expired torpedoes
        :return: None
        """
        for torpedo in self._torpedo_list:
            if torpedo.is_life_expired():
                self._torpedo_list.remove(torpedo)
                self.__screen.unregister_torpedo(torpedo)

    def __handle_key_press(self):
        """
        this method handles user's key press
        :return: None
        """
        if self.__screen.is_right_pressed():
            self.my_ship.update_directions(-7)
        if self.__screen.is_left_pressed():
            self.my_ship.update_directions(7)
        if self.__screen.is_up_pressed():
            self.my_ship.update_speed_x(
                cos(radians(self.my_ship.get_directions())))
            self.my_ship.update_speed_y(
                sin(radians(self.my_ship.get_directions())))
        if self.__screen.is_space_pressed():
            if len(self._torpedo_list) < 10:
                self.__create_torpedo()


def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
