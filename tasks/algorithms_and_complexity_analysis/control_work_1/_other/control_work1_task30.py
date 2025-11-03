"""Студент: Коробейников Артём Юрьевич на 10 строке
Преподаватель: Кислицин Евгений Вительевич
Дисциплина: Алгоритмы и анализ сложности
Работа: Контрольная или домашняя работа 1
Варианты: 3, 4, 8, 12, 14, 17, 19, 24, 28, 30"""


def length(coord):
    n = 0
    numbers = [*range(coord[0], coord[1] + 1)]
    for _ in numbers: n += 1
    return n


def bubble_sort(s):
    if not s: return s
    n = 0
    for _ in s: n += 1
    for i in range(n):
        for j in range(n-i-1):
            if s[j] > s[j+1]: s[j], s[j+1] = s[j+1], s[j]
    return s


def check_entry(num, coord):
    numbers = [*range(coord[0], coord[1] + 1)]
    return num in numbers


def task30():
    """Задача 30. Вложенные отрезки
Ограничение времени: 1 секунда. Ограничение памяти: 64 МБ.
На прямой лежат n отрезков. Для каждой пары отрезков известно, что они либо не
имеют общих точек, либо все точки одного из них также принадлежат и другому отрезку.
Дано m запросов. Каждый запрос представляет собой точку на прямой. Найдите для
каждого запроса отрезок минимальной длины, которому принадлежит эта точка.
Формат входных данных:
В первой строке записано целое число n — количество отрезков (1 ≤ n ≤ 105). i-я из
следующих n строк содержит целые числа ai и bi — координаты концов i-го отрезка (1
≤ ai < bi ≤ 109). Отрезки упорядочены по возрастанию ai, а при ai = aj — по убыванию
длины. Совпадающих отрезков нет. В следующей строке записано целое число m —
количество запросов (1 ≤ m ≤ 105). В j-й из следующих m строк записано целое число cj —
координата точки (1 ≤ cj ≤ 109). Запросы упорядочены по возрастанию cj.
Формат выходных данных:
Для каждого запроса выведите номер искомого отрезка в отдельной строке. Если
точка не принадлежит ни одному отрезку, выведите «-1». Отрезки пронумерованы числами
от 1 до n в том порядке, в котором они перечислены во входных данных."""

    # test
    n = 4
    lines = [
    [1, 5],
    [3, 6],
    [7, 8],
    [14, 109]
    ]
    for lineee in lines: print(lineee)
    print()
    m = 6
    requests = [1, 4, 5, 6, 7, 100]
    for re in requests: print(re)
    print()
    answer = """
    1 1
    2 4
    2 5
    2 6
    3 7
    4 100"""

    # input datas
    n = int(input())
    if n > 105: n = 105
    elif n < 1: n = 1

    lines = []
    for _ in range(n):
        one_line = input()
        list1 = one_line.split()
        list_numbers = tuple(map(int, list1))
        lines.append(list_numbers)
    print(lines)

    m = int(input())
    if m > 105: m = 105
    elif m < 1: m = 1

    requests = []
    for _ in range(m):
        one_line = int(input())
        requests.append(one_line)
    print(requests)

    lil_req_lines = []  # Список точек или запросов и подходящих для них отрезков
    for req in requests:  # перебираем точки или запросы
        entry_lines = []  # Количество точек, содержащих точку или запрос

        for il, l in enumerate(lines):
            if check_entry(req, l): entry_lines.append([*l, il + 1])
        # Список списков содержащих три числа. Первые два это координаты концов, третий это индекс отрезка

        if entry_lines:
            entry_lines_and_length = [[*ll, length((ll[0], ll[1]))] for ll in entry_lines]
            # Список из списков отрезков и их длин
            # Теперь в списке 4 числа. Четвёртое число это длинна отрезка

            min_line = [1, 2, 1, 110] # Отрезок с минимальной длинной

            # Идёт перебор.
            # Подбираем список с минимальным четвёртым числом
            for lll in entry_lines_and_length:
                if min_line[3] > lll[3]: min_line = lll
            lil_req_lines.append([min_line[2], req])
    answer = ''
    for ii, ss in enumerate(lil_req_lines):
        if ss == lil_req_lines[-1]: answer += str(ss[0]) + ' ' + str(ss[1])
        else: answer += str(ss[0]) + ' ' + str(ss[1]) + '\n'
    print(answer)


if __name__ == "__main__": task30()