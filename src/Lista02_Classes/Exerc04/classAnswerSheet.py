class AnswerSheet:
    def __init__(self, answers_list):
        answers_dic = {}
        if len(answers_list) == 15:
            for question, answer in enumerate(answers_list):
                if answer.lower() in 'abcde':
                    answers_dic[question + 1] = answer

        self.__answer_sheet = answers_dic

    # Getter and Setter __answer_sheet
    @property
    def answer_sheet(self):
        return self.__answer_sheet

    @answer_sheet.setter
    def answer_sheet(self, new_answer_sheet):
        self.__answer_sheet = new_answer_sheet


if __name__ == '__main__':
    gaba = AnswerSheet(['a', 'c', 'd', 'b', 'e', 'b', 'c', 'a', 'c', 'd', 'b', 'e', 'b', 'c', 'd'])
    print(gaba.answer_sheet)
