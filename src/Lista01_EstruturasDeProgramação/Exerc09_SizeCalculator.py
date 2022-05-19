from math import *


def size_calculator(d, a):
    dhor = d * cos(a)
    size = sqrt((d ** 2) - (dhor ** 2))
    return size
