"""28 30"""


def task24():
    """Задача 24. Очередь с минимумом
Реализуйте работу очереди. В дополнение к стандартным операциям очереди,
необходимо также отвечать на запрос о минимальном элементе из тех, которые сейчас
находится в очереди. Для каждой операции запроса минимального элемента выведите ее
результат.
На вход программе подаются строки, содержащие команды. Каждая строка
содержит одну команду. Команда — это либо «+ N», либо «−», либо «?». Команда «+ N»
означает добавление в очередь числа N, по модулю не превышающего 109. Команда «−»
означает изъятие элемента из очереди. Команда «?» означает запрос на поиск
минимального элемента в очереди.
Формат входных данных:
В первой строке содержится M (1≤M≤106) — число команд. В последующих строках
содержатся команды, по одной в каждой строке.
Формат выходных данных:
Для каждой операции поиска минимума в очереди выведите её результат.
Результаты должны быть выведены в том порядке, в котором эти операции встречаются во
входном файле. Гарантируется, что операций извлечения или поиска минимума для пустой
очереди не производится.
"""


    def bubble_sort(s):
        n = len(s)
        s_list = list(map(int, list(s)))
        for i in range(n):
            for j in range(n-i-1):
                if s_list[j] < s_list[j + 1]: s_list[j], s_list[j + 1] = s_list[j + 1], s_list[j]
        return s_list[::-1]


    m = int(input())
    lilst_command = []
    for _ in range(m):
        command = input()
        command_split = command.split()
        if len(command_split) == 2: lilst_command.append([command[0], int(command[2])])
        else: lilst_command.append(command)
    print(lilst_command)

    lilst_elem = []
    for c in lilst_command:
        if c[0] == "-" and len(lilst_elem) > 0:
            deleted = lilst_elem.pop(0)
            print(deleted, "was deleted")
        elif c[0] == "+":
            lilst_elem.append(c[1])
            print(c[1], "was been taken")
        elif len(lilst_elem) > 0:
            lilst_elem = bubble_sort(lilst_elem)
            print(lilst_elem[0], "is minimum.")


if __name__ == "__main__": task24()