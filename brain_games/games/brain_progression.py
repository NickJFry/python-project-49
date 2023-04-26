from random import randint


RULES = 'What number is missing in the progression?'
START_TERM = 1
END_TERM = 20
MIN_DIFF = 1
MAX_DIFF = 10
MIN_REPEAT = 5
MAX_REPEAT = 10


def get_progression_numbers():
    term = randint(START_TERM, END_TERM)
    common_difference = randint(MAX_DIFF, MAX_DIFF)
    repeat = randint(MIN_REPEAT, MAX_REPEAT)
    series = []
    for num in range(term, term + common_difference * repeat, common_difference):
        series.append(num)
    return series


def get_progression_string(progression_list):
    progression = ' '.join(map(str, progression_list))
    return progression


def get_round():
    get_progression = get_progression_numbers()
    element_x = randint(1, len(get_progression) - 1)
    right_answer = get_progression[element_x]
    get_progression[element_x] = '..'
    question = get_progression_string(get_progression)
    return right_answer, question
