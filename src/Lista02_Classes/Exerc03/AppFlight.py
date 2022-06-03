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
        seat = str(input(msg)).strip().upper()
        try:
            if (seat[0].isalpha()) and (seat[1:].isalnum()):
                if (str(seat[0]) in seats_list(True)) and (int(seat[1:]) in range(0, 16)):
                    return seat
            print('\033[31mInvalid seat value, Try Again!\033[m')
            continue
        except (ValueError, TypeError):
            print('\033[31mInvalid seat value, Try Again!\033[m')
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
    main_flight = flight_data_entry()
    print(main_flight)
    while True:
        print('=' * 50)
        choice = input_number(
            "1 - View seats map;\n"
            "2 - Take a seat;\n"
            "3 - Number of vacant seats;\n"
            "4 - Check if a seat is occupied;\n"
            "5 - Next vacant seat;\n"
            "6 - Exit.\n"
            "> ")
        if choice == 1:
            apart('Seat Map', 50)
            print(main_flight.seat_map())

        if choice == 2:
            st = seat_input('> Enter seat number (Ex: A2): ')
            if main_flight.occupy_seat(st):
                print(f'\033[32mSeat {st} has been occupied.\033[m')
            else:
                print(f'\033[32mIt is not possible to occupy the seat {st}.\033[m')

        if choice == 3:
            vac = main_flight.number_vacancies()
            print(f'\033[32mThere are {vac} seats available.\033[m')

        if choice == 4:
            st = seat_input('> Enter seat number (Ex: A2): ')
            if main_flight.check_occupancy(st):
                print(f'\033[32mSeat {st} is occupied.\033[m')
            else:
                print(f'\033[32mSeat {st} is empty.\033[m')

        if choice == 5:
            while True:
                st = seat_input('> Enter seat number (Ex: A2): ')
                if main_flight.check_occupancy(st):
                    print('\033[32mEnter a vacant seat.\033[m')
                else:
                    if main_flight.next_vacant_seat(st):
                        st_clos = main_flight.next_vacant_seat(st)
                        print(f'\033[32mThe closest vacant seat is {st_clos}.\033[m')
                    else:
                        print('\033[32mThere are no vacant seats in the column.\033[m')
                    break

        if choice == 6:
            apart('End of the Program, always come back!', 50)
            break

        if (choice < 1) or (choice > 6):
            print('\033[31mInvalid Value, Try Again!\033[m')
            print('=' * 50)


if __name__ == '__main__':
    main()
