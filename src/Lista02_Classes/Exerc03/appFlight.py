from src.Lista01_EstruturasDeProgramacao.Exerc03_BinaryConverter import input_number
from src.Lista02_Classes.Exerc02.AppDate import apart
from string import ascii_uppercase
from classFlightManager import FlightManager


def seats_list(lett_list=False):
    letters = list(ascii_uppercase[:6])
    if lett_list:
        return letters

    seats = dict()
    for c in letters:
        seats[c] = list('.' * 16)
    return seats


def seat_input(msg):
    while True:
        try:
            seat = str(input(msg)).strip().upper()
        except (ValueError, TypeError):
            print('\033[31mInvalid seat value, Try Again\033[m')
            continue
        else:
            if (seat[0].isalpha()) and (seat[0] in seats_list(True)):
                if (int(seat[1:].isalnum())) and (int(seat[1:]) in range(0, 16)):
                    return seat
            print('\033[31mInvalid seat value, Try Again\033[m')
            continue


def flight_data_entry():
    num = input_number('Enter the flight number: ')
    day = input_number('Enter the flight date:\n'
                       '> Day ')
    month = input_number('> Month (number) ')
    year = input_number('> Year ')
    main_date = {'day': day, 'month': month, 'year': year}
    flight_data = FlightManager(num, main_date, seats_list())
    return flight_data


def main():
    apart('Welcome to the Flight Manager', 50)
    my_flight = flight_data_entry()
    print(my_flight)


if __name__ == '__main__':
    main()
