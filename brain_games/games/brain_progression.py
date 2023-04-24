from random import randint
# https://asciinema.org/connect/7685d9e0-be41-40b5-ab49-77cae8fc7158


RULES = 'What number is missing in the progression?'


def get_progression_numbers():
    term = randint(1, 20)
    common_difference = randint(1, 10)
    repeat = randint(5, 10)
    series = []
    for num in range(term, term + common_difference * repeat, common_difference):
        series.append(num)
    return series


def get_progression_string(progression_list):
    progression = ' '.join(map(str, progression_list))
    return progression


def get_round():
    get_progression = get_progression_numbers()
    get_string = get_progression_string(get_progression)
    element_x = randint(1, len(get_progression) - 1)
    question = get_string.replace(str(get_progression[element_x]), '..')
    right_answer = get_progression[element_x]
    return right_answer, question
