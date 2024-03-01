TORPEDO_LIFE = 200


class Torpedo:
    """
    this class manage the torpedo, each torpedo has location,speed,direction
    and life units. in case of torpedo and asteroid intersection the torpedo
    will be destroyed and the asteroid will be smashed
    """

    def __init__(self, place_x, place_y, speed_x, speed_y, directions=0):
        self.__place_x = place_x
        self.__speed_x = speed_x
        self.__place_y = place_y
        self.__speed_y = speed_y
        self.__directions = directions
        self.__num_loop = 0
        self.__radios = 4

    def get_radios(self):
        """
        This method return the torpedo radios
        :return: the torpedo radios
        """
        return self.__radios

    def is_life_expired(self):
        """
        This method return a boolean value indicating if the torpedo life time
        had expired
        :return: True in case the torpedo life time has expired
                 False in case the torpedo is still alive
        """
        self.__num_loop = self.__num_loop + 1
        if self.__num_loop > TORPEDO_LIFE:
            return True
        return False

    def get_directions(self):
        """
        This method return the torpedo direction
        :return: the torpedo direction
        """
        return self.__directions

    def get_placed_x(self):
        """
        This method return the x coordinate of the torpedo location
        :return: the x coordinate of the torpedo location
        """
        return self.__place_x

    def get_placed_y(self):
        """
        This method return the y coordinate of the torpedo location
        :return: the y coordinate of the torpedo location
        """
        return self.__place_y

    def get_speed_x(self):
        """
        This method return the speed of the torpedo on the x axis
        :return: the speed of the torpedo on the x axis
        """
        return self.__speed_x

    def get_speed_y(self):
        """
        This method return the speed of the torpedo on the y axis
        :return: the speed of the torpedo on the y axis
        """
        return self.__speed_y

    def update_placed(self, value_x, value_y):
        """
        This method updates the torpedo location
        :param value_x: the x coordinate of the torpedo location
        :param value_y: the y coordinate of the torpedo location
        :return: None
        """
        self.__place_x = value_x
        self.__place_y = value_y
