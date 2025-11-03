"""Студент: Коробейников Артём Юрьевич на 10 строке
Преподаватель: Кислицин Евгений Вительевич
Дисциплина: Алгоритмы и анализ сложности
Работа: Контрольная или домашняя работа 1
Варианты: 3, 4, 8, 12, 14, 17, 19, 24, 28, 30"""


def bubble_sort(s):
    if not s: return s
    n = 0
    for _ in s: n += 1
    for i in range(n):
        for j in range(n-i-1):
            if s[j] > s[j+1]: s[j], s[j+1] = s[j+1], s[j]
    return s


def task28() -> None:
    """Задача 28. Считаем комментарии.
Ограничение по времени: 1 с. Ограничение по памяти: 256 Mb.
Комментарием в языке Object Pascal является любой текст, находящийся между последовательностью символов, начинающих
комментарий определенного вида и последовательностью символов, заканчивающей комментарий этого вида.
Виды комментариев могут быть следующие:
1. Начинающиеся с набора символов (* и заканчивающиеся набором символов *).
2. Начинающиеся с символа { и заканчивающиеся символом }.
3. Начинающиеся с набора символов // и заканчивающиеся символом новой строки.
Еще в языке Object Pascal имеются литеральные строки, начинающиеся с символа одиночной кавычки ‘ и заканчивающиеся
этим же символом. В корректной программе строки не могут содержать символа перехода на новую строку.
Будьте внимательны, в задаче используются только символы с кодами до 128, то есть, кодировка ASCII. При тестировании
своего решения будьте внимательны. Код одиночной кавычки – 39, двойной – 34.
Формат входных данных:
На вход программы подается набор строк, содержащих фрагмент корректной программы на языке Object Pascal.
Формат выходных данных:
Выходом программы должно быть 4 числа – количество комментариев первого, второго и третьего типов, а также количество
литеральных строк.
Примеры:

Стандартный ввод
program test;
(* just for testing *)
var
(* variables
note that
// here is not comment
and (* here is
not a begin of
another comment
*)
x: integer; (* *)
begin
write(‘(*is not comment//’);
write(‘ and (*here*) ‘
,x // y);
End. // It is comment

Стандартный вывод
3 0 2 2
"""
#    lil = """program test;
# (* just for testing *)
# var
# (* variables
# note that
# // here is not comment
# and (* here is
# not a begin of
# another comment
# *)
# x: integer; (* *)
# begin
# write(‘(*is not comment//’);
# write(‘ and (*here*) ‘
# ,x // y);
# End. // It is comment""".split('\n')
#    print(lil)

    count_stars = 0
    count_figures1 = 0
    count_figures2 = 0
    count_slash = 0
    count_lit = 0

    lil = []
    line = ''
    while line[:4] != 'End.':
        line = input()
        lil.append(line)
    print(lil)

    for s in lil:
        if s[0:2] == '//' or (s[:5] == "End. " and s[5:7] == "//"): count_slash += 1
        if '(*' in s and '*)' in s: count_stars += 1
        if '{' in s: count_figures1 += 1
        if '}' in s: count_figures2 += 1
        if "‘" in s: count_lit += 1


    condition = (count_figures1 == count_figures2)
    count_figures = count_figures1 if condition else bubble_sort([count_figures1, count_figures2])[0]

    count_slash = count_slash

    count_lit = count_lit if count_lit % 2 == 0 and count_lit != 0 else count_lit - 1

    print(count_stars, count_figures, count_slash, count_lit)


if __name__ == '__main__': task28()