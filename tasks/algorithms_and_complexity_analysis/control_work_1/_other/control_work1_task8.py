"""Студент: Коробейников Артём Юрьевич на 10 строке
Преподаватель: Кислицин Евгений Вительевич
Дисциплина: Алгоритмы и анализ сложности
Работа: Контрольная или домашняя работа 1
Варианты: 3, 4, 8, 12, 14, 17, 19, 24, 28, 30"""


def task8():
    """Задача 8. Магараджа.
Ограничение по времени: 1 с. Ограничение по памяти: 16 Mb.
Магараджа — это шахматная фигура, сочетающая возможности ферзя и коня. Таким
образом, магараджа может ходить и бить на любое количество клеток по диагонали,
горизонтали и вертикали (т.е. как ферзь), а также либо на две клетки по горизонтали и на
одну по вертикали, либо на одну по горизонтали и на две по вертикали (как конь).
Ваша задача — найти число способов расставить на доске N на N ровно K
магараджей так, чтобы они не били друг друга.
Формат входных данных:
Входной файл INPUT.TXT содержит два целых числа: N и K (1 ≤ K ≤ N ≤ 10).
Формат выходных данных:
В выходной файл OUTPUT.TXT выведите ответ на задачу.
Примеры:
INPUT.TXT 3 1 OUTPUT.TXT 9
INPUT.TXT 4 2 OUTPUT.TXT 20
INPUT.TXT 5 3 OUTPUT.TXT 48
Источник задачи: https://acmp.ru/index.asp?main=task&id_task=101"""
    with open("INPUT8.txt", "r") as f:
        content = f.read(5)
        content_list = content.split()
        content_numbers = list(map(int, content_list))
        n, k = content_numbers
        answer = "no answer"

        def safe_or_no(board, row, column, n):
            for i in range(n):
                if board[row][i] == 1 or board[i][column] == 1: return False

            for i in range(n):
                for j in range(n):
                    if board[i][j] == 1 and (abs(row - i) == abs(column - j)): return False

            knight_moves = [
                (2, 1), (2, -1), (-2, 1), (-2, -1),
                (1, 2), (1, -2), (-1, 2), (-1, -2)
            ]

            for move in knight_moves:
                r, c = row + move[0], column + move[1]
                if 0 <= r < n and 0 <= c < n and board[r][c] == 1: return False

            return True

        def rec(board, column, count, k, n, results):
            if count == k:
                results[0] += 1
                return

            if column >= n: return

            for i in range(n):
                if safe_or_no(board, i, column, n):
                    board[i][column] = 1
                    rec(board, column + 1, count + 1, k, n, results)
                    board[i][column] = 0

            rec(board, column + 1, count, k, n, results)

        def find_count(n, k):
            if k == 0: return 1
            if k > n: return 0

            board = [[0 for _ in range(n)] for _ in range(n)]
            results = [0]
            rec(board, 0, 0, k, n, results)
            return results[0]

        answer = find_count(n, k)

        print("n =", n, """
k =""", k, """
answer =""", answer)

    with open("OUTPUT8.txt", "w") as f:
        answer = str(answer)
        f.write(answer)


if __name__ == "__main__": task8()