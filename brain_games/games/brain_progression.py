from random import randint
# https://asciinema.org/connect/7685d9e0-be41-40b5-ab49-77cae8fc7158


rules = 'What number is missing in the progression?'


def launch():
    start = randint(1, 20)
    step = randint(1, 10)
    repeat = randint(5, 10)
    series = []
    for num in range(start, start + step * repeat, step):
        series.append(num)
    x = randint(1, len(series) - 1)
    progression = ' '.join(map(str, series))
    question = progression.replace(str(series[x]), '..')
    right_answer = series[x]
    return right_answer, question
