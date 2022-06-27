from src.Lista02_Classes.Exerc02.classDate import Date
from string import ascii_uppercase
import pandas as pd


class Flight:
    def __init__(self, number, date):
        letters = list(ascii_uppercase[:6])
        seats = dict()
        for c in letters:
            seats[c] = list('.' * 16)

        self.seats_list = seats
        self.__number = number
        self.__date = Date(date['day'], date['month'], date['year'])

    def __str__(self):
        return f'The flight number was set to: {self.number}\n' \
               f'The flight date was set to: {self.date}'

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

    # Main Methods
    def next_vacant_seat(self, seat):
        column, row = str(seat[0]), int(seat[1:])
        closest_value = []
        for num, c in enumerate(self.seats_list[column]):
            if c == '.':
                if num < row:
                    diff = row - num
                    closest_value.append(diff)
                if num > row:
                    diff = num - row
                    closest_value.append(diff)

        if len(closest_value) == 0:  # There are no vacant seats
            return False

        closest_value = sorted(closest_value, key=int)
        lower = closest_value[0]
        closest_seat = row + lower
        if (closest_seat > 15) or (self.check_occupancy(f'{column}{closest_seat}')):
            closest_seat = row - lower
        return f'{column}{closest_seat}'

    def check_occupancy(self, seat):
        occupation = False
        column, row = str(seat[0]), int(seat[1:])
        if self.seats_list[column][row] == 'X':
            occupation = True
        return occupation

    def occupy_seat(self, seat):
        column, row = str(seat[0]), int(seat[1:])
        if not self.check_occupancy(seat):
            self.seats_list[column][row] = 'X'
            return True
        return False

    def number_vacancies(self):
        amount = 0
        df = self.seat_map()
        for c in self.seats_list:
            freq = df.groupby([c]).size()
            amount += freq.values[0]
        return amount

    def seat_map(self):
        return pd.DataFrame(self.seats_list)
