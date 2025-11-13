from time import time


def time_of_function(funcion_for_check):
    def wrapper():
        start_time = time()
        result = funcion_for_check()
        end_time = round(time() - start_time, 6)
        print(f"Время выполнения {end_time} секунд")
        return result
    return wrapper


@time_of_function
def task26():
    """
Задача 26. Палиндром. Он же палиндром.
Ограничение времени: 1.0 секунды
Ограничение памяти: 64 МБ
Под словом будем понимать некоторую непустую последовательность символов a1a2…an. Палиндромом будем называть такое
слово a1a2…an, которое читается одинаково как слева направо, так и справа налево (т.е. что a1a2…an = anan−1…a1).
Если S1 = a1a2…an и S2 = b1b2…bm, то тогда S1S2 = a1a2…anb1b2…bm. Вам дано некоторое слово S1. Ваша задача — найти
такое непустое слово S2 минимальной длины, что S1S2 — палиндром.
Исходные данные
В первой строке записано S1 (оно может состоять только из символов латиницы). Гарантируется, что длина S1 не
превышает 10000 символов.

Результат
Выведите S1S2

Примеры

исходные данные
No
результат
NoN

исходные данные
OnLine
результат
OnLineniLnO

исходные данные
AbabaAab
результат
AbabaAababA
    """

    s1 = input()

    answer = 'not polindrom'
    n = len(s1)

    for i in range(n):
        right_half = s1[i:]

        result = s1 + right_half[::-1]

        if s1 == s1[::-1]:
            answer = result
            break

    print(answer)

if __name__ == '__main__': task26()