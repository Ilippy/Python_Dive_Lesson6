# * Вспомните какие модули вы уже проходили на курсе.
# * Создайте файл, в котором вы импортируете встроенные в модуль функции под псевдонимами. (3-7 строк импорта).
def task1():
    from lesson_6_package.task7_check_date import *



# � Создайте модуль с функцией внутри.
# � Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# � Внутри генерируется случайное число в указанных границах
# и пользователь должен угадать его за заданное число попыток.
# � Функция выводит подсказки “больше” и “меньше”.
# � Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
def task2():
    from lesson_6_package.task2_guess_number import guess_number
    print(guess_number(0, 5, 3))


# � Улучшаем задачу 2.
# � Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# � Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# � Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное
# выражение.
def task3():
    from lesson_6_package.task3_guess_number import guess_number
    print(guess_number(5))


# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.
def task4():
    from lesson_6_package.task4_guess_answer import guess_answer
    print(guess_answer("Весит груша, нельзя скушать", ["лампочка"], 5))


# � Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# � Ключ словаря - загадка, значение - список с отгадками.
# � Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки
def task5():
    from lesson_6_package.task5_guess_answer import survey
    dct = {"Весит груша, нельзя скушать": ["лампочка"]}
    survey(dct)


# � Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки)
# и число (номер попытки, с которой она угадана).
# � Функция формирует словарь с информацией о результатах отгадывания.
# � Для хранения используйте защищённый словарь уровня модуля.
# � Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения
# виде.
# � Для формирования результатов используйте генераторное выражение.
def task6():
    from lesson_6_package.task6_guess_answers import survey, print_answers
    dct = {"Весит груша, нельзя скушать": ["лампочка"], "Загадка 2": ['1', '2', '3'], "Загадка 3": ['1', '2', '3']}
    print_answers(survey(dct))


# � Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# � Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# � Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# � Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# � Проверку года на високосность вынести в отдельную защищённую функцию.
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
