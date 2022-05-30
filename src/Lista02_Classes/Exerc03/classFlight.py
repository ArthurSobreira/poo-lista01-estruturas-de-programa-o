from src.Lista02_Classes.Exerc02.classDate import Date


class Flight:
    def __init__(self, number, date):
        self.__number = number
        self.__date = Date(date['day'], date['month'], date['year'])

    def __str__(self):
        return f'Fligth number was defined as: {self.number}\n' \
               f'Flight date was define as: {self.date}'

    # Getter and Setter __number
    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, new_number):
        self.__number = new_number

    # Getter __date
    @property
    def date(self):
        return self.__date
