import pandas as pd
from string import ascii_uppercase
from classFlight import Flight


class FlightManager(Flight):
    def __init__(self, number, data, seat_list):
        super().__init__(number, data)
        self.__seats_list = seat_list

    @property
    def seats_list(self):
        return self.__seats_list

    @seats_list.setter
    def seats_list(self, new_list):
        self.__seats_list = new_list

    def vacant_seat(self):  # proximoLivre
        pass

    def check_occupancy(self):  # verifica
        pass

    def occupy_seat(self, seat):  # ocupa
        column, row = str(seat[0].upper()), int(seat[1:])
        self.seats_list[column][row] = 'X'
        return self.seats_list

    def vacancy(self):  # vagas
        pass

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
    my_obj.occupy_seat('c2')
    my_obj.occupy_seat('d7')
    my_obj.occupy_seat('f13')
    my_obj.occupy_seat('e10')
    my_obj.occupy_seat('a15')
    print(my_obj.seats_list)
    print(my_obj.seat_map())
