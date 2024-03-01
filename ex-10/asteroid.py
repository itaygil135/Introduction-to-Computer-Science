import math


class Asteroid:
    """
    this class manage asteroid object,each object has location,speed and size
    may collide with torpedo or ship
    """
    def __init__(self, place_x, place_y, speed_x, speed_y, size=3):
        self.__place_x = place_x
        self.__speed_x = speed_x
        self.__place_y = place_y
        self.__speed_y = speed_y
        self.__size = size

    def has_intersection(self, obj):
        """
        this method check if an asteroid has intersection with given object
        :param obj: the object to check intersection with
        :return: True if was intersection
                 False otherwise
        """
        distance = math.sqrt((((obj.get_placed_x()) - self.__place_x) ** 2) +
                             (((obj.get_placed_y()) - self.__place_y) ** 2))
        if distance <= (self.get_radios() + obj.get_radios()):
            return True
        return False

    def get_radios(self):
        """
        This method calculate and return the asteroid radios
        :return: the asteroid radios
        """
        return (self.__size * 10) - 5

    def update_placed(self, value_x, value_y):
        """
        This method updates the asteroid location
        :param value_x: the x coordinate of the asteroid location
        :param value_y: the y coordinate of the asteroid location
        :return: None
        """
        self.__place_x, self.__place_y = value_x, value_y

    def update_size(self):
        """
        This method update the size of the asteroid and return True/False
        value indicating if the asteroid still exist
        :return: True: in case the asteroid still exist
                 False: in case the asteroid does not exist any more
        """
        self.__size = self.__size -1
        if self.__size > 0:
            return True
        return False

    def get_ast_size(self):
        """
        This method return the size of asteroid
        :return: This method return the size of asteroid
        """
        return self.__size

    def get_placed_x(self):
        """
        This method return the x coordinate of the asteroid location
        :return: the x coordinate of the asteroid location
        """
        return self.__place_x

    def get_placed_y(self):
        """
        This method return the y coordinate of the asteroid location
        :return: the y coordinate of the asteroid location
        """
        return self.__place_y

    def get_speed_y(self):
        """
        This method return the speed of the asteroid on the y axis
        :return: the speed of the asteroid on the y axis
        """
        return self.__speed_y

    def get_speed_x(self):
        """
        This method return the speed of the asteroid on the x axis
        :return: the speed of the asteroid on the x axis
        """
        return self.__speed_x
