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
def task28():
    n = 11
    s = "abracadabra"
    t = "racadabraab"

    count_cycle = 0
    lil_s = list(s)
    lil_t = list(t)
    limit = 0
    while lil_t != lil_s and limit <= n:
        limit += 1
        count_cycle += 1
        lil_t = [lil_t[-1]] + lil_t
        lil_t.pop()
    print("".join(lil_t))
    answer = n - count_cycle
    print(answer)


if __name__ == '__main__': task28()