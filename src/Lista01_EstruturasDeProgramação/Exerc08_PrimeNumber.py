def prime_number(number):
    primes_list = []
    for c in range(1, (number + 1)):
        div_list = []
        for i in range(1, (c + 1)):
            if c % i == 0:
                div_list.append(i)
        if len(div_list) == 2:
            primes_list.append(c)

    if number in primes_list:
        return True
    return False


