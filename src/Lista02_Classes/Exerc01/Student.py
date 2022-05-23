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
