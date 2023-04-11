import prompt


def game_start(game):
    print('Welcome to the Brain games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello,', user_name, '!')
    print(game.rules)
    tries = 3
    while tries != 0:
        right_answer, question = game.launch()
        print('Question:', question)
        user_answer = input('Your answer: ')
        if user_answer == str(right_answer):
            print('Correct!')
            tries -= 1
        else:
            print(user_answer + ' is wrong answer ;(. Correct answer was ' + str(right_answer))
            print("Let's try again,", user_name)
            break
    else:
        print('Congratulations, 'f'{user_name}!')
