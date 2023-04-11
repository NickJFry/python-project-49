import random
# https://asciinema.org/connect/7685d9e0-be41-40b5-ab49-77cae8fc7158

rules = 'Answer "yes" if the number is even, otherwise answer "no"'


def launch():
    num = random.randint(1, 100)
    question = num
    if num % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return right_answer, question
