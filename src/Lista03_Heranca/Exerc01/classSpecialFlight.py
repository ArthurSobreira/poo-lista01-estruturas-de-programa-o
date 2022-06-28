from src.Lista02_Classes.Exerc03.classFlight import Flight


class SpecialFlight(Flight):
    def __init__(self, number, date, smoking_seat):
        super().__init__(number, date)

        # Define Smoking Seats
        for col in self.seats_list:
            for seat in range(1, smoking_seat+1):
                self.seats_list[col].__setitem__(-seat, 's')
