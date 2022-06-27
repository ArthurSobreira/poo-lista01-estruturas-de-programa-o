from classStudent import Student
from src.Lista01_EstruturasDeProgramacao.Exerc03_BinaryConverter import *


def apart(msg, size):
    print('=' * size)
    print(f'{msg:^{size}}')
    print('=' * size)


def register():
    apart('Welcome to the Student Manage', 50)
    reg = input_number("Enter the student's matriculation number: ", int)
    name = input_number("Enter the student's name: ", str).strip().title()
    grade_1 = input_number('Enter the exam grade 1: ', float)
    grade_2 = input_number('Enter the exam grade 2: ', float)
    work_grade = input_number('Enter the work grade: ', float)
    return Student(reg, name, grade_1, grade_2, work_grade)


def main():
    student = register()
    while True:
        print('=' * 50)
        choice = input_number(
                "1 - Student average;\n"
                "2 - Status of approbation;\n"
                "3 - Register a new student;\n"
                "4 - Exit.\n"
                "> ")
        if choice == 1:
            student.average()
            continue
        if choice == 2:
            student.final(student.average())
            continue
        if choice == 3:
            student = register()
            continue
        if choice == 4:
            apart('End of the Program, always come back!', 50)
            break
        else:
            print('\033[31mInvalid Value, Try Again!\033[m')


if __name__ == '__main__':
    main()
