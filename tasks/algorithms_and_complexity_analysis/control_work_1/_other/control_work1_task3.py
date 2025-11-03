"""Студент: Коробейников Артём Юрьевич на 10 строке
Преподаватель: Кислицин Евгений Вительевич
Дисциплина: Алгоритмы и анализ сложности
Работа: Контрольная или домашняя работа 1
Варианты: 3, 4, 8, 12, 14, 17, 19, 24, 28, 30"""


def task3(data) -> str:
    """Задание 3: Симметрическая разность.
Ограничение по времени: 2 с. Ограничение по памяти: 64 Mb.
На вход подается множество чисел в диапазоне от 1 до 20000, разделенных
пробелом. Они образуют множество А. Затем идет разделитель – число 0 и на вход подается
множество чисел В, разделенных пробелом, 0 – признак конца описания множества (во
множество не входит). Необходимо вывести множество АΔВ – симметрическую разность
множеств А и В в порядке возрастания элементов. В качестве разделителя используйте
пробел. В случае, если множество пусто, вывести 0.
Формат входных данных:
1 2 3 4 5 0 1 7 5 8 0
Формат выходных данных:
2 3 4 7 8
Примеры:
Стандартный ввод
1 2 6 8 7 3 0 4 1 6 2 3 9 0
Стандартный вывод
4 7 8 9
Замечание. Для вывода можно использовать любой алгоритм сортировки."""
    print("Входные данные", data)
    print()
    result1 = []
    result2 = []
    i = 0
    while data[i] != 0:
        result1.append(data[i])
        i += 1
    i += 1
    while data[i] != 0:
        result2.append(data[i])
        i += 1
    print("Первое множество", result1)
    print("Второе множество", result2)
    print()

    result1_len = 0
    for _ in result1: result1_len += 1
    result2_len = 0
    for _ in result2: result2_len += 1

    similarities = []
    for i in range(result1_len):
        for j in range(result2_len):
            if result1[i] == result2[j]:
                similarities.append(result1[i])

    print("Одинаковые числа в двух множествах", similarities)
    print()
    difference = []
    for r_task3 in data:
        if r_task3 in similarities or r_task3 == 0: continue
        else: difference.append(r_task3)

    print("Симметричная разность", difference)
    print()
    minus = difference if difference != [] else 0

    sort_data = heapsort(minus) if minus != 0 else 0
    sort_data_str = map(str, sort_data)
    sort_str = " ".join(sort_data_str)

    return sort_str


def heapsort(heap):
    n = len(heap)

    for i in range(n // 2 - 1, -1, -1): heapify(heap, n, i)

    for i in range(n - 1, 0, -1):
        heap[0], heap[i] = heap[i], heap[0]
        heapify(heap, i, 0)

    return heap


def heapify(heap, n, i):
    root = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and heap[left] > heap[root]: root = left

    if right < n and heap[right] > heap[root]: root = right

    if root != i:
        heap[i], heap[root] = heap[root], heap[i]
        heapify(heap, n, root)

"""heap = [1, 58, 56, 22, 10]
head_sorted = heapsort(heap)
print("Отсортированный массив:", head_sorted) # [1, 10, 22, 56, 58]"""


def main():
    """Формат входных данных:
1 2 3 4 5 0 1 7 5 8 0
Формат выходных данных:
2 3 4 7 8
Примеры:
Стандартный ввод
1 2 6 8 7 3 0 4 1 6 2 3 9 0
Стандартный вывод
4 7 8 9"""
    set_input = """
    1 2 6 8 7 3 0 4 1 6 2 3 9 0
    """
    set_input = input()
    set_input_split = set_input.split()
    set_numbers = map(int, set_input_split)
    data = tuple(set_numbers)

    answer = task3(data)

    print("Выходные и отсортированные данные", answer)


if __name__ == "__main__": main()

