from Exerc03_BinaryConverter import *


def prime_number(number):
    primes_list = []
    for c in range(1, (number + 1)):
        div_list = []
        for i in range(1, (c + 1)):
            if c % i == 0:
                div_list.append(i)
        if len(div_list) == 2:
            primes_list.append(c)

    if number in primes_list:
        return True
    return False


def main():
    num = input_number('Enter a number to check if it is a Prime Number: ')
    if prime_number(num):
        print(f'{num} is a Prime Number.')
    else:
        print(f'{num} is not a Prime Number.')


if __name__ == '__main__':
    main()
