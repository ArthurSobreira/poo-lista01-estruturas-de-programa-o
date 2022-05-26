from Exerc03_BinaryConverter import *
from math import *


def size_calculator(d, a):
    dhor = d * cos(a)
    size = sqrt((d ** 2) - (dhor ** 2))
    return size


def main():
    distance = input_number('Enter the Distance value: ')
    angle = input_number('Enter the Angle value: ')
    size = size_calculator(distance, angle)
    print(f'The object size is {size:.2f}')


if __name__ == '__main__':
    main()
