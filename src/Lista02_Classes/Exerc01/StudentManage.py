from StudentNotes import StudentsNotes
from src.Lista01_EstruturasDeProgramação.Exerc03_BinaryConverter import *


class StudentManage:
    @staticmethod
    def apart(msg, size):
        print('=' * size)
        print(f'{msg:^{size}}')
        print('=' * size)

    @classmethod
    def register(cls):
        cls.apart('Wellcome to the Student Manage', 50)
        reg = input_number("Enter the student's matriculation number: ", int)
        name = input_number("Enter the student's name: ", str).strip().title()
        test_sco_1 = input_number('Enter the Test Score 1: ', float)
        test_sco_2 = input_number('Enter the test Score 2: ', float)
        work_sco = input_number('Enter the work score: ', float)
        return StudentsNotes(reg, name, test_sco_1, test_sco_2, work_sco)

    @classmethod
    def main(cls):
        student = cls.register()
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
                student = cls.register()
                continue
            if choice == 4:
                break
        print('=' * 50)


if __name__ == '__main__':
    StudentManage.main()
