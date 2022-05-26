from math import *


def root_calculator(a, b, c):
    delt = (b ** 2) - (4 * a * c)
    if delt < 0:  # Without real roots
        return {'root_1': 0, 'root_2': 0, 'status': 0}

    if delt == 0:  # Two real and equal roots
        root = (- b + sqrt(delt)) / (2 * a)
        return {'root_1': root, 'root_2': root, 'status': 1}

    if delt > 0:  # Two real and different roots
        root_1 = (- b + sqrt(delt)) / (2 * a)
        root_2 = (- b - sqrt(delt)) / (2 * a)
        return {'root_1': root_1, 'root_2': root_2, 'status': 2}
