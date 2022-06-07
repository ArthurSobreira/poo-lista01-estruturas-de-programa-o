from src.Lista02_Classes.Exerc04.classExam import Exam, AnswerSheet


class ExamManager(Exam):
    def __init__(self, stu_ans_list, ans_list):
        super().__init__(stu_ans_list)
        self.__answer_list = AnswerSheet(ans_list)

    # Getter and Setter __answer_list
    @property
    def answer_list(self):
        return self .__answer_list

    @answer_list.setter
    def answer_list(self, new_answer_list):
        self.__answer_list = new_answer_list

    # Main Methods
    def student_answer(self):
        pass

    def right_answers(self):
        pass

    def exam_grade(self):
        pass

    def highest_grade(self):
        pass
