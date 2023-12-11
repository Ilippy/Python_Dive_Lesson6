# * Вспомните какие модули вы уже проходили на курсе.
# * Создайте файл, в котором вы импортируете встроенные в модуль функции под псевдонимами. (3-7 строк импорта).
def task1():
    pass


# � Создайте модуль с функцией внутри.
# � Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# � Внутри генерируется случайное число в указанных границах
# и пользователь должен угадать его за заданное число попыток.
# � Функция выводит подсказки “больше” и “меньше”.
# � Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
def task2():
    from lesson_6_package.task2_guess_number import guess_number
    print(guess_number(0, 5, 3))


def task3():
    from lesson_6_package.task3_guess_number import guess_number
    print(guess_number(5))


# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.
def task4():
    from lesson_6_package.task4_guess_answer import guess_answer
    print(guess_answer("Весит груша, нельзя скушать", ["лампочка"], 5))


def task5():
    from lesson_6_package.task5_guess_answer import survey
    dct = {"Весит груша, нельзя скушать": ["лампочка"]}
    survey(dct)


def task6():
    from lesson_6_package.task6_guess_answers import survey, print_answers
    dct = {"Весит груша, нельзя скушать": ["лампочка"], "Загадка 2": ['1', '2', '3'], "Загадка 3": ['1', '2', '3']}
    print_answers(survey(dct))


def task7():
    from lesson_6_package.task7_check_date import check_date
    print(check_date("29.02.2004"))


def main():
    # task1()
    # task2()
    # task3()
    # task4()
    # task5()
    # task6()
    task7()


if __name__ == '__main__':
    main()
