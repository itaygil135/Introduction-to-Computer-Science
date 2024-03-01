class CarDriver:
    def __init__(self, skill_level):
        self.__skill_level = skill_level

    def get_skill(self):
        return self.__skill_level


class Car:
    def __init__(self, speed):
        self.__speed = speed

    def set_driver(self, driver):
        self.__driver = driver

    def get_driving_speed(self):
        if self.__driver:
            return self.__driver.get_skill() * self.__speed
        return 1


some_car=Car(50)
some_driver=CarDriver(2.5)
some_car.set_driver((some_driver))
print(some_car.get_driving_speed())