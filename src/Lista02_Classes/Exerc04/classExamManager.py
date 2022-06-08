from src.Lista02_Classes.Exerc04.classExam import Exam, AnswerSheet


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
    def student_answer(self):
        pass

    def number_right_answers(self):
        num_right_ans = 0
        for key in range(1, 16):
            if self.answer_list[key] == self.student_answers[key]:
                num_right_ans += 1
        return num_right_ans

    def exam_grade(self):
        for key in range(1, 16):
            if key <= 10:
                pass
            else:
                pass

    def highest_grade(self):
        pass


if __name__ == '__main__':
    li_es = ['b', 'b', 'e', 'd', 'e', 'a', 'b', 'c', 'd', 'a', 'a', 'b', 'c', 'd', 'e']
    li_main = ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']
    t = ExamManager(li_es, li_main)
    print(t.answer_list)
    print(t.student_answers)
    print(t.number_right_answers())
