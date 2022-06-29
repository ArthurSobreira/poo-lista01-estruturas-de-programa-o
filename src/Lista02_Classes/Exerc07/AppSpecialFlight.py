from src.Lista01_EstruturasDeProgramacao.Exerc03_BinaryConverter import input_number
from src.Lista03_Heranca.Exerc01.classSpecialFlight import SpecialFlight
from src.Lista02_Classes.Exerc01.AppStudent import apart


def flight_data_entry():
    num = input_number('Enter the flight number: ')
    day = input_number('Enter the flight date:\n'
                       '> Day ')
    month = input_number('> Month (number) ')
    year = input_number('> Year ')
    main_date = {'day': day, 'month': month, 'year': year}

    while True:
        num_rows_smo = input_number('> Number of rows for smokers(1 - 15): ')
        if num_rows_smo in range(1, 16):
            break
        print('\033[31mInvalid Value, enter only numbers between 1 and 15!\033[m')

    return SpecialFlight(num, main_date, num_rows_smo)


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
            "6 - Number of smoking seats;\n"
            "7 - Seat type (smoker or not);\n"
            "8 - Exit.\n"
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
            main_flight.number_smoking_seats()

        if choice == 7:
            main_flight.seat_type()

        if choice == 8:
            apart('End of the Program, always come back!', 50)
            break

        if (choice < 1) or (choice > 8):
            print('\033[31mInvalid Value, Try Again!\033[m')


if __name__ == '__main__':
    main()
