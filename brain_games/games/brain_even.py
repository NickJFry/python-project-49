import random

RULES = 'Answer "yes" if the number is even, otherwise answer "no"'
START_RANGE = 1
END_RANGE = 100


def is_even(num):
    if num % 2 == 0:
        return True
    return False


def get_round():
    num = random.randint(START_RANGE, END_RANGE)
    question = num
    if is_even(num) is True:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return right_answer, question
