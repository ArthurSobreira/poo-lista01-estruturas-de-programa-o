class Student:
    def __init__(self, register, name, exam_1_grade, exam_2_grade, work_grade):
        self.__register = register
        self.__exam_1_grade = exam_1_grade
        self.__exam_2_grade = exam_2_grade
        self.__work_grade = work_grade
        self.__name = name

    # Getter and Setter __name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    # Getter and Setter __exam_1_grade
    @property
    def exam_1_grade(self):
        return self.__exam_1_grade

    @exam_1_grade.setter
    def exam_1_grade(self, new_grade):
        self.__exam_1_grade = new_grade

    # Getter and Setter __exam_2_grade
    @property
    def exam_2_grade(self):
        return self.__exam_2_grade

    @exam_2_grade.setter
    def exam_2_grade(self, new_grade):
        self.__exam_1_grade = new_grade

    # Getter and Setter __work_grade
    @property
    def work_grade(self):
        return self.__work_grade

    @work_grade.setter
    def work_grade(self, new_grade):
        self.__work_grade = new_grade
