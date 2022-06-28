from src.Lista02_Classes.Exerc03.classFlight import Flight
from string import ascii_uppercase


class SpecialFlight(Flight):
    def __init__(self, number, date, row_smoking_seats):
        super().__init__(number, date)

        # Define Smoking Seats
        for col in ascii_uppercase[:6]:
            for seat in range(1, row_smoking_seats+1):
                self.seats_list[col][-seat] = 's'
        self.__row_smoking_seats = (row_smoking_seats * 6)

    # Getter and Setter __row_smoking_seats
    @property
    def row_smoking_seats(self):
        return self.__row_smoking_seats

    @row_smoking_seats.setter
    def row_smoking_seats(self, new_row_sts):
        self.__row_smoking_seats = new_row_sts

    def number_vacancies(self):
        vacant_seats = 0
        for col in ascii_uppercase[:6]:
            for seat in self.seats_list[col]:
                if (seat == '.') or (seat == 's'):
                    vacant_seats += 1

        print(f'\033[32mThere are {vacant_seats} seats available.\033[m')

    def number_smoking_seats(self):
        vacant_smo_seats = 0
        for col in ascii_uppercase[:6]:
            for seat in self.seats_list[col]:
                if seat == 's':
                    vacant_smo_seats += 1

        tot_smo_seats = self.row_smoking_seats
        print(f'\033There are {tot_smo_seats} smoking seats.')
        print(f'\033Of these, {vacant_smo_seats} are vacant.')
        
