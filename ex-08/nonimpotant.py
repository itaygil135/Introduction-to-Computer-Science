class Car:
    def  __init__(self,speed,name):
        self.__speed = speed
        self.__name = name
        self.__next = None


    def create_next_car(self):
        self.__next(Car(66,"shuly"))

    def set_next_car(self,carnum):
        self.__next = carnum

    def __str__(self):
        if self.__next == None:
            return "(" + self.__name + "," + str(self.__speed) + ")"

        return "(" + self.__name + "," + str(self.__speed) + ")" + "next = " + self.__next.__name

class Garge:
    def __init__(self):
        self.__head = None

    def add_to_head(self,car):
        if self.__head == None:
            self.__head = car
        else:
            car.__next = self.__head
            self.__head = car

    def remove_from_head(self):
        if self.__head == None:
            return "no car"
        variable = self.__head
        self.__head = self.__head.__next
        return variable.__name


car1 = Car(50,"honda")
car1.create_next_car()
print("car1 = ", car1)
'''
car2 = Car(30,"touota")
car3 =Car(100, "audi")
car1.set_next_car(car2)
car2.set_next_car(car3)
print("car1 = ", car1)
print("car2 = ", car2)
print("car3 =", car3)

my_garage = Garge()
'''
