#from src.Lista02_Classes.Exerc04.classExamManager import ExamManager
from src.Lista01_EstruturasDeProgramacao.Exerc03_BinaryConverter import input_number
from string import ascii_lowercase


def answers_list():
    ans_list = list()
    for c in range(1, 16):
        while True:
            alt = input_number(f'Enter the answer to question {c}: ', str).lower().strip()
            if alt in ascii_lowercase[:5]:
                ans_list.append(alt)
                break
            print('\033[31mInsert only alternatives between A-E!!\033[m')
    return ans_list


if __name__ == '__main__':
    main_list = answers_list()
    print(main_list)
