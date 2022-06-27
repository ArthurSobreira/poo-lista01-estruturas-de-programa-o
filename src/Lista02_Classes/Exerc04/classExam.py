from src.Lista02_Classes.Exerc04.classAnswerSheet import AnswerSheet


class Exam:
    def __init__(self, student_answers, answers_keys):
        self.__student_answers = AnswerSheet(student_answers)
        self.__answers_keys = AnswerSheet(answers_keys)

    # Getters and Setters
    @property
    def student_answers(self):
        return self.__student_answers

    @student_answers.setter
    def student_answers(self, new_student_answers):
        self.__student_answers = new_student_answers

    @property
    def answers_keys(self):
        return self.__answers_keys

    @answers_keys.setter
    def answers_keys(self, new_anwers_keys):
        self.__answers_keys = new_anwers_keys

    # Main Methods
    def same_answer(self, index):
        if self.answers_keys[index] == self.student_answers[index]:
            return True

    def question_answer(self, question):
        try:
            return self.student_answers[question]
        except (IndexError, KeyError):
            return 0

    def number_right_answers(self):
        num_right_ans = 0
        for index in range(1, 16):
            if self.same_answer(index):
                num_right_ans += 1
        return num_right_ans

    def exam_grade(self):
        grade = 0
        for index in range(1, 16):
            if self.same_answer(index):
                if index <= 10:
                    grade += 0.5
                else:
                    grade += 1
        return grade

