import math


class Asteroid:
    def __init__(self, place_x, place_y, speed_x, speed_y, size=3):
        self.__place_x = place_x
        self.__speed_x = speed_x
        self.__place_y = place_y
        self.__speed_y = speed_y
        self.__size = size

    def has_intersection(self, obj):
        distance = math.sqrt((((obj.get_placed_x()) - self.__place_x) ** 2) +
                             (((obj.get_placed_y()) - self.__place_y) ** 2))
        if distance <= (self.get_radious() + obj.get_radious()):
            return True
        return False

    def get_radious(self):
        return (self.__size * 10) - 5

    def update_placed(self, value_x, value_y):
        self.__place_x, self.__place_y = value_x, value_y

    def update_size(self):
        self.__size = self.__size -1
        if self.__size > 0:
            return True
        return False

    def get_ast_size(self):
        return self.__size

    def get_placed_x(self):
        return self.__place_x

    def get_placed_y(self):
        return self.__place_y

    def get_speed_y(self):
        return self.__speed_y

    def get_speed_x(self):
        return self.__speed_x
