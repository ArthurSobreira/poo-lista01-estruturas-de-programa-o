from Exerc03_BinaryConverter import *
from math import *


def interest_calculator(capital, fee, time):
    inter = capital * (fee / 100) * time
    return inter


def main():
    loan = input_number('Enter the loan value: R$ ', float)
    portion = input_number('Enter the value of the payment installment: R$ ', float)
    fees = input_number('Enter the fee value: % ')


# if __name__ == '__main__':
#     main()
