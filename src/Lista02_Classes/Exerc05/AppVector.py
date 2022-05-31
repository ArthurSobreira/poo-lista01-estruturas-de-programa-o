from src.Lista01_EstruturasDeProgramacao.Exerc03_BinaryConverter import input_number
from src.Lista02_Classes.Exerc02.AppDate import apart
from classVectorManager import VectorManage


def vector_input(msg):
    while True:
        vector = str(input(msg)).strip()
        try:
            if (vector[0] == '[') and (vector[-1] == ']'):
                if '.' not in vector:
                    ind = vector.index(',')
                    if vector[ind + 1] == ' ':
                        vctr = list(vector[1:-1].split(', '))
                        for c in range(len(vctr)):
                            if vctr[c].isnumeric():
                                vctr[c] = int(vctr[c])
                        return vctr
                    else:
                        print('\033[31mPlease, separate the elements with a space after the comma!\033[m')
                        continue
                else:
                    print('\033[31mPlease, do not enter decimal numbers!\033[m')
                    continue
            else:
                print('\033[31mInvalid input, Try Again!\033[m')
                continue
        except (ValueError, TypeError, IndexError):
            print('\033[31mInvalid input, Try Again!\033[m')
            continue
