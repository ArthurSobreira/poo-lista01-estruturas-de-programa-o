from src.Lista01_EstruturasDeProgramacao.Exerc03_BinaryConverter import input_number
from src.Lista02_Classes.Exerc05.AppVector import remove, vector_input
from src.Lista02_Classes.Exerc02.AppDate import apart
from classOrderedVector import OrderedVector


def main():
    apart('Welcome to Ordered Vector Manager', 50)
    vctr = vector_input('Enter the vector (Ex: [x, y]): ', False)
    main_vector = OrderedVector(vctr)
    while True:
        print('=' * 50)
        choice = input_number(
            "1 - Print the vector;\n"
            "2 - Sort the vector Alphabetically;\n"
            "3 - Insert a element;\n"
            "4 - Merge two vectors;\n"
            "5 - Exit.\n"
            "> ")

        if choice == 1:
            print(f'> \033[32m{main_vector}\033[m')

        if choice == 2:
            print(f'> \033[32mOrdered Vector: {main_vector.order()}\033[m')

        if choice == 3:
            element = input_number('> Enter the new element: ', str)
            main_vector.insert_string(element)
            print(f'\033[32mThe element {element} has been inserted into the vector.\033[m')

        if choice == 4:
            merge_vector = OrderedVector(vector_input('> Enter the merge vector (Ex: [x, y]): ', False))
            new_vector = main_vector.merge(merge_vector)
            print(f'> \033[32mMerged Vector: {new_vector}\033[m')

        if choice == 5:
            apart('End of the Program, always come back!', 50)
            break

        if (choice < 1) or (choice > 5):
            print('\033[31mInvalid Value, Try Again!\033[m')


if __name__ == '__main__':
    main()
