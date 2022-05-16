def addition(salary):
    if salary in range(150):
        return 25
    if salary in range(150, 300):
        return 20
    if salary in range(300, 600):
        return 15
    if salary >= 600:
        return 10


def readjustment(salary, percent):
    perc = salary * (percent / 100)
    return salary + perc


def print_info(name, current_sal, new_salary):
    print(f'> Name: {name}\n'
          f'> Current Salary: R${current_sal:.2f}\n'
          f'> Salary Readjusted: R${new_salary:.2f}')


def main():
    list_current_sal = []
    list_new_sal = []
    while True:
        print()
        name = str(input("Enter the functionary's name (End for stop): ")).strip().title()
        if name == 'End':
            break
        salary = float(input("Enter the functionary's currently salary: "))
        list_current_sal.append(salary)
        add = addition(salary)
        new_salary = readjustment(salary, add)
        list_new_sal.append(new_salary)
        print_info(name, salary, new_salary)

    print(f'Sum of the Current Salaries: R${sum(list_current_sal):.2f}\n'
          f'Sum of the Readjusted Salaries: R${sum(list_new_sal):.2f}\n'
          f'Difference between the sum of salaries: {(sum(list_new_sal) - sum(list_current_sal)):.2f}')


if __name__ == '__main__':
    main()
