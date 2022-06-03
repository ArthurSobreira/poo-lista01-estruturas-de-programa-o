class AnswerSheet:
    def __init__(self, answers_list):
        answers_dic = {}
        if len(answers_list) == 15:
            for question, answer in enumerate(answers_list):
                if answer.lower() in 'abcde':
                    answers_dic[question + 1] = answer

        self.answer_sheet = answers_dic


if __name__ == '__main__':
    gaba = AnswerSheet(['a', 'c', 'd', 'b', 'e', 'b', 'c', 'a', 'c', 'd', 'b', 'e', 'b', 'c', 'd'])
    print(gaba.answer_sheet[1])
