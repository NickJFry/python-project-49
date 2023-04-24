import random


RULES = 'What is the result of the expression?'

START_FIRST_RANGE = 6
END_FIRST_RANGE = 10

START_SECOND_RANGE = 1
END_SECOND_RANGE = 5


def get_round():
    num1 = random.randint(START_FIRST_RANGE, END_FIRST_RANGE)
    num2 = random.randint(START_SECOND_RANGE, END_SECOND_RANGE)
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
