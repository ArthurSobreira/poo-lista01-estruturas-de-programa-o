import pandas as pd
from string import ascii_uppercase
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
        if not self.check_occupancy(seat):
            self.seats_list[column][row] = 'X'
            return True
        return False

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
