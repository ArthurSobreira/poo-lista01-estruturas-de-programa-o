from string import ascii_uppercase
from classFlight import Flight


class FlightManager(Flight):
    def __init__(self, seats_list, number, data):
        super().__init__(number, data)
        self.seats_list()

    def vacant_seat(self):  # proximoLivre
        pass

    def check_occupancy(self):  # verifica
        pass

    def occupy_seat(self, seats_list, seat):  # ocupa
        column = seat[0]
        row = seat[1]
        seats_list[column][row] = 'o'

    def vacancy(self):  # vagas
        pass

    @staticmethod
    def seats_list():
        letters = list(ascii_uppercase[:6])
        seats = dict()
        for c in letters:
            seats[c] = list('x' * 16)
        return seats
