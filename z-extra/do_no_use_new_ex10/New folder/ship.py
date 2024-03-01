class Ship:
    def __init__(self, place_x, place_y, speed_x=0, speed_y=0, directions=0):
        self.__place_x = place_x
        self.__speed_x = speed_x
        self.__place_y = place_y
        self.__speed_y = speed_y
        self.__directions = directions
        self.__life = 3


    def reduce_life(self):
        self.__life = self.__life -1
        if self.__life == 0:
            return True
        else:
            return False


    def get_radious(self):
        return 1

    def get_directions(self):
        return self.__directions

    def update_directions(self, value):
        self.__directions += value
        return self.__directions

    def get_placed_x(self):
        return self.__place_x

    def update_placed(self, value_x, value_y):
        self.__place_x = value_x
        self.__place_y = value_y

    def get_placed_y(self):
        return self.__place_y

    def get_speed_y(self):
        return self.__speed_y

    def update_speed_y(self, value):
        self.__speed_y += value
        return self.__speed_y

    def get_speed_x(self):
        return self.__speed_x

    def update_speed_x(self, value):
        self.__speed_x += value
        return self.__speed_x


