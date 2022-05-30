import pandas as pd
from string import ascii_uppercase

import self

from classFlight import Flight


class FlightManager(Flight):
    def __init__(self, number, data, seat_list):
        super().__init__(number, data)
        self.__seats_list = seat_list

    # Getter and Setter __seats_list
    @property
    def seats_list(self):
        return self.__seats_list

    @seats_list.setter
    def seats_list(self, new_list):
        self.__seats_list = new_list

    # Main Methods
    def vacant_seat(self):  # proximoLivre
        pass

    def check_occupancy(self, seat):  # verifica
        occupation = False
        column, row = str(seat[0].upper()), int(seat[1:])
        if self.seats_list[column][row] == 'X':
            occupation = True
        return occupation

    def occupy_seat(self, seat):  # ocupa
        column, row = str(seat[0].upper()), int(seat[1:])
        self.seats_list[column][row] = 'X'
        return self.seats_list

    def number_vacancies(self):  # vagas
        amount = 0
        df = pd.DataFrame(self.seats_list)
        for c in self.seats_list:
            freq = df.groupby([c]).size()
            amount += freq.values[0]
        return amount

    def seat_map(self):
        return pd.DataFrame(self.seats_list)


if __name__ == '__main__':
    def seats_list():
        letters = list(ascii_uppercase[:6])
        seats = dict()
        for c in letters:
            seats[c] = list('.' * 16)
        return seats

    my_list = seats_list()
    my_obj = FlightManager(23123, {'day': 2, 'month': 4, 'year': 2076}, my_list)
    # my_obj.occupy_seat('c2')
    # my_obj.occupy_seat('d7')
    # my_obj.occupy_seat('f13')
    # my_obj.occupy_seat('e10')
    print(my_obj.number_vacancies())
    print(my_obj.seats_list)
    print(my_obj.seat_map())
