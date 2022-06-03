from src.Lista01_EstruturasDeProgramacao.Exerc03_BinaryConverter import input_number
from src.Lista02_Classes.Exerc02.AppDate import apart
from classVectorManager import VectorManage


def remove(string):
    comma, spc = ',', ' '
    string = string.replace(spc, '')

    if string[0] == comma:
        string = string[1:]

    if string[-1] == comma:
        string = string[:-1]

    return string


def vector_input(msg, num=True):
    while True:
        vector = str(input(msg)).strip()
        try:
            if (vector[0] == '[') and (vector[-1] == ']'):
                vector = list(vector[1:-1])
                new_vct = [''.join(vector)]

                if len(vector) == 0:
                    return vector

                else:
                    new_vct[0] = remove(new_vct[0])

                    if ',' not in new_vct[0]:
                        if num:
                            if new_vct[0].isnumeric():
                                new_vct[0] = int(new_vct[0])
                        return new_vct

                    else:
                        new_vct = new_vct[0].split(',')
                        if num:
                            for c in range(len(new_vct)):
                                if new_vct[c].isnumeric():
                                    new_vct[c] = int(new_vct[c])
                        return new_vct
            else:
                print('\033[31mInvalid input, enter a list with only letters or integers!\033[m')
                continue
        except (ValueError, TypeError, IndexError):
            print('\033[31mAn error has occurred, please try again!\033[m')
            continue


def main():
    apart('Welcome to Vector Manager', 50)
    vctr = vector_input('Enter the vector (Ex: [x, y]): ')
    main_vector = VectorManage(vctr)
    while True:
        print('=' * 50)
        choice = input_number(
            "1 - To insert an element;\n"
            "2 - Access an element by index;\n"
            "3 - See the length of the vector;\n"
            "4 - Print the vector;\n"
            "5 - Exit.\n"
            "> ")

        if choice == 1:
            new_element = input_number('> Enter the new element: ', str)
            if new_element.isnumeric():
                new_element = int(new_element)
            main_vector.insert(new_element)

        if choice == 2:
            if main_vector.vector_size() == 0:
                print(f'\033[32mThe list is empty, please insert an element!\033[m')
            else:
                while True:
                    index = input_number('Enter the element index: ')
                    element = main_vector.get_element(index)
                    if element:
                        print(f'\033[32mThe element at index {index} is {element}.\033[m')
                        break
                    print(f'\033[31mIndex out of vector range, try again!\033[m')

        if choice == 3:
            lght = main_vector.vector_size()
            print(f'> \033[32m The vector has {lght} elements.\033[m')

        if choice == 4:
            print(f'> \033[32m{main_vector}\033[m')

        if choice == 5:
            apart('End of the Program, always come back!', 50)
            break

        if (choice < 1) or (choice > 5):
            print('\033[31mInvalid Value, Try Again!\033[m')


if __name__ == '__main__':
    main()
