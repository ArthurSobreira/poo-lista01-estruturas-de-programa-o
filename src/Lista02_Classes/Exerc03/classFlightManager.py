import pandas as pd
from classFlight import Flight
from src.Lista02_Classes.Exerc02.AppDate import apart


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
        df = pd.DataFrame(self.seats_list)
        for c in self.seats_list:
            freq = df.groupby([c]).size()
            amount += freq.values[0]
        return amount

    def seat_map(self):
        apart('Seat Map', 50)
        return pd.DataFrame(self.seats_list)

