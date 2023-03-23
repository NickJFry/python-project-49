import random


def is_even():
    num = random.randint(1, 100)
    print('Question:', num)
    one = 1
    zero = 0
    if num % 2 == 0:
        good = 'yes'
    else:
        good = 'no'
    answer = input('Your answer: ')
    if answer == good:
        return one, one
    else:
        return one, zero


count_answer = 3
i = 0
while i < 1:
    rules = 'Answer "yes" if the number is even, otherwise answer "no"'
    print(rules)
    i = i + 1
while count_answer != 0:
    right_answer, user_answer = is_even()
    if user_answer == right_answer:
        print('Correct!')
        count_answer -= 1
    else:
        print('"yes" is wrong answer ;(. Correct answer was "no".\nLet\'s try again')
        break
else:
    print('Congrat Brat!')


print(is_even())
