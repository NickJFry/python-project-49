import random

RULES = 'Find the greatest common divisor of given numbers.'
START_RANGE = 1
END_RANGE = 100


def get_divisor():
    num1 = random.randint(START_RANGE, END_RANGE)
    num2 = random.randint(START_RANGE, END_RANGE)
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1


def get_round():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = num1, num2
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    right_answer = num1
    return right_answer, question
