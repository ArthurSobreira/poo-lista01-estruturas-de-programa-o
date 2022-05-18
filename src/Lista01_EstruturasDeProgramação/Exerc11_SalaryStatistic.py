def salary_statistic(salary_list):
    list_size = len(salary_list)
    average = sum(salary_list) / list_size
    above_average = []
    for c in salary_list:
        if c > average:
            above_average.append(c)
    print(f'{len(above_average)} functionary(ies) have above average salary(ies)')
