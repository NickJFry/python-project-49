import random


rules = 'Find the greatest common divisor of given numbers.'


def launch():
    # tries = 3
    # while tries != 0:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        question = num1, num2
        while num1 != num2:
            if num1 > num2:
                num1 = num1 - num2
            else:
                num2 = num2 - num1
        right_answer = num1
        return right_answer, question
    #   print(right_answer)
    #     user_answer = input('Your answer: ')
    #     if int(user_answer) == right_answer:
    #         print('Correct!')
    #         tries -= 1
    #     else:
    #         print(user_answer + ' is wrong answer ;(. Correct answer was ' + f'{right_answer}')
    #         break
    # else:
    #     print('Congrat!')
