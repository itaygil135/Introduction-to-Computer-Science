class Ship:
    def __init__(self,place_x, place_y,speed_x = 0,speed_y = 0,dircetions = 0):
        self.__place_x = place_x
        self.__speed_x = speed_x
        self.__place_y = place_y
        self.__speed_y = speed_y
        self.__directions = dircetions

    def get_directions(self):
        return self.__directions

    def set_direction(self, value):
        self.__directions += value
        return self.__directions

    def get_speed_y(self):
        return self.__speed_y

    def get_speed_x(self):
        return self.__speed_x




