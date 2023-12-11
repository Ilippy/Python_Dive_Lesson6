# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

__all__ = ['guess_answer']


def guess_answer(question: str, answers: list[str], tries: int) -> int:
    for i in range(tries):
        print(question)
        answer = input("Введите ваш ответ: ")
        if answer in answers:
            return i + 1
        else:
            print("Ответ не верный")
    return 0
