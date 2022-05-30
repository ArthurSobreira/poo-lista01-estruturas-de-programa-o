from src.Lista01_EstruturasDeProgramacao.Exerc03_BinaryConverter import *
from src.Lista02_Classes.Exerc02.classDateAttributes import DateAttributes


def apart(msg, size):
    print('=' * size)
    print(f'{msg:^{size}}')
    print('=' * size)


def date_input():
    day = input_number('> Day: ')
    mon = input_number('> Month (Number): ')
    year = input_number('> Year: ')
    my_date = DateAttributes(day, mon, year)
    if my_date.__str__() == '01/01/0001':
        print(f'Invalid Date, it will be set to {my_date}.')
    else:
        print(f'Date defined as {my_date}.')
    return my_date


def main():
    apart('Welcome to Date Manager', 50)
    main_date = date_input()
    while True:
        print('=' * 50)
        choice = input_number(
            "1 - Compare dates;\n"
            "2 - Which the month;\n"
            "3 - Check if the year is a leap;\n"
            "4 - Clone the input date;\n"
            "5 - Exit.\n"
            "> ")

        if choice == 1:
            apart('Enter the Date to Compare it', 50)
            new_date = date_input()
            comp = main_date.compare(new_date)
            if comp == 0:
                print('\033[32mSame dates.\033[m')
            if comp == 1:
                print('\033[32mThe First date is greater.\033[m')
            else:
                print('\033[32mThe Second date is greater.\033[m')
            continue

        if choice == 2:
            mon_name = main_date.month_by_name()
            print(f"> The name of the month is {mon_name}.")
            continue

        if choice == 3:
            current_year = main_date.year
            if main_date.leap_year(current_year):
                print(f'> {current_year} is a leap year.')
            else:
                print(f'> {current_year} is not a leap year.')
            continue

        if choice == 4:
            date_clone = main_date.clone()
            print(f'Object {date_clone} has just been cloned. ')
            continue

        if choice == 5:
            apart('End of the Program, always come back!', 50)
            break

        else:
            print('\033[31mInvalid Value, Try Again!\033[m')


if __name__ == '__main__':
    main()
