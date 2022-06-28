from src.Lista01_EstruturasDeProgramacao.Exerc03_BinaryConverter import input_number
from src.Lista02_Classes.Exerc02.AppDate import apart
from src.Lista02_Classes.Exerc03.classFlight import Flight


def flight_data_entry():
    num = input_number('Enter the flight number: ')
    day = input_number('Enter the flight date:\n'
                       '> Day ')
    month = input_number('> Month (number) ')
    year = input_number('> Year ')
    main_date = {'day': day, 'month': month, 'year': year}
    flight_data = Flight(num, main_date)
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
            main_flight.occupy_seat()

        if choice == 3:
            main_flight.number_vacancies()

        if choice == 4:
            st = main_flight.seat_input('> Enter seat number (Ex: A2): ')
            main_flight.check_occupancy(st, prt=True)

        if choice == 5:
            main_flight.next_vacant_seat()

        if choice == 6:
            apart('End of the Program, always come back!', 50)
            break

        if (choice < 1) or (choice > 6):
            print('\033[31mInvalid Value, Try Again!\033[m')


if __name__ == '__main__':
    main()
