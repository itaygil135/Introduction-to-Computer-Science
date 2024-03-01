class Asteroid:
    def __init__(self,place_x,speed_x,place_y,speed_y,size):
        self.__place_x = place_x
        self.__speed_x = speed_x
        self.__place_y = place_y
        self.__speed_y = speed_y
        self.__size = size
        # new_spot = self.new_spot_ship()
        # self.__screen.draw_ship(new_spot[0],new_spot[1], self.my_ship.get_directions())
        '''def new_spot_ship(self,):
              self_x = self.__screen_min_x + ((self._x + self.my_ship.get_speed_x())%(self.__screen_max_x - self.__screen_min_x ))
              self_y = self.__screen_min_y + ((self._y + self.my_ship.get_speed_y())%(self.__screen_max_y - self.__screen_min_y))
              return (self_x,self_y)'''