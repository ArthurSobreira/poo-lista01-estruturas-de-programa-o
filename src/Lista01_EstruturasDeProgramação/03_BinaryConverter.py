def input_number(msg):
    while True:
        try:
            number = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mInvalid Number, Try Again!\033[m')
            continue
        else:
            return number

