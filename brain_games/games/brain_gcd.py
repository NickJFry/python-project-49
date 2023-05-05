import random

RULES = 'Find the greatest common divisor of given numbers.'
START_RANGE = 1
END_RANGE = 100


def get_divisor(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1


def get_round():
    numbers = (random.randint(START_RANGE, END_RANGE), random.randint(START_RANGE, END_RANGE))
    num1 = numbers[0]
    num2 = numbers[1]
    question = str(num1) + ' ' + str(num2)
    right_answer = get_divisor(num1, num2)
    return right_answer, question
