# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

from lesson_6_package.task4_guess_answer import guess_answer

__all__ = ['survey']


def survey(dct: dict[str, list[str]], tries=3):
    for question, answers in dct.items():
        guess_answer(question, answers, tries)
