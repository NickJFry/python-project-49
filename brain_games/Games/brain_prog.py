import random
import prompt

def test():
    num_start = random.randint(1, 20)
    start = num_start
    num_step = random.randint(1, 10)
    step = num_step
    repeat = random.randint(5, 10)
    n = repeat
    series = []
    for num in range(start, start + step * n, step):
        series.append(num)
    print(series)
    x = random.randint(1, len(series) - 1)
    replace = str(series).replace(str(series[x]), '..')
    print(replace)
    right_answer = series[x]
    user_answer = input('число: ')
    if int(user_answer) == right_answer:
        print('Nice')
    else:
        print('Ne nice')