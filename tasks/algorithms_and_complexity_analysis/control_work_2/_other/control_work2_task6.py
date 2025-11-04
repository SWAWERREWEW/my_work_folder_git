"""Студент: Коробейников Артём Юрьевич на 10 строке
Преподаватель: Кислицин Евгений Вительевич
Дисциплина: Алгоритмы и анализ сложности
Работа: Контрольная или домашняя работа 2
Варианты: 3, 6, 7, 11, 13, 18, 21, 22, 26, 28"""


def custom_summ(l):
    summ = 0
    for el in l: summ += el
    return summ


def custom_max(l):
    m = 0
    for el in l:
        if el >= m: m = el
    return m


def can_split_pages(pages, max_page_in_tom, k):
    summ = 0
    tomes_count = 1

    for page in pages:
        if summ + page > max_page_in_tom:
            tomes_count += 1
            summ = page
        else:
            summ += page

        if tomes_count > k:
            return False

    return True


def task6():
    """Задача 6. Роман в томахОграничение по времени: 1 секунда Ограничение по памяти: 16 мегабайтВ романе N глав.
В i-той главе ai страниц. Требуется издать роман в K томах так, чтобы объем самого «толстого» томабыл минимален. В
каждом томе главы располагаются по порядку своих номеров. Требуется написать программу, которая найдетколичество
страниц в самом «толстом» томе. Формат входных данных: Входной текстовый файл INPUT.TXT содержит в первойстроке число
N (1 ≤ N ≤ 100). Во второй строке через пробел записаны N чисел – количество страниц в каждой главе. Количество страниц
в романе не превышает 32767. В третьей строке записано число K (1 ≤ K ≤ N).Формат выходных данных: Выходной файл
OUTPUT.TXT должен содержать количество страниц в самом «толстом» томе. Пример
INPUT.TXT
3
1 2 1
2
OUTPUT.TXT
3

INPUT.TXT
4
1 2 1 1
3
OUTPUT.TXT
2"""
    # n = 4
    # pages = (1, 2, 1, 1)
    # k = 3
    # pages_sort = quick_sort(pages)
    # print(pages_sort)
    # answer = 0
    # for i in range(k-1):
    #     answer += pages_sort[i]
    # print(answer)


    with open('INPUT6.TXT', 'r') as f:
        n = int(f.readline().strip())
        a = list(map(int, f.readline().split()))
        k = int(f.readline().strip())

    low = custom_max(a)
    high = custom_summ(a)

    while low < high:
        mid = (low + high) // 2
        if can_split_pages(a, mid, k):
            high = mid
        else:
            low = mid + 1

    with open('OUTPUT6.TXT', 'w') as f:
        f.write(str(low))


if __name__ == "__main__": task6()