class Odd:
    def __init__(self, var_a, var_b):
        self.__a = var_a
        self.__b = var_b

    @property
    def var_a(self):
        return self.__a

    @property
    def var_b(self):
        return self.__b

    def odd_between(self):
        list_odd = []
        if self.__a < self.__b:
            for c in range((self.__a + 1), self.__b):
                if c % 2 != 0:
                    list_odd.append(c)
        else:
            for c in range((self.__b + 1), self.__a):
                if c % 2 != 0:
                    list_odd.append(c)

        return list_odd


def main():
    result = Odd(5, 9)
    list_odd = result.odd_between()
    print(f'Odd between {result.var_a} and {result.var_b}: ')
    for c in list_odd:
        print(c, end='...')


if __name__ == '__main__':
    main()
