from Exerc03_BinaryConverter import *
from math import *


def interest_calculator(capital, fee):
    inter = capital * (fee / 100)
    return inter


def main():
    loan = input_number('Enter the loan value: R$ ', float)
    portion = input_number('Enter the value of the payment installment: R$ ', float)
    fees = input_number('Enter the fee value: % ')
    interest = interest_calculator(loan, fees)

    total_inter = interest
    debt = loan - (portion - interest)
    c = 1
    while debt > 0:
        print()
        print(f'================= {c}st Month =================')
        print(f'> Value of interest paid: R${interest:.2f}')
        print(f'> Value applied in the loan payment: R${portion - interest:.2f}')
        print(f'> Accumulated interest value: R${total_inter:.2f}')
        print(f'> Loan value still to be paid: R${debt:.2f}')
        total_inter += interest
        debt -= portion - interest
        c += 1


if __name__ == '__main__':
    main()
