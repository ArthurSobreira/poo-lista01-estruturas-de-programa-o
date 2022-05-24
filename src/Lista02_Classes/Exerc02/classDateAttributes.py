from classDate import Date
import datetime


class DateAttributes(Date):
    def compare(self, date):
        date_1 = datetime.date(self.year, self.month, self.day)
        date_2 = datetime.date(date.year, date.month, date.day)
        if date_1 == date_2:
            return 0
        if date_1 > date_2:
            return 1
        return -1

    def month_by_name(self):
        month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'july',
                      'august', 'september', 'october', 'november', 'december']
        return month_list[self.month - 1].title()

    def clone(self):
        data_clone = Date(self.day, self.month, self.year)
        return data_clone
