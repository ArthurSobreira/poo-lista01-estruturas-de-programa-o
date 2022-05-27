from src.Lista02_Classes.Exerc02.classDate import Date


class Flight:
    def __init__(self, number, data):
        self.__number = number
        self.__data = Date(data['day'], data['month'], data['year'])

    # Getter and Setter __number
    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, new_number):
        self.__number = new_number

    # Getter __data
    @property
    def data(self):
        return self.__data
