# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
from random import randint

__all__ = ['guess_number']


def guess_number(min_value: int, max_value: int, amount_of_tries: int) -> bool:
    print(f"Угадайте число в диапазоне {min_value}..{max_value} c {amount_of_tries} попыток")
    number = randint(min_value, max_value)
    for i in range(1, amount_of_tries + 1):
        try_number = int(input(f"Попытка №{i}: \nВведите число: "))
        if number == try_number:
            return True
        print("Меньше" if try_number > number else "Больше")
    return False
