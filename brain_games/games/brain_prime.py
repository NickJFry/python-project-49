import random
from random import randint
from math import sqrt
# https://asciinema.org/connect/7685d9e0-be41-40b5-ab49-77cae8fc7158


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START_RANGE = 1
END_RANGE = 100


def is_prime(num):
    i = 2
    while i <= sqrt(num):
        if num % i == 0:
            return False
        i += 1
    return True


def get_round():
    num = random.randint(START_RANGE, END_RANGE)
    question = num
    if is_prime(num) is False:
        right_answer = 'no'
    else:
        right_answer = 'yes'
    return right_answer, question
