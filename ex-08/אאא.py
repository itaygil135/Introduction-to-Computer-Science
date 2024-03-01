
class Vehicles:
    __color = "white"

    def get_color(self):
        return self.__color


class Car(Vehicles):
    def __init__(self):
        self.__feul=88

    def set_fuel(self,new_feul):
        self.__feul=new_feul
        print("Set", self.__feul)

    def get_fuel(self):
        return self.__feul

    def get_diff(self, other):
        print(other.get_fuel())
        return other.get_fuel() - self.__feul

class Prius(Car):
    __size = 99



    def get_size(self):
        return self.__size

    def get_color(self):
        return "blu"



focus = Vehicles()
print("focus=",focus.get_color())

car1 = Car()
print(car1.get_color())


prius_1 = Prius()
print(prius_1.get_color())
