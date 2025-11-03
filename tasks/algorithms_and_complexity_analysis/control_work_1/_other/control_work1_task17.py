"""Студент: Коробейников Артём Юрьевич на 10 строке
Преподаватель: Кислицин Евгений Вительевич
Дисциплина: Алгоритмы и анализ сложности
Работа: Контрольная или домашняя работа 1
Варианты: 3, 4, 8, 12, 14, 17, 19, 24, 28, 30"""


def task17():
    """Задача 17. Внешняя сортировка.
Ограничение по времени: 2 с. Ограничение по памяти: 2 Mb.
В файле «input.txt» содержатся строки символов, длина каждой строки не превышает
10000 байт. Файл нужно отсортировать в лексикографическом порядке и вывести результат
в файл «output.txt». Вот беда, файл занимает много мегабайт, а в Вашем распоряжении
оказывается вычислительная система с очень маленькой оперативной памятью. Но файл
должен быть отсортирован!
Примеры:
input.txt
qwertyuiopasdffghhj
qpoiuytredgfhfd
asdfghjjklvcvx
alkjghcdysdfgsr
pquytrgsdjdsa
akjhfgdghshhfuushvdfs
output.txt
akjhfgdghshhfuushvdfs
alkjghcdysdfgsr
asdfghjjklvcvx
pquytrgsdjdsa
qpoiuytredgfhfd
qwertyuiopasdffghhj"""
    with open("input17.txt", "r") as f:
        content = f.read()

        def bubble_sort(s):
            symbols = list(s)
            length = 0
            for _ in symbols: length += 1

            for i in range(length):
                for j in range(length-i-1):
                    if symbols[j] > symbols[j + 1]:
                        symbols[j], symbols[j + 1] = symbols[j + 1], symbols[j]

            return "".join(symbols)

        answer = ""
        lines = content.split()
        leng = 0
        for _ in lines: leng += 1
        for l in range(leng):
            if l == leng-1:
                answer += bubble_sort(lines[l])
            else:
                answer += bubble_sort(lines[l]) + "\n"

    with open("output17.txt", "w") as f:
        answer = str(answer)
        f.write(answer)


if __name__ == "__main__": task17()