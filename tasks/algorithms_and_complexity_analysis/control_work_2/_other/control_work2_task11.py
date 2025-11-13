"""Студент: Коробейников Артём Юрьевич на 10 строке
Преподаватель: Кислицин Евгений Вительевич
Дисциплина: Алгоритмы и анализ сложности
Работа: Контрольная или домашняя работа 2
Варианты: 3, 6, 7, 11, 13, 18, 21, 22, 26, 28"""
import time


def time_of_function(funсtion_for_check):
    def wrapper():
        start_time = time.time()
        result = funсtion_for_check()
        end_time = round(time.time() - start_time, 6)
        print(f'Время выполнения {end_time} секунд')
        return result
    return wrapper


def length(l):
    n = 0
    for _ in l: n += 1
    return n


def count_often(requests):
    frequencies = {}
    for r in requests:
        if r in frequencies: frequencies[r] += 1
        else: frequencies[r] = 1
    return frequencies


def find_rarelly_element_in_cache(cache, future_requests):
    frequencies = count_often(future_requests)
    rarest_item = None
    lowest_frequency = 999999999999
    for item in cache:
        count = frequencies.get(item, 0)
        if count < lowest_frequency:
            rarest_item = item
            lowest_frequency = count
    return rarest_item

@time_of_function
def task11():
    data = """
5 15
3
1
4
1
5
9
2
6
5
3
5
8
7
9
3    """
    # # Получаем и обрабатываем данные
    # first_str = input("str two numbers:_")
    # n_and_m_list = first_str.split()
    # n, m = int(n_and_m_list[0]), int(n_and_m_list[1])
    # requests_lil = []
    # for _ in range(m):
    #     line = int(input("int:_"))
    #     requests_lil.append(line)

    data_split = data.split()
    data_lil = list(map(int, data_split))
    n, m = data_lil[0], data_lil[1]
    requests_lil = data_lil[2:]

    cache = []
    answer = 0

    for i, r in enumerate(requests_lil):
        if not r in cache:
            if length(cache) >= n:
                element_to_remove = find_rarelly_element_in_cache(cache, requests_lil[i:])
                cache.remove(element_to_remove)

            cache.append(r)
            answer += 1

    print(answer)


if __name__ == '__main__': task11()