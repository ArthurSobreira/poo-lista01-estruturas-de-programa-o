from src.Lista01_EstruturasDeProgramacao.Exerc03_BinaryConverter import input_number
from src.Lista02_Classes.Exerc02.AppDate import apart
from classVectorManager import VectorManage


def vector_input(msg):  # Não aceita uma lista com menos de 2 elementos.
    while True:
        vector = str(input(msg))
        try:
            if ((vector[0] == '[') and (vector[-1] == ']')) and ('.' not in vector):
                vector = list(vector[1:-1])
                if isinstance(vector, list):
                    new_vct = []
                    if len(vector) == 0:
                        return vector
                    else:
                        print(f'Ah é {vector} length: {len(vector)}')
                        if (',' not in vector) or (vector[-1] or vector[0] == ','):
                            new_vct.append(''.join(vector))
                            print(new_vct)
                        else:
                            pass
            else:
                print('\033[31mInvalid input, please enter letters or whole numbers only!\033[m')
                continue

        except (ValueError, TypeError, IndexError):
            print('\033[31mAn error has occurred, please try again!\033[m')
            continue

            # if (vector[0] == '[') and (vector[-1] == ']'):
            #     if vector.replace(' ', '') == '[]':
            #         return list()
            #     ind = vector.index(',')
            #     if vector[ind + 1] == ' ':
            #         vctr = list(vector[1:-1].split(', '))
            #         for c in range(len(vctr)):
            #             if vctr[c].isnumeric():
            #                 vctr[c] = int(vctr[c])
            #         return vctr
            #     else:
            #         print('\033[31mPlease, separate the elements with a space after the comma!\033[m')
            #         continue
            # else:
            #     print('\033[31mInvalid input, Try Again!\033[m')
            #     continue


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
