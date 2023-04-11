import random
# https://asciinema.org/connect/7685d9e0-be41-40b5-ab49-77cae8fc7158


rules = 'What is the result of the expression?'


def launch():
        num1 = random.randint(6, 10)
        num2 = random.randint(1, 5)
        operators = ['+', '-', '*']
        sign = random.choice(operators)
        question = str(num1) + sign + str(num2)
        if sign == '+':
            right_answer = str(num1 + num2)
        elif sign == '-':
            right_answer = str(num1 - num2)
        else:
            right_answer = str(num1 * num2)
        return right_answer, question