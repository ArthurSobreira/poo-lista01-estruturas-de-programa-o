from string import ascii_uppercase


def seats_list(lett_list=False):
    letters = list(ascii_uppercase[:6])
    if lett_list:
        return letters

    seats = dict()
    for c in letters:
        seats[c] = list('.' * 16)
    return seats


def seat_input(msg):
    while True:
        try:
            seat = str(input(msg)).strip().upper()
        except (ValueError, TypeError):
            print('\033[31mInvalid seat value, Try Again\033[m')
            continue
        else:
            if (seat[0].isalpha()) and (seat[0] in seats_list(True)):
                if (int(seat[1:].isalnum())) and (int(seat[1:]) in range(0, 16)):
                    return seat
            print('\033[31mInvalid seat value, Try Again\033[m')
            continue

