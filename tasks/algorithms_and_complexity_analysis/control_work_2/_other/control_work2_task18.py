from time import time


def time_of_function(function_for_check):
    def wrapper():
        start_time = time()
        result = function_for_check()
        end_time = round(time() - start_time, 6)
        print(f"Время выполнения {end_time} секунд")
        return result
    return wrapper


@time_of_function
def task18():
    import sys
    INITIAL_CAPACITY = 100003

    class MyHashTable:
        def __init__(self, capacity):
            self.capacity = capacity
            self.table = [[] for _ in range(self.capacity)]

        def _get_hash(self, key):
            return key % self.capacity

        def put(self, key, value):
            hash_index = self._get_hash(key)
            bucket = self.table[hash_index]

            for i, pair in enumerate(bucket):
                if pair[0] == key:
                    bucket[i][1] = value
                    return

            bucket.append([key, value])

        def get(self, key):
            hash_index = self._get_hash(key)
            bucket = self.table[hash_index]

            for pair in bucket:
                if pair[0] == key:
                    return pair[1]

            return "None"

        def delete(self, key):
            hash_index = self._get_hash(key)
            bucket = self.table[hash_index]

            for i, pair in enumerate(bucket):
                if pair[0] == key:
                    value = pair[1]
                    del bucket[i]
                    return value
            return "None"

    n = int(input())

    hash_table = MyHashTable(INITIAL_CAPACITY)

    results = []
    for _ in range(n):
        command_parts = input().split()
        command = command_parts[0]
        key = int(command_parts[1])

        if command == "put":
            value = int(command_parts[2])
            hash_table.put(key, value)
        elif command == "get":
            result = hash_table.get(key)
            results.append(str(result) + "\n")
        elif command == "delete":
            result = hash_table.delete(key)
            results.append(str(result) + "\n")

    print("".join(results))

if __name__ == '__main__': task18()