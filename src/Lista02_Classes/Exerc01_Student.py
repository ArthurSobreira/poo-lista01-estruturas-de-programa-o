class Student:
    def __init__(self, register, name, test_1_note, test_2_note, work_note):
        self.__register = register
        self.__test_1_note = test_1_note
        self.__test_2_note = test_2_note
        self.__work_note = work_note
        self.name = name

    def average(self):
        test_sum = ((self.__test_1_note + self.__test_2_note) * 8) / 20
        work_sum = (self.__work_note * 2) / 10
        final_note = test_sum + work_sum
        return final_note

    def final(self, note):
        if note >= 6:
            return 0
        final_test = 12 - note
        print(f'Student {self.name} must get a {final_test} on the final test to pass.')
