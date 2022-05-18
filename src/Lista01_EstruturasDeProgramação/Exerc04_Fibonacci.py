from Exerc03_BinaryConverter import *


def fibonacci(number):
    first_number = second_number = 1
    fibo_list = [first_number, second_number]
    while True:
        current_number = first_number + second_number
        fibo_list.append(current_number)
        first_number = second_number
        second_number = current_number
        if current_number > number:
            return fibo_list


def main():
    number = input_number('Enter the number to verify if it pertains to the Fibonacci sequence: ')
    fibo = fibonacci(number)
    if number in fibo:
        print(f'The {number} is in the Fibonacci Sequence.')
    else:
        print(f'The {number} is not in the Fibonacci Sequence.')


if __name__ == '__main__':
    main()
