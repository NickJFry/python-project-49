import random
from math import sqrt


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START_RANGE = 1
END_RANGE = 100


def is_prime(num):
    if num == 1:
        return False
    i = 2
    while i <= sqrt(num):
        if num % i == 0:
            return False
        i += 1
    return True


def get_round():
    num = random.randint(START_RANGE, END_RANGE)
    question = num
    if is_prime(num):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return right_answer, question
