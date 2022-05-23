from classStudent import Student


class StudentsNotes(Student):
    def average(self):
        test_sum = ((self.test_1_note + self.test_2_note) * 8) / 20
        work_sum = (self.work_note * 2) / 10
        final_note = test_sum + work_sum
        return final_note

    def final(self, note):
        if note >= 6:
            print(f'Student {self.name} is not in recovery.')
        else:
            final_test = 12 - note
            print(f'Student {self.name} must get a {final_test} on the final test to pass.')
