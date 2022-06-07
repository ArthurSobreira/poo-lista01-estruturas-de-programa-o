from string import ascii_lowercase


class AnswerSheet:
    def __init__(self, answers_list):
        answers_dic = dict()
        if len(answers_list) == 15:
            for question, answer in enumerate(answers_list):
                if answer.lower() in ascii_lowercase[:5]:
                    answers_dic[question + 1] = answer

        self.__answer_sheet = answers_dic

    # Getter and Setter __answer_sheet
    @property
    def answer_sheet(self):
        return self.__answer_sheet

    @answer_sheet.setter
    def answer_sheet(self, new_answer_sheet):
        self.__answer_sheet = new_answer_sheet

    # Instance Method
    def right_answer(self, question):
        try:
            return self.answer_sheet[question]
        except (TypeError, ValueError, KeyError):
            return 0
