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
        return self.name

    @name.setter
    def name(self, new_name):
        self.name = new_name

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


class Notes:
    def __init__(self):
        self.__name = Student.name
        self.__test_1_note = Student.test_1_note
        self.__test_2_note = Student.test_2_note
        self.__work_note = Student.work_note

    def average(self):
        test_sum = ((self.__test_1_note + self.__test_2_note) * 8) / 20
        work_sum = (self.__work_note * 2) / 10
        final_note = test_sum + work_sum
        return final_note

    def final(self, note):
        if note >= 6:
            return 0
        final_test = 12 - note
        print(f'Student {self.__name} must get a {final_test} on the final test to pass.')
        
