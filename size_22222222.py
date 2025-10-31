"""Для каждого из участков выведите расстояние до ближайшего нуля. Числа выводите в одну строку, разделяя их
пробелами.

длина улицы – n (1 ≤ n ≤ 106)

номера домов и обозначения пустых участков на карте (нули). Гарантируется, что в последовательности есть хотя бы один
ноль. Номера домов (положительные числа) уникальны и не превосходят 10^9.
"""


# Функция для создания списка случайных координат
# def rdc(wid_p: int, hei_p: int, coord_for_obej=None, obej=None) -> list:
#     """Возвращает список из двух случайных координат в диапазоне от размеров текстового поля до размеров экрана
#     минус размер объекта, для которого нужно подобрать случайные координаты"""
#     coord = [randint(0, (const.wid - wid_p)), randint(const.size_title, (const.hei - hei_p))]
#     if not (obej is None and coord_for_obej is None):
#         red_in_blue = True
#         while red_in_blue:
#             # if (coord[0] < (obej.x + obej.wid) and coord[0] > obej.x) :
#             #     coord = [randint(0, (const.wid - wid_p)), randint(const.size_title, (const.hei - hei_p))]
#             condition1 = (coord[0] + coord_for_obej.wid > obej.x) and (coord[0] + coord_for_obej.wid < obej.x + obej.wid
#             and coord[1] + coord_for_obej.hei > obej.y and coord[1] + coord_for_obej.hei < obej.y + obej.hei)
#             condition2 = ()
#
#             if:
#                 coord = [randint(0, (const.wid - wid_p)), randint(const.size_title, (const.hei - hei_p))]
#             else:
#                 red_in_blue = False
#     print(coord, obej.x, obej.y)
#     return coord
# # Функция для создания списка случайных координат
# from random import randint
#
# red_squ = [randint(0, 50), randint(0, 50)]
# red_squ_size = 50
#
# blue_squ = [300, 300]
# blue_squ_size = 50
#
# red_in_squ = True
#
# while red_in_squ:
#     for n in range(red_squ[0], red_squ[1]+1):
#         if ((blue_squ[0] == n or blue_squ[1] == n)
#             and
#             (blue_squ[0] + blue_squ_size == n or blue_squ[1] + blue_squ_size == n)):
#                 red_squ = [randint(0, 50), randint(0, 50)]
#         else:
#             red_in_squ = False
#
# print(red_squ[0], red_squ[0] + red_squ_size, red_squ[1], red_squ[1] + red_squ_size)
# print(blue_squ[0], blue_squ[0] + blue_squ_size, blue_squ[1], blue_squ[1] + blue_squ_size)

































# def we(): return 6
# r = {"x": 4, "y": 5, "we": we}
# print(r["x"])
# print(r["y"])
# print(r["we"]())
# luil = [[[5.5, 4],[3, 3]], ["23423"]]
# print(luil[0][0][0])
# y = lambda x: x**2
# print(y(4))
#
# from typing import Callable, Any
#
# Validator = Callable[[Any], bool]
#
#
# def validate_data(validator: Validator, data: Any) -> bool:
#     return validator(data)
#
#
# def is_positive_number(data: int) -> bool:
#     return data > 0
#
#
# def is_string_longer_than_five(data: str) -> bool:
#     return len(data) > 5
#
#
# print(validate_data(is_positive_number, 10))  # True
# print(validate_data(is_positive_number, -5))  # False
# print(validate_data(is_string_longer_than_five, "abcdefg"))  # True
# print(validate_data(is_string_longer_than_five, "abc"))  # False
#
# Validator = Callable[[Any], bool]
#
#
# def validate_data(validator: Validator, data: Any) -> bool:
#     return validator(data)
#
#
# def is_positive_number(data: int) -> bool:
#     return data > 0
#
#
# validate_data(is_positive_number, 4)
#
#
# def quick_sort(s):
#     if len(s) <= 1:
#         return s
#     pivot = s[len(s) // 2]
#     left = [x for x in s if x < pivot]
#     middle = [x for x in s if x == pivot]
#     right = [x for x in s if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)
#
#
# print(quick_sort([3, 4, 5, 1, 3, 4, 65, 22, 0]))

def hrenb(s, lil=[]):  # Это неправильно
    lil.append(s)
    return lil

l = hrenb(1)
print(l)
l = hrenb(2)
print(l)