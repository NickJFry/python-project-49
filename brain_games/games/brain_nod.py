import random

RULES = 'Find the greatest common divisor of given numbers.'
START_RANGE = 1
END_RANGE = 100


def get_divisor(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1


def get_round():
    num1 = random.randint(START_RANGE, END_RANGE)
    num2 = random.randint(START_RANGE, END_RANGE)
    question = num1, num2
    right_answer = get_divisor(num1, num2)
    return right_answer, question
