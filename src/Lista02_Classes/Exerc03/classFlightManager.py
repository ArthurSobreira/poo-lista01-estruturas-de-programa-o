from src.Lista02_Classes.Exerc02.AppDate import apart
from classFlight import Flight
import pandas as pd


class FlightManager(Flight):
    def __init__(self, number, date, seat_list):
        super().__init__(number, date)
        self.__seats_list = seat_list

    # Getter and Setter __seats_list
    @property
    def seats_list(self):
        return self.__seats_list

    @seats_list.setter
    def seats_list(self, new_list):
        self.__seats_list = new_list

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
