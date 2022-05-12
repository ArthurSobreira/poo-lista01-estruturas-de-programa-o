def odd_between(val_a, val_b):
    list_odd = []
    if val_a < val_b:
        for c in range((val_a + 1), val_b):
            if c % 2 != 0:
                list_odd.append(c)
    if val_b < val_a:
        for c in range((val_b + 1), val_a):
            if c % 2 != 0:
                list_odd.append(c)
    return list_odd


def is_empty(list):
    if len(list) == 0:
        print('There are no odd numbers among the given values.')
    else:
        print('These are the odd numbers among the given values: ', end='')
        for c in list:
            print(f'{c}...', end='')
        print()


def select(msg):
    while True:
        try:
            val = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mInvalid Number, Try Again!!\033[m')
            continue
        else:
            return val


def main():
    val_a = select('Enter the value A: ')
    val_b = select('Enter the value B: ')
    is_empty(odd_between(val_a, val_b))


if __name__ == '__main__':
    main()
