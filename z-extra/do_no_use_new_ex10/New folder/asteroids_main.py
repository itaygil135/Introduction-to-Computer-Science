from screen import Screen
import sys
import random
from ship import Ship
from math import *
from asteroid import Asteroid
from torpedo import Torpedo
from copy import  deepcopy
DEFAULT_ASTEROIDS_NUM = 5
SCORE_DICT = {1:100,2:50,3:20}
class GameRunner:

    def __init__(self, asteroids_amount):
        self.__screen = Screen()
        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        self._torpedo_list = []
        self._x, self._y = self._starting_cordinates()
        self.my_ship = Ship(self._x, self._y)
        self._astro_list = []
        self._start_ast_speed = [1, 2, 3, 4]
        self._new_astroid_list = []
        self._removed_astroid = [ ]
        self._count_loops = 0
        for rock in range(asteroids_amount):
            self.place_ast_x, self.place_ast_y = self._starting_cordinates()
            cur_rock = Asteroid(self.place_ast_x, self.place_ast_y,
                                random.choice(self._start_ast_speed),
                                random.choice(self._start_ast_speed))

            while cur_rock.has_intersection(self.my_ship):
                self.place_ast_x, self.place_ast_y = self._starting_cordinates()
                cur_rock.update_placed(self.place_ast_x, self.place_ast_y)

            self.__screen.register_asteroid(cur_rock, cur_rock.get_ast_size())
            self._astro_list.append(cur_rock)






    def _starting_cordinates(self):
        holder_x = random.randint(self.__screen_min_x, self.__screen_max_x)
        holder_y = random.randint(self.__screen_min_y, self.__screen_max_y)
        return holder_x, holder_y

    def _new_spot(self, obj):
        location_x = self.__screen_min_x + ((obj.get_placed_x() + obj.get_speed_x() - self.__screen_min_x) % (self.__screen_max_x - self.__screen_min_x))
        location_y = self.__screen_min_y + ((obj.get_placed_y() + obj.get_speed_y() - self.__screen_min_y) % (self.__screen_max_y - self.__screen_min_y))
        obj.update_placed(location_x, location_y)


    def set_tor_speed(self,obj):
        self.__speed_x = obj.get_speed_x() + 2*cos(radians(obj.get_directions()))
        self.__speed_y = obj.get_speed_y() + 2*sin(radians(obj.get_directions()))
        return self.__speed_x,self.__speed_y

    def create_torpedo(self):
        speed_t_x, speed_t_y = self.set_tor_speed(self.my_ship)
        torpedo = Torpedo(self.my_ship.get_placed_x(),self.my_ship.get_placed_y()
                          ,speed_t_x,speed_t_y,self.my_ship.get_directions(),self._count_loops)
        self.__screen.register_torpedo(torpedo)
        self._torpedo_list.append(torpedo)


    def _ship_smashed(self,cur_ast):
        self.__screen.show_message("Crashed!!!", "your ship has crashed with an asteroid")
        self.__screen.remove_life()
        self.__screen.unregister_asteroid(cur_ast)
        self._astro_list.remove(cur_ast)
        return self.my_ship.reduce_life()




    def asteroid_smashed(self,cur_ast,torpedo):
        if cur_ast.update_size():
            speed_x = (torpedo.get_speed_x() + cur_ast.get_speed_x())/ sqrt(((cur_ast.get_speed_x())**2)+((cur_ast.get_speed_y())**2))
            speed_y = (torpedo.get_speed_y() + cur_ast.get_speed_y())/ sqrt(((cur_ast.get_speed_x()) ** 2) + ((cur_ast.get_speed_y()) ** 2))
            self._new_asteroid_1 = Asteroid(cur_ast.get_placed_x(),cur_ast.get_placed_y(),
                                      speed_x,speed_y,cur_ast.get_ast_size())
            speed_x_2 = speed_x *(-1)
            speed_y_2 = speed_y *(-1)
            self._new_asteroid_2 = Asteroid(cur_ast.get_placed_x(), cur_ast.get_placed_y(),
                                      speed_x_2, speed_y_2, cur_ast.get_ast_size())
            self.__screen.register_asteroid(self._new_asteroid_1,cur_ast.get_ast_size())
            self.__screen.register_asteroid(self._new_asteroid_2, cur_ast.get_ast_size())
            self._new_astroid_list.append(self._new_asteroid_1)
            self._new_astroid_list.append(self._new_asteroid_2)

        self._removed_astroid.append(cur_ast)
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
        self._count_loops = self._count_loops + 1
        while self._count_loops > 200:
            for torpedo in self._torpedo_list:
                if torpedo.get_num_loop()  <= self._count_loops - 200:
                    self._torpedo_list.remove(torpedo)
                    self.__screen.unregister_torpedo(torpedo)





        self.__screen.draw_ship(self.my_ship.get_placed_x(), self.my_ship.get_placed_y(), self.my_ship.get_directions())
        self._handle_key_press()
        for torpedo in self._torpedo_list:
            self.__screen.draw_torpedo(torpedo, torpedo.get_placed_x(), torpedo.get_placed_y(),
                                       torpedo.get_directions())


        any_crash = False
        for cur_ast in self._astro_list:
            self.__screen.draw_asteroid(cur_ast, cur_ast.get_placed_x(), cur_ast.get_placed_y())
            if cur_ast.has_intersection(self.my_ship):
                if self._ship_smashed(cur_ast):
                    # end_game()
                    #sys.exit()
                    continue
            this_ast_crash = False
            for torpedo in self._torpedo_list:
                if cur_ast.has_intersection(torpedo):
                    self.__screen.set_score(SCORE_DICT[cur_ast.get_ast_size()])
                    self.asteroid_smashed(cur_ast,torpedo)
                    this_ast_crash = True
                    any_crash =  True
                    break

            if this_ast_crash:
                 continue
            self._new_spot(cur_ast)

        if any_crash:
            self._astro_list = self._astro_list + self._new_astroid_list
            self._new_astroid_list=[]
            for item in self._removed_astroid:
                self._astro_list.remove(item)
            self._removed_astroid = []


        for torpedo in self._torpedo_list:
            self._new_spot(torpedo)
        self._new_spot(self.my_ship)

    def _handle_key_press(self):
        if self.__screen.is_right_pressed():
            self.my_ship.update_directions(-7)
        if self.__screen.is_left_pressed():
            self.my_ship.update_directions(7)
        if self.__screen.is_up_pressed():
            self.my_ship.update_speed_x(cos(radians(self.my_ship.get_directions())))
            self.my_ship.update_speed_y(sin(radians(self.my_ship.get_directions())))
        if self.__screen.is_space_pressed():
            self.create_torpedo()



def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
