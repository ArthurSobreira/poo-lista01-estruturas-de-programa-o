from src.Lista02_Classes.Exerc04.classExam import Exam, AnswerSheet


class ExamManager(Exam):
    def __init__(self, stu_ans_list, ans_list):
        super().__init__(stu_ans_list)
        self.__obj = AnswerSheet(ans_list)
        self.simple_list = ans_list
        self.print_ans_list = AnswerSheet(ans_list).__str__()

    # Getter and Setter __answer_list
    @property
    def answer_list(self):
        return self.__obj.answer_sheet

    @answer_list.setter
    def answer_list(self, new_answer_list):
        self.__obj.answer_sheet = new_answer_list

    # Main Methods
    def same_answer(self, ind):
        if self.answer_list[ind] == self.student_answers[ind]:
            return True

    def question_answer(self, question):
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
