from random import randint


RULES = 'What number is missing in the progression?'
START_TERM = 1
END_TERM = 20
MIN_DIFF = 1
MAX_DIFF = 10
MIN_REPEAT = 5
MAX_REPEAT = 10


def get_progression(initial_term, common_difference, length):
    series = []
    for num in range(initial_term,
                     initial_term + common_difference * length,
                     common_difference):
        series.append(num)
    return series


def stringify(progression):
    progression = ' '.join(map(str, progression))
    return progression


def get_round():
    progression = get_progression(randint(START_TERM, END_TERM),
                                  randint(MIN_DIFF, MAX_DIFF),
                                  randint(MAX_REPEAT, MAX_REPEAT))
    hidden_term_index = randint(1, len(progression) - 1)
    right_answer = progression[hidden_term_index]
    progression[hidden_term_index] = '..'
    question = stringify(progression)
    return right_answer, question
