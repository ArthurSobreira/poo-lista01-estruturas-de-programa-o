def fibonacci(number):
    first_number = second_number = 1
    list_fibo = [first_number, second_number]
    while True:
        current_number = first_number + second_number
        list_fibo.append(current_number)
        first_number = second_number
        second_number = current_number
        if current_number > number:
            return list_fibo
