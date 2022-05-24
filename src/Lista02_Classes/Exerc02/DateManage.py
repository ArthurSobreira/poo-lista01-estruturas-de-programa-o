from src.Lista01_EstruturasDeProgramação.Exerc03_BinaryConverter import *
from classDateAttributes import DateAttributes


def apart(msg, size):
    print('=' * size)
    print(f'{msg:^{size}}')
    print('=' * size)


def date_input():
    apart('Welcome to Date Manager', 50)
    day = input_number('> Enter the Day: ')
    mon = input_number('> Enter the Month (Number): ')
    year = input_number('> Enter the Year: ')
    return DateAttributes(day, mon, year)

