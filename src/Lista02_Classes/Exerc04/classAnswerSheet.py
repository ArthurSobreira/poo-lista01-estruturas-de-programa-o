from string import ascii_lowercase, ascii_uppercase
import pandas as pd


class AnswerSheet:
    def __init__(self, answers_list):
        answers_dic = dict()
        if len(answers_list) == 15:
            for question, answer in enumerate(answers_list):
                if answer.lower() in ascii_lowercase[:5]:
                    answers_dic[question + 1] = answer

        self.__answer_sheet = answers_dic

    def __str__(self):
        # Create Template
        letters = list(ascii_uppercase[:5])
        answer_sht = dict()
        for c in letters:
            answer_sht[c] = list('.' * 15)

        # Occupy Answer Sheet
        for q, l in enumerate(self.answer_sheet):
            answer_sht[self.answer_sheet[l].upper()][q] = 'X'

        # Return DataFrame of Answer Sheet
        return str(pd.DataFrame(answer_sht).rename(index=lambda x: x + 1))

    # Getter and Setter __answer_sheet
    @property
    def answer_sheet(self):
        return self.__answer_sheet

    @answer_sheet.setter
    def answer_sheet(self, new_answer_sheet):
        self.__answer_sheet = new_answer_sheet
