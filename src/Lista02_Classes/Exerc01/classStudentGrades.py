from classStudent import Student


class StudentsNotes(Student):
    def average(self):
        test_sum = ((self.test_1_note + self.test_2_note) * 8) / 20
        work_sum = (self.work_note * 2) / 10
        final_grade = test_sum + work_sum
        return final_grade

    def final(self, grade):
        if grade >= 6:
            print(f'The student {self.name} is not get held back.')
        else:
            final_test = 12 - grade
            print(f'The student {self.name} must get a {final_test} on the final exam to pass.')
