class Book:

    def __init__(self, name, publishing_year,number_of_copies=1):
        self.name = name
        self.publishing_year = publishing_year
        self.__copies = number_of_copies



    def get_number_of_copies(self):
        return self.__copies


    def add_copies(self, amount):
        self.__copies += amount


    def __str__(self):
        return self.name + " : " + str(self.publishing_year) + " : " + str(self.__copies) + " copies"