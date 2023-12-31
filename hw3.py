# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
#
# Под "успешной расстановкой ферзей" в данном контексте подразумевается такая расстановка ферзей на шахматной доске,
# в которой ни один ферзь не бьет другого.
# Другими словами, ферзи размещены таким образом, что они не находятся на одной вертикали, горизонтали или диагонали.
#
# Список из 4х комбинаций координат сохраните в board_list. Дополнительно печатать его не надо.

# [[(1, 4), (2, 7), (3, 1), (4, 8), (5, 5), (6, 2), (7, 6), (8, 3)],
# [(1, 5), (2, 3), (3, 8), (4, 4), (5, 7), (6, 1), (7, 6), (8, 2)],
# [(1, 3), (2, 6), (3, 8), (4, 2), (5, 4), (6, 1), (7, 7), (8, 5)],
# [(1, 6), (2, 1), (3, 5), (4, 2), (5, 8), (6, 3), (7, 7), (8, 4)]]
from random import randint


def is_attacking(q1: tuple[int, int], q2: tuple[int, int]) -> bool:
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])


def check_queens(queens: list[tuple[int, int]]) -> bool:
    for queen in queens:
        for q in queens:
            if q != queen:
                if is_attacking(queen, q):
                    return False
    return True


def generate_board():
    board = []

    for i in range(1, 9):
        queen = (i, randint(1, 8))
        board.append(queen)
    return board


def generate_boards():
    count = 0
    board_list = []
    while count < 4:
        board = generate_board()
        if check_queens(board):
            count += 1
            board_list.append(board)
    return board_list


def main():
    print(generate_boards())


if __name__ == '__main__':
    main()
