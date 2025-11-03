"""Студент: Коробейников Артём Юрьевич на 10 строке
Преподаватель: Кислицин Евгений Вительевич
Дисциплина: Алгоритмы и анализ сложности
Работа: Контрольная или домашняя работа 2
Варианты: 3, 6, 7, 11, 13, 18, 21, 22, 26, 28"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def intersect_sorted_lists(list1, list2):
    i = j = 0
    common_elements = []

    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            common_elements.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1

    return common_elements


def task3():
    """Задача 3. Пересечение множеств
Ограничение по времени: 2 секунды
Ограничение по памяти: 64 мегабайта
Задано 2 ≤ N ≤ 1000 множеств из 3 ≤ M ≤ элементов, значения которых могут
находиться в диапазоне от -2000000000 до 2000000000. Значения каждого множества
задаются в произвольном порядке. Гарантируется, что для одного множества все
задаваемые значения различные.
Требуется найти наибольший размер множества, получаемого при пересечении
какой-либо из пар из заданных множеств.
Формат входных данных:
N M
A_1[1] A_1[2] … A_1[M]
A_2[1] A_2[2] … A_2[M]
…
A_N[1] A_N[2] … A_N[M]
Формат выходных данных:
Одно целое число.
Примеры:
Стандартный ввод
3 4
9 7 1 8
5 7 6 3 этот список
5 9 8 6 и этот список имеют
Стандартный вывод
2 общих элемента, а именно 5 и 6

Стандартный ввод
4 5
-2 6 8 4 -1 этот список имеет
5 3 10 -5 -1
7 8 -5 -1 -2 с этим списком
-1 8 4 9 0
Стандартный вывод
3 общих элемента, а именно -2 -1 и 8"""
    n_and_m = list(map(int, input().split()))
    n, m = n_and_m[0], n_and_m[1]

    sorted_sets = []
    for _ in range(n):
        unsorted_values = list(map(int, input().split()))
        sorted_values = quick_sort(unsorted_values)
        sorted_sets.append(sorted_values)

    max_count = 0

    for i in range(n):
        for j in range(i + 1, n):
            similarities = intersect_sorted_lists(sorted_sets[i], sorted_sets[j])
            count = len(similarities)
            max_count = max_count if max_count >= count else count

    print(max_count)


if __name__ == "__main__": task3()