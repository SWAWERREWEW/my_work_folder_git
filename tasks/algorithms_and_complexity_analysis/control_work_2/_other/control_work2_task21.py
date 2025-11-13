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
def task21():
    """
Задача 21. Привидение Ваня
Ограничение по времени: 2 секунды.
Ограничение по памяти: 64 мегабайта
Привидение Ваня любит играть со своими плитками. Он любит выкладывать их в
ряд и разглядывать свое творение. Однако недавно друзья решили подшутить над Ваней и
поставили в его игровой комнате зеркало. Ведь всем известно, что привидения не
отражаются в зеркале! А плитки отражаются. Теперь Ваня видит перед собой N цветных
плиток, но не знает, какие из этих плиток настоящие, а какие — всего лишь отражение в
зеркале. Помогите Ване! Выясните, сколько плиток может быть у Вани. Ваня видит
отражение всех плиток в зеркале и часть плиток, которая находится перед ним. Часть
плиток может быть позади Вани, их он не видит.
Описание входных данных
Первая строка входного файла содержит число N (1⩽ N ⩽106) и количество
различных цветов, в которые могут быть раскрашены плитки — M (1⩽M⩽106). Следующая
строка содержит N целых чисел от 1 до M — цвета плиток
Описание выходных данных
Выведите в выходной файл все такие K, что у Вани может быть K плиток в порядке
убывания.
    """
    def quick_sort(l):
        if len(l) == 1: return l
        pivot = l[0]
        left = [x for x in l if x < pivot]
        middle = [x for x in l if x == pivot]
        right = [x for x in l if x > pivot]
        return quick_sort(left) + quick_sort(middle) + quick_sort(right)


    def find_possible_tiles(n, m, colors):
        possible_ks = []

        for k in range((n + 1) // 2, n + 1):
            if colors[:k] == list(reversed(colors[n - k:n])):
                possible_ks.append(k)

        possible_ks = quick_sort(possible_ks)[::-1]
        return possible_ks

    with open("input21.txt", "r") as f:
        content = f.read().split("\n")
        n, m = int(content[0][0]), int(content[0][1])
        colors = list(map(int, content[1]))

        result = find_possible_tiles(n, m, colors)
        answer = " ".join(map(str, result))
    with open("input21.txt", "w") as f:
        f.write(answer)

if __name__ == '__main__': task21()