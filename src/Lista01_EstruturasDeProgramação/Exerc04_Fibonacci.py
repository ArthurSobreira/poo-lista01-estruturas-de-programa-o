from Exerc03_BinaryConverter import *


def fibonacci(number):
    first_number = second_number = 1
    list_fibo = [first_number, second_number]
    while True:
        current_number = first_number + second_number
        list_fibo.append(current_number)
        first_number = second_number
        second_number = current_number
        if current_number > number:
            return list_fibo


def main():
    number = input_number('Enter the number to verify if it pertains to the Fibonacci sequence: ')
    list_fibo = fibonacci(number)
    if number in list_fibo:
        print(f'The {number} is in the Fibonacci Sequence.')
    else:
        print(f'The {number} is not in the Fibonacci Sequence.')


if __name__ == '__main__':
    main()

