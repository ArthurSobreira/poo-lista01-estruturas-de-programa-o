from src.Lista02_Classes.Exerc04.classAnswerSheet import AnswerSheet


class Exam:
    def __init__(self, ans_list):
        self.__answer_sheet = AnswerSheet(ans_list)

    @property
    def answer_sheet(self):
        return self.__answer_sheet

    @answer_sheet.setter
    def answer_sheet(self, new_answer_sheet):
        self.__answer_sheet = new_answer_sheet
