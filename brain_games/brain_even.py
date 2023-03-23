import random


def is_even():
    num = random.randint(1, 100)
    print('Question:', num)
    if num % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    user_answer = input('Your answer: ')
    if user_answer == right_answer:
        return right_answer, user_answer
    else:
        return user_answer, user_answer


count_answer = 3
i = 0
while i < 1:
    rules = 'Answer "yes" if the number is even, otherwise answer "no"'
    print(rules)
    i = i + 1
while count_answer != 0:
    even, not_even = is_even()
    if even == not_even:
        print('Correct!')
        count_answer -= 1
    else:
        print('"yes" is wrong answer ;(. Correct answer was "no".\nLet\'s try again')
        break
else:
    print('Congrat Brat!')

