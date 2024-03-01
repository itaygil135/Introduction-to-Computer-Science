from math import *
class Torpedo:

    def __init__(self, place_x , place_y, speed_x, speed_y, directions=0, num_loop = 0):
        self.__place_x = place_x
        self.__speed_x = speed_x
        self.__place_y = place_y
        self.__speed_y = speed_y
        self.__directions = directions
        self.__num_loop = num_loop

    def get_radious(self):
        return 4

    def get_num_loop(self):
        return self.__num_loop


    def get_directions(self):
        return self.__directions

    def get_placed_x(self):
        return self.__place_x

    def get_placed_y(self):
        return self.__place_y

    def get_speed_x(self):
        return self.__speed_x

    def get_speed_y(self):
        return self.__speed_y

    def update_placed(self, value_x, value_y):
        self.__place_x = value_x
        self.__place_y = value_y