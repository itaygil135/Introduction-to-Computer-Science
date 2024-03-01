class Ship:
    """
    this class manage the ship object, the ship has location,speed , direction
    and limited life units.the ship can shoot torpedoes.
     in case of intersection with an asteroid the ship life unit reduced
    """
    def __init__(self, place_x, place_y, speed_x=0, speed_y=0, directions=0):
        self.__place_x = place_x
        self.__speed_x = speed_x
        self.__place_y = place_y
        self.__speed_y = speed_y
        self.__directions = directions
        self.__life = 3
        self.__radios = 1

    def reduce_life(self):
        """
        This method reduce the life of the ship and return a True/False value
         indicating if the ship was totally smashed
        :return: True: in case the ship was totally smashed
                 False: in case the ship is still alive
        """
        self.__life = self.__life -1
        if self.__life == 0:
            return True
        else:
            return False

    def get_radios(self):
        """
        This method return the ship radios
        :return: the ship radios
        """
        return self.__radios

    def get_directions(self):
        """
        This method return the ship direction
        :return: the ship direction
        """
        return self.__directions

    def update_directions(self, value):
        """
        This method update the ship direction
        :param value: the new ship direction
        :return:
        """
        self.__directions += value
        return self.__directions

    def get_placed_x(self):
        """
        This method return the x coordinate of the ship location
        :return: the x coordinate of the ship location
        """
        return self.__place_x

    def get_placed_y(self):
        """
        This method return the y coordinate of the ship location
        :return: the y coordinate of the ship location
        """
        return self.__place_y

    def update_placed(self, value_x, value_y):
        """
        This method updates the ship location
        :param value_x: the x coordinate of the ship location
        :param value_y: the  y coordinate of the ship location
        :return: None
        """
        self.__place_x = value_x
        self.__place_y = value_y

    def get_speed_y(self):
        """
        This method return the speed of the ship on the y axis
        :return: the speed of the ship on the y axis
        """
        return self.__speed_y

    def update_speed_y(self, value):
        """
        This method update the speed of the ship in the y axis
        :param value: the number of the 'speed's units' to be added to the
                      ship speed on the y axis
        :return: the update speed of the ship on the y axis
        """
        self.__speed_y += value
        return self.__speed_y

    def get_speed_x(self):
        """
        This method return the speed of the ship on the x axis
        :return: the speed of the ship on the x axis
        """
        return self.__speed_x

    def update_speed_x(self, value):
        """
        This method update the speed of the ship in the x axis
        :param value: the number of the 'speed's units' to be added to the
                      ship speed on the x axis
        :return: the update speed of the ship on the y axis
        """
        self.__speed_x += value
        return self.__speed_x


