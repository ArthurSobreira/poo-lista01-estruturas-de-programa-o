from src.Lista02_Classes.Exerc03.classFlight import Flight
from string import ascii_uppercase


class SpecialFlight(Flight):
    def __init__(self, number, date, smoking_seat):
        super().__init__(number, date)

        # Define Smoking Seats
        for col in ascii_uppercase[:6]:
            for seat in range(1, smoking_seat+1):
                self.seats_list[col].__setitem__(-seat, 's')

    def number_vacancies(self):
        smo_seats, norm_seats = 0, 0
        for col in ascii_uppercase[:6]:
            for seat in self.seats_list[col]:
                if seat == '.':
                    norm_seats += 1
                if seat == 's':
                    smo_seats += 1

        total_seats = smo_seats + norm_seats
        print(f'\033[32mThere are {total_seats} seats available.\033[m')
        print(f'\033[32m{norm_seats} normal seat(s) and {smo_seats} smoking seat(s).\033[m')
