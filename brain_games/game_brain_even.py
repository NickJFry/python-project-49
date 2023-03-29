import random, prompt


def is_even():
    name = prompt.string('May I have your name? ')
    print('Hello,', name, '!')
    count_answer = 3
    rules = 'Answer "yes" if the number is even, otherwise answer "no"'
    print(rules)
    while count_answer != 0:
        num = random.randint(1, 100)
        print('Question:', num)
        user_answer = input('Your answer: ')
        if num % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'
        if right_answer == user_answer:
            print('Correct!')
            count_answer -= 1
        else:
            print('"yes" is wrong answer ;(. Correct answer was "no".\nLet\'s try again')
            break
    else:
        print('Congratulations, 'f'{name}!')
