from src.Lista02_Classes.Exerc04.classAnswerSheet import AnswerSheet


class Exam:
    def __init__(self, stu_ans_list):
        self.__obj = AnswerSheet(stu_ans_list)
        self.print_stu_ans_list = AnswerSheet(stu_ans_list).__str__()

    # Getter and Setter __student_answers
    @property
    def student_answers(self):
        return self.__obj.answer_sheet

    @student_answers.setter
    def student_answers(self, new_student_answers):
        self.__obj.answer_sheet = new_student_answers
