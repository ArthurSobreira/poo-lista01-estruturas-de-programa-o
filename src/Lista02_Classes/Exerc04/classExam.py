from src.Lista02_Classes.Exerc04.classAnswerSheet import AnswerSheet


class Exam:
    def __init__(self, ans_list):
        self.__student_answers = AnswerSheet(ans_list)

    def __str__(self):
        return self.student_answers

    @property
    def student_answers(self):
        return self.__student_answers

    @student_answers.setter
    def student_answers(self, new_student_answers):
        self.__student_answers = new_student_answers
