import random


RULES = 'What is the result of the expression?'

FIRST_RANGE_START = 6
FIRST_RANGE_END = 10
SECOND_RANGE_START = 1
SECOND_RANGE_END = 5


def get_round():
    num1 = random.randint(FIRST_RANGE_START, FIRST_RANGE_START)
    num2 = random.randint(SECOND_RANGE_START, SECOND_RANGE_END)
    operators = ['+', '-', '*']
    sign = random.choice(operators)
    question = str(num1) + sign + str(num2)
    if sign == '+':
        right_answer = str(num1 + num2)
    elif sign == '-':
        right_answer = str(num1 - num2)
    else:
        right_answer = str(num1 * num2)
    return right_answer, question
