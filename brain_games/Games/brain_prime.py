from random import randint
from math import sqrt


rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def launch():
    num = randint(1, 100)
    question = num
    i = 2
    while i <= sqrt(num):
        if num % i == 0:
            right_answer = 'no'
            break
        i += 1
    else:
        right_answer = 'yes'
    return right_answer, question
