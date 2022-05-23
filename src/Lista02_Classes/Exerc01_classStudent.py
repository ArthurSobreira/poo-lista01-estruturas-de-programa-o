class Student:
    def __init__(self, register, name, test_1_note, test_2_note, work_note):
        self.__register = register
        self.__test_1_note = test_1_note
        self.__test_2_note = test_2_note
        self.__work_note = work_note
        self.__name = name

    # Getter and Setter __name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    # Getter and Setter __test_1_note
    @property
    def test_1_note(self):
        return self.__test_1_note

    @test_1_note.setter
    def test_1_note(self, new_note):
        self.__test_1_note = new_note

    # Getter and Setter __test_2_note
    @property
    def test_2_note(self):
        return self.__test_2_note

    @test_2_note.setter
    def test_2_note(self, new_note):
        self.__test_2_note = new_note

    # Getter and Setter __work_note
    @property
    def work_note(self):
        return self.__work_note

    @work_note.setter
    def work_note(self, new_note):
        self.__work_note = new_note


class StudentsNotes(Student):
    def average(self):
        test_sum = ((self.test_1_note + self.test_2_note) * 8) / 20
        work_sum = (self.work_note * 2) / 10
        final_note = test_sum + work_sum
        return final_note

    def final(self, note):
        if note >= 6:
            print(f'Student {self.name} is not in recovery.')
        else:
            final_test = 12 - note
            print(f'Student {self.name} must get a {final_test} on the final test to pass.')


class StudentManage:
    @staticmethod
    def input_value(msg, type=int):
        while True:
            try:
                number = type(input(msg))
            except (ValueError, TypeError):
                print('\033[31mInvalid Value, Try Again!\033[m')
                continue
            else:
                return number

    @staticmethod
    def apart(msg, size):
        print('=' * size)
        print(f'{msg:^{size}}')
        print('=' * size)

    @classmethod
    def register(cls):
        cls.apart('Wellcome to the Student Manage', 50)
        reg = cls.input_value("Enter the student's matriculation number: ", int)
        name = cls.input_value('Enter the student name: ', str).strip().title()
        test_sco_1 = cls.input_value('Enter the Test Score 1: ', float)
        test_sco_2 = cls.input_value('Enter the test Score 2: ', float)
        work_sco = cls.input_value('Enter the work score: ', float)
        return StudentsNotes(reg, name, test_sco_1, test_sco_2, work_sco)

    @classmethod
    def main(cls):
        student = cls.register()
        while True:
            print('=' * 50)
            choice = cls.input_value(
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
                final = student.final(student.average())
                continue
            if choice == 3:
                student = cls.register()
                continue
            if choice == 4:
                break


if __name__ == '__main__':
    StudentManage.main()
