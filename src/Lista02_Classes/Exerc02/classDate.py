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
            self.day, self.month, self.year = day, month, year
        else:
            self.day, self.month, self.year = 1, 1, 1

    def leap_year(self):
        if ((self.year % 4 == 0) and (self.year % 100 != 0)) or (self.year % 400 == 0):
            return True
