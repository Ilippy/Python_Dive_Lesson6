# Создайте модуль и напишите в нём функцию,
# которая получает на вход дату в формате DD.MM.YYYY и возвращает истину,
# если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999]. И весь период действует григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

__all__ = ['check_date']


def _is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False


def check_date(arg: str) -> bool:
    try:
        day, month, year = map(int, arg.split("."))
    except ValueError:
        return False
    if 0 < year < 10_000:
        if month in [1, 3, 5, 7, 8, 10, 12] and 0 < day < 32 or \
                month in [4, 6, 9, 11] and 0 < day < 31 or \
                month == 2 and 0 < day < 29 + _is_leap_year(year):
            return True
        else:
            return False
    return False
