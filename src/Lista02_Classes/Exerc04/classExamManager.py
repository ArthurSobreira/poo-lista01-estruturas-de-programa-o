from src.Lista02_Classes.Exerc04.classExam import Exam, AnswerSheet
from string import ascii_uppercase
import pandas as pd


class ExamManager(Exam):
    def __init__(self, stu_ans_list, ans_list):
        super().__init__(stu_ans_list)
        self.__answer_list = AnswerSheet(ans_list).answer_sheet

    # Getter and Setter __answer_list
    @property
    def answer_list(self):
        return self.__answer_list

    @answer_list.setter
    def answer_list(self, new_answer_list):
        self.__answer_list = new_answer_list

    # Main Methods
    def same_answer(self, ind):
        if self.answer_list[ind] == self.student_answers[ind]:
            return True

    def student_answer(self, question):
        try:
            return self.student_answers[question]
        except (IndexError, KeyError):
            return 0

    def number_right_answers(self):
        num_right_ans = 0
        for key in range(1, 16):
            if self.same_answer(key):
                num_right_ans += 1
        return num_right_ans

    def exam_grade(self):
        grd = 0
        for key in range(1, 16):
            if self.same_answer(key):
                if key <= 10:
                    grd += 0.5
                else:
                    grd += 1
        return grd

    def highest_grade(self, answers_obj):
        if answers_obj.exam_grade() > self.exam_grade():
            return answers_obj.exam_grade()
        return self.exam_grade()

    def print_answer_sheet(self):
        # Create Template
        letters = list(ascii_uppercase[:5])
        quest = dict()
        for c in letters:
            quest[c] = list('.' * 15)

        # Occupy Answer Sheet
        for q, l in enumerate(self.student_answers):
            quest[self.student_answers[l].upper()][q] = 'X'

        # Print Answer Sheet with DataFrame
        print(pd.DataFrame(quest).rename(index=lambda x: x + 1))
