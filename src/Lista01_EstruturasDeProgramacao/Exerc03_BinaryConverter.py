def input_number(msg, type=int):
    while True:
        try:
            number = type(input(msg))
        except (ValueError, TypeError):
            print('\033[31mInvalid Value, Try Again!\033[m')
            continue
        else:
            return number


def main():
    number = input_number('Enter a number to see your binary conversion: ')
    print(f'The conversion of the number {number} to binary is: {bin(number)}.')


if __name__ == '__main__':
    main()
