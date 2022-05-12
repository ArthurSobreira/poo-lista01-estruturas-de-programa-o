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


def main():
    val_a = int(input('Enter the value A: '))
    val_b = int(input('Enter the value B: '))
    print(odd_between(val_a, val_b))


if __name__ == '__main__':
    main()
