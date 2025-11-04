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

    def is_palindrome(s):
        return s == s[::-1]

    def find_minimum_right_half_to_make_palindrome(s):
        n = len(s)
        for i in range(n):
            right_half = s[i:]

            result = s + right_half[::-1]

            if is_palindrome(result):
                return result
        return None

    s1 = input()

    answer = find_minimum_right_half_to_make_palindrome(s1)
    print(answer)

if __name__ == '__main__': task26()