# Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем.
# На вход будет подаваться дата в формате "день.месяц.год". Ваша задача - создать программу,
# которая проверяет, является ли введенная дата корректной или нет.
#
# Ваша программа должна предоставить ответ "True" (дата корректна)
# или "False" (дата некорректна) в зависимости от результата проверки.

from datetime import datetime, date


def is_valid_date(date_to_prove: str) -> bool:
    try:
        datetime.strptime(date_to_prove, "%d.%m.%Y")
        return True
    except ValueError:
        return False


def main():
    date_to_prove = '31.6.2022'
    print(is_valid_date(date_to_prove))


if __name__ == '__main__':
    main()
