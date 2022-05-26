from classStudentNotes import StudentsNotes
from src.Lista01_EstruturasDeProgramação.Exerc03_BinaryConverter import *


def apart(msg, size):
    print('=' * size)
    print(f'{msg:^{size}}')
    print('=' * size)


def register():
    apart('Welcome to the Student Manage', 50)
    reg = input_number("Enter the student's matriculation number: ", int)
    name = input_number("Enter the student's name: ", str).strip().title()
    test_sco_1 = input_number('Enter the Test Score 1: ', float)
    test_sco_2 = input_number('Enter the test Score 2: ', float)
    work_sco = input_number('Enter the work score: ', float)
    return StudentsNotes(reg, name, test_sco_1, test_sco_2, work_sco)


def main():
    student = register()
    while True:
        print('=' * 50)
        choice = input_number(
                "1 - To view the student's average.\n"
                "2 - To view if the student is in recovery.\n"
                "3 - To register a new student.\n"
                "4 - To go out.\n"
                "> ")
        if choice == 1:
            note = student.average()
            print(f"> {student.name}'s average: {note:.2f}")
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
