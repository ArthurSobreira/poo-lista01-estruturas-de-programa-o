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
            "2 - Sort the list Alphabetically;\n"
            "3 - Insert a element;\n"
            "4 - Merge two vectors;\n"
            "5 - Exit.\n"
            "> ")

        if choice == 1:
            print(f'> \033[32m{main_vector}\033[m')

        if choice == 2:
            pass

        if choice == 3:
            pass

        if choice == 4:
            pass

        if choice == 5:
            apart('End of the Program, always come back!', 50)
            break


if __name__ == '__main__':
    main()
