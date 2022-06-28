from src.Lista01_EstruturasDeProgramacao.Exerc03_BinaryConverter import input_number
from src.Lista03_Heranca.Exerc01.classSpecialFlight import SpecialFlight
#from src.Lista02_Classes.Exerc01.AppStudent import apart


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
    pass
