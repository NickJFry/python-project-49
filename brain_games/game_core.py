import prompt
tries = 3


def game_start(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello,', user_name, '!')
    print(game.rules)
    while tries != 0:
        right_answer, question = game.launch()
        print('Question:', question)
        user_answer = input('Your answer: ')
        if user_answer == right_answer:
            print('Correct!')
        else:
            print(user_answer + 's wrong answer ;(. Correct answer was ' + right_answer)
            print("Let's try again,", user_name)
            break
    else:
        print('Congratulations, 'f'{user_name}!')
