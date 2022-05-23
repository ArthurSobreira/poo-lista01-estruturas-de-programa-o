import datetime


class Date:
    def __init__(self, day, month, year):
        months = [[2], [4, 6, 9, 11], [1, 3, 5, 7, 8, 10, 12]]
        valid_date = False
        if year > 0:
            if month in range(1, 13):
                # Months with 30 days
                if (day in months[1]) and (day in range(1, 31)):
                    valid_date = True

                # Months with 31 days
                if (day in months[2]) and (day in range(1, 32)):
                    valid_date = True

                # Month with 28/29 days
                if day in months[0]:
                    if (Date.leap_year(year)) and (day in range(1, 30)):
                        valid_date = True
                    if (not Date.leap_year(year)) and (day in range(1, 29)):
                        valid_date = True

        if valid_date:
            self.__day, self.__month, self.__year = day, month, year
        else:
            self.__day, self.__month, self.__year = 1, 1, 1

    @property
    def day(self):
        return self.__day

    @property
    def month(self):
        return self.__month

    @property
    def year(self):
        return self.__year

    @staticmethod
    def leap_year(year):
        if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
            return True

    def compare(self, year, month, day):
        date_1 = datetime.date(self.year, self.month, self.day)
        date_2 = datetime.date(year, month, day)
        if date_1 == date_2:
            return 0
        if date_1 > date_2:
            return 1
        return -1

    def month_by_name(self):
        month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'july',
                      'august', 'september', 'october','november', 'december']
        return month_list[self.month - 1].title()
