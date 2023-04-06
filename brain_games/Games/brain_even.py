import random, prompt


rules = 'Answer "yes" if the number is even, otherwise answer "no"'


def launch():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello,', user_name, '!')
    print(rules)
    tries = 3
    while tries != 0:
        num = random.randint(1, 100)
        question = num
        print('Question:', question)
        user_answer = input('Your answer: ')
        if num % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'
        if right_answer == user_answer:
            print('Correct!')
            tries -= 1
        else:
            print('"yes" is wrong answer ;(. Correct answer was "no".\nLet\'s try again')
            break
    else:
        print('Congratulations, 'f'{user_name}!')

launch()