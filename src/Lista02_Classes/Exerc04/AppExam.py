from src.Lista02_Classes.Exerc04.classExamManager import ExamManager
from src.Lista01_EstruturasDeProgramacao.Exerc03_BinaryConverter import input_number
from string import ascii_lowercase
from random import choice


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


def input_answers_list():
    exam_answers = list()
    for c in range(15):
        alt = choice(ascii_lowercase[:5])
        exam_answers.append(alt)
    stud_answers = answers_list()
    return ExamManager(stud_answers, exam_answers)

