import prompt

ROUNDS = 3


def play_game(game):
    print('Welcome to the Brain games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello,', user_name, '!')
    print(game.RULES)
    rounds = ROUNDS
    while rounds != 0:
        right_answer, question = game.get_round()
        print('Question:', question)
        user_answer = input('Your answer: ')
        if user_answer == str(right_answer):
            print('Correct!')
            rounds -= 1
        else:
            print(user_answer
                  + ' is wrong answer ;(. Correct answer was '
                  + str(right_answer))
            print("Let's try again, "f"{user_name}!")
            break
    else:
        print('Congratulations, 'f'{user_name}!')
