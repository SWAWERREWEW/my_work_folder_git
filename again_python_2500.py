from random import shuffle
import some_file


def main():
    print("https://www.youtube.com/watch?v=qJwkaKgNxfE&list=PLA0M1Bcd0w8yWHh2V70bTtbVxJICrnJHd&index=3")

    r"""ins.bat:
    python -m venv .venv
    call .\venv\Scripts\activate.bat
    python -r req.txt / python main.py / pip install pygame / pip install book
    deactivate
    
    act.bat:
    call .\.venv\Scripts\activate.bat
    python main.py
    deactivate
    
    req.txt:
    pygame==2.4.0"""

    a = 7
    r"операнд слева = операнд справа"
    r"Присваивание"
    a = 6.7
    "Переприсваивание"
    print(a)

    lil = ["hu_tao", "shenhe", "xilonen", "mech", "luk", "knijka"]
    shuffle(lil)
    print(lil[0])

    b = c = d = 1
    r, t = 1, "▲"
    print(b, c, d)
    print(id(b), id(c), id(d), id(r), type(id(t)))
    "Для всех он одинаков, так как и значение одинаково."
    """
    
    7*3 = 21
    21 - 17 = 4
    
    -17 % 8 = ?
    8 * 2 = 16 > 17 => 8 * 3 = 24 > 17 =>
    24 - 17 = 7 =>
    -17 % 8 = 7
    
    17 % -8 = ?
    8 * 2 = 16 > 17 => 8 * 3 = 24 > 17 =>
    24 - 17 = 7 & -8 =>
    17 % -8 = -7
    
    print(6, 2, sep="  |  ")
    """

    kapsula = r"C:\python\project\folder\file.file"

    a = "C:\\python\\project\\folder\\file.file"

    msg = "lalalal {0} and hahaha {1}".format(kapsula, a)
    print(msg)

    lil1 = [2, 3]
    lil2 = lil1
    lil1 = 3
    print(lil1)
    print(lil2)

    testr = 3
    b = 9 if testr == 2 else "Ahaha"
    print(b)
    "Гениально"
    for x in [1, 2, 3, 4, 5]:
        x = 0
    print(x)
    "print(list(range(-10, -5, -2)))   # вообще пустой списак"
    words = ['python', 'дай', 'мне', 'силы', 'пройти', 'этот', 'курс', 'до', 'конца']
    s = ''
    for w in words:
        if w == words[0]:
            s += w
        else:
            s += ' ' + w
    print(s)
    s = ''
    fl_first = True
    for w in words:
        s += ('' if fl_first else ' ') + w
        fl_first = False
    print(s)
    "Но быстрее будет работать следующий вариант с lstrip() "
    s = ''
    for w in words:
        s += ' ' + w
    print(s.lstrip())
    "Но самый быстрый способ это с join"
    print(' '.join(words), "join")

    dgis = [4, 3, 100, -53, -30, 1, 34, -8]

    for i, d in enumerate(dgis):
        if 10 <= abs(d) <= 99:
            dgis[i] = 0
    print(dgis)

    "Итерируемый объект можно создать с помощью iter()"
    it = iter([5])
    "Чтобы его перебирать нужно использовать функцию next. Только для iter() можно использовать функцию next() ."
    print(next(it))

    "Генератор генераторов списка. Список чисел в двоичной системе счисления."
    a = [str(i) + str(j) + str(k)
         for i in range(2)
         for j in range(2)
         for k in range(2)]
    print(a)
    "Таблица умножения"
    math_table = [f"{str(i)} * {str(j)} = {str(i * j)}"
                  for i in range(10)
                  for j in range(10)
                  if i != 0 and j != 0 and i != 1 and j != 1]
    "Плохая попытка сделать таблицу умножения"
    indd = math_table[0][0]
    for i, m in enumerate(math_table):
        if indd != m[0]:
            indd = m[0]
            print(math_table[i])
        elif i == len(math_table) - 1:
            print(math_table[i])
        else:
            print(math_table[i], end="   ")

    print(math_table[0])
    lil_two = [math_table[i] for i in range(len(math_table)) if math_table[i][0] == math_table[0][0]]
    print(lil_two, "two")

    math_table_save = math_table
    lil_table = []
    for cr in range(10):
        rt = 2
        for i, m in enumerate(math_table_save):
            if m[0] == str(rt):
                rt += 1
                if rt == 10:
                    rt = 2
                lil_table.append(m)
                math_table_save.pop(i)
    for irt in range(len(lil_table)):
        print(lil_table[irt])
    print(lil_table)

    indde = 0
    for c in range(10):
        for ii in range(8):
            print(lil_table[indde], end="   ")
            indde += 1
            if indde >= len(lil_table):
                break
        if indde >= len(lil_table):
            break
        print()
    print()

    "Успешная попытка сделать таблицу умножения"
    math_table = [f"{str(i)} * {str(j)} = {str(i * j)}"
                  for i in range(2, 10)
                  for j in range(2, 10)]
    print(math_table)

    dodo = {}
    dodind = 2
    while dodind <= 9:
        dodo[str(dodind)] = []
        for i, p in enumerate(math_table):
            if str(dodind) == p[0]:
                dodo[str(dodind)].append(math_table[i])
        dodind += 1

    s = ""
    for i, es in enumerate(dodo):
        for e in dodo:
            if " " in dodo[e][i][-2]:
                s += dodo[e][i] + "    "
            elif dodo[e][i][0] != "9":
                s += dodo[e][i] + "   "
            else:
                s += dodo[e][i]
        s += """
"""
    print()
    print(s)

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    a = [x
         for row in matrix
         for x in row
         ]
    print(a)
    print([[a for a in range(3)] for _ in range(4)])
    print([[a for _ in range(2)] for _ in range(2)])  # ???
    print()
    number_lil_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    number_lil_2 = [[x ** 2 for x in row] for row in number_lil_1]
    number_lil_3 = [x ** 2 for row in number_lil_1 for x in row]
    print(number_lil_1)
    print(number_lil_2)
    print(number_lil_3)
    print("Транспонирование матрицы")
    number_lil_4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    number_lil_5 = [[row[i] for row in number_lil_4] for i in range(len(number_lil_4[0]))]
    print(number_lil_4)
    print(number_lil_5)
    print()
    number_lil_6 = [u ** 2 for u in [x + 1 for x in range(5)]]
    print(number_lil_6)
    print("Функция dict()")
    number_lil_7 = [[2, "loh"], [3, "meh"]]
    number_lil_8 = dict(number_lil_7)
    print(number_lil_7)
    print(number_lil_8)
    print("Функция del")
    del number_lil_8[2]
    print(number_lil_8)
    print("Функция fromkeys")
    number_lil_9 = ["+7", "+6"]
    print(number_lil_9)
    number_lil_10 = dict.fromkeys(number_lil_9)
    print(number_lil_10)
    number_lil_10 = dict.fromkeys(number_lil_9, "koziavki")
    print(number_lil_10)
    print("Функция clear()")
    number_lil_10.clear()
    print(number_lil_10)
    print("Функция copy(). Python работает так, что в нём копию можно создать только с помощью этой функции.")
    number_lil_10 = dict.fromkeys(number_lil_9, "koziavki")
    number_lil_11 = number_lil_10.copy()
    number_lil_11["versios"] = "copied"
    print(number_lil_10)
    print(number_lil_11)
    print("Функция get(key, значение_при_ошибке). Просто получаем значение по ключу. При ошибке возвращает None.")
    print(number_lil_11.get("version", "Oops"))
    print("""Функция setdefault(key, value). Возвращает значение по ключу, но если его нет, то добавляет это
значение None по этому ключу или добавит указаное значечние по этому ключу.          """)
    print(number_lil_11.setdefault("versioгнеоноs", "UUAAAAAAAA"))
    print(number_lil_11)
    print("Функция pop(key, else_value) . Удаляет указаное значение или возвращает значение указаное вторым аргументом")
    print("""Функция popitem удаляет последнее значение""")
    print(number_lil_11.items())
    print(number_lil_11)
    print("""Можно объединить словари. **d или d | d2 . Но вторая запись более новая и не работает на старых
интепретаторах""")
    number_lil_12 = {"uuu": 3333, "nenag": 333224235}
    number_lil_13 = {**number_lil_10, **number_lil_11, **number_lil_12}
    print(number_lil_13)
    print("Картежи занимают меньше памяти. __sizeof__() возвращает занимаемое количество памяти в байтах.")
    number_parem_1 = 1,
    number_parem_2 = (3, 4)
    print(number_parem_1)
    print(number_parem_2)
    print(number_parem_1.__sizeof__(), number_parem_1)
    print(number_parem_2.__sizeof__(), number_parem_2)
    print("Картежи можно объединять плюсикоми. (То есть картежи вроде менять нельзя, а объединять можно почемуто.)")
    number_parem_3 = ()
    print(number_parem_3, end=" + ")
    number_parem_4 = (1,)
    print(number_parem_4, end=" = ")
    number_parem_3 = number_parem_3 + number_parem_4
    print(number_parem_3)
    number_parem_5 = (1, 2)
    print(number_parem_5, end=" + ")
    number_parem_6 = (1, 4)
    print(number_parem_6, end=" = ")
    number_parem_5 = number_parem_5 + number_parem_6
    print(number_parem_5)
    print(r"""Картеж можно превратить в список list(tuple(1,)) = [1]. Списки в картеже можно менять, хотя картежи менять
нельзя""")
    print(r"""lil.count("s") возвращает количество найденных совпадений с объектом в аргументе функции.""")
    print(r"""lil.index("s", 2, 3) возвращает индекс первого совпадения после индекса, который указан во втором
аргументе и до индекса, который указан в третьем аргументе.""")
    print(r"""set() множество это неупорядоченный список уникальных неизменяемых значений. loh = {1, 2, 3, 3}""")
    number_parem_7 = {1, 2, 3, 3}
    print(number_parem_7)
    print(r"""С помощью list(set(lil)) можно сделать обычный список, но из уникальных значений.""")
    number_parem_8 = [1, 2, 3, 3, 54, 5, 5, 56, 56, 57, 54, 57, 87, 37, 5487, 47, 5, 74, 7]
    number_parem_9 = list(set(number_parem_8))
    print(number_parem_9)
    print(r"""Функция add добавит элемент в множество""")
    number_parem_7.add(54)
    print(number_parem_7)
    print(
        r"""sett.update Добавит несколько значений. В аргументе нужен список. Если будет строка, то добавятся буквы.""")
    number_parem_7.update([67, 43, 100])
    print(number_parem_7)
    print(r"""sett.discard("element") и sett.remove("element") удаляет элемент. Но remove возвращает ошибку, а discard
ничего не возвращает. pop() удаляет первый элемент, но тоже выдаст ошибку""")
    number_parem_7.update([67, 43, 100])
    print(number_parem_7)
    number_parem_10 = {1, 2, 3}
    number_parem_11 = {1, 4, 5, 6}
    print(number_parem_10 & number_parem_11, r"""пересечение
set1 = set1 & set2
set1 &= set2
set3 = set1.intersection(set2)
set1.intersection_update(set2) множество set1 изменится

объединение
set1 = set1 | set2
set1 |= set2
set3 = set1.union(set2)

Вычитание множеств
set3 = set1 - set2
set1 -= set2

Симетричная разность (Общие элементы исключаются, остаются только несовпадающиеся элементы)
set3 = set1 ^ set2

Сравнение множества
{3, 2, 1} == {1, 2, 3}  # True
set1 != set2
{1, 2, 3} < {1, 2, 3, 4, 5, 6}  # True
set1 > set2
set1 >= set2
set1 <= set2
""")
    print("Генераторы множеств и словарей.")
    print("... Аналогично")

    def five() -> int:
        return 5

    print(five.__sizeof__())
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    print(five.__sizeof__())
    print(one + two + three + four + five + six + seven + eight + nine + ten)
    def min_heu(lil_in_min_heu: list) -> int:
        mimi = 9999999999999999999999999999
        for i_in_min_heu in lil_in_min_heu:
            mimi += i_in_min_heu
        for i_in_min_heu in lil_in_min_heu:
            if mimi > i_in_min_heu:
                mimi = i_in_min_heu
        return mimi
    print(min_heu([45545, 232353252, 3534534, 3453534 ,34534, 345, 345453, 5,345, 534, 1, -4334534]))
    print(min([45545, 232353252, 3534534, 3453534 ,34534, 345, 345453, 5,345, 534, 1, -4334534]))
    print(min_heu.__sizeof__())
    print(min.__sizeof__())
    class Gamer:
        def __init__(self, dva):
            self.dva = dva
        def geniu(self):
            pass
    loh = Gamer({1, 2})
    print("class =", loh.__sizeof__(), "?????")
    def passsa():
        pass
    print("def =", passsa.__sizeof__())
    print("str =", "4".__sizeof__())
    print("list =", [4].__sizeof__())
    print("tuple =", (4, 5).__sizeof__())
    a = 1
    print("int = ", a.__sizeof__())
    a = 1.1
    print("float =", a.__sizeof__())
    print("dict =", {"game": 1}.__sizeof__())
    print("set =", {1, 2}.__sizeof__())

    from sys import getsizeof
    print(r"from sys import getsizeof")
    class Gamer:
        def __init__(self, dva):
            self.dva = dva
        def geniu(self):
            pass
    loh = Gamer({1, 2})
    print("class =", getsizeof(loh), "?????")
    def passsa():
        pass
    print("def =", getsizeof(passsa))
    print("str =", getsizeof("4"))
    print("list =", getsizeof([4]))
    print("tuple =", getsizeof((4, 5)))
    a = 1
    print("int = ", getsizeof(a))
    a = 1.1
    print("float =", getsizeof(a))
    print("dict =", getsizeof({"game": 1}))
    print("set =", getsizeof({1, 2}))

    def hrenb(s, lil=[]):  # Это неправильно
        lil.append(s)
        return lil
    l = hrenb(1)
    l = hrenb(2)
    print(l)  # Ну и дичь
    def okey(s, lil=None):
        if lil is None: lil = []
        lil.append(s)
        return lil
    l = okey(1)
    l = okey(2)
    print(l)
    print("*args **kwargs")
    def os_path(disk, *args, sep=None, **kwargs):
        if sep is None:
            sep = '\\'
        args = (disk, ) + args
        if "trim" in kwargs and kwargs["trim"]:
            args = [x22.strip() for x22 in args]
        path = sep.join(args)
        return path

    p = os_path("F:\\", "     -stepik.org",
    "Добрый, добрый Python (Питон)",
    "39\\р39. Функция.docx", trim=True)
    print(p)

    p = os_path("F:\\", "      -stepik.org",
    "     Добрый, добрый Python (Питон)    ",
    "39\\р39. Функция.docx", sep="/", trim=True)
    print(p)
    def docdac(**nokti):
        return nokti
    print(docdac(haha=2, game="start"))
    def loha(*nokti):
        return nokti
    print(loha(2, 3, "deee"))
    print("""x, *y = (1, 2, 3, 4, 5, 6)
=> x = 1, y = (2, 3,4 ,5 ,6)
r = [1, 2, 3]
a = (*r,)
=> a = (1, 2, 3)
d = (-5, 5)
t = list(range(*d))
=> [-5, 5]
[*range(1, 5)]
=> [1, 2, 3, 4]""")
    print([*range(1, 5)] + [*range(-9, -4)])
    print([*range(1, 11)])
    print()
    print("RECURSION")
    field = [
        ["#", "*", "*", "*", "#"],
        ["#", "#", "#", "#", "#"],
        ["*", "*", "*", "*", "#"],
        ["#", "#", "*", "*", "*"],
        ["#", "#", "*", "#", "#"]
    ]
    print()
    for oba in field: print(oba)
    print()

    def recs(p, i, j, sz):
        if p[i][j] != "*": return
        p[i][j] = "@"
        if i-1 >= 0 and p[i-1][j] == "*": recs(p, i-1, j, sz)
        if i+1 < sz and p[i+1][j] == "*": recs(p, i+1, j, sz)
        if j-1 >= 0 and p[i][j-1] == "*": recs(p, i, j-1, sz)
        if j+1 < sz and p[i][j+1] == "*": recs(p, i, j+1, sz)

    recs(field, 2, 2, len(field))
    print(*field, sep="\n")


    # field = (
    #     ("#", "*", "*", "*", "#"),
    #     ("#", "#", "#", "#", "#"),
    #     ("*", "*", "*", "*", "#"),
    #     ("#", "#", "*", "*", "*"),
    #     ("#", "#", "*", "#", "#")
    # )
    # for loh in field:
    #     for i, geni in enumerate(loh):
    #         recs(geni, i)
    # res = [["@" if x == "*" and i >= (len(field)//2) else x
    #         for x in row]
    #         for i, row in enumerate(field)]
    # print()
    # for obe in res: print(obe)
    # res2 = tuple(tuple("@" if x == "*" and i >= (len(field)//2) else x
    #                    for x in row)
    #              for i, row in enumerate(field))
    # print()
    # for penws in res2: print(penws)
    def factoriall(n):
         return 1 if n <= 1 else n * factoriall(n-1)
    print(factoriall(3))
    print("Хвостовая функция лучше для памяти.")
    def factoriel(n, res=1):
        return res if n <= 1 else factoriel(n-1, res*n)
    print(factoriel(3))

    def ee(a):
        print("11") if a == 11 else print(None)
        return "11" if a == 11 else None
    print(ee(13231))
    ha = lambda a1: a1 % 2 == 0
    print(ha(1))


    def say_name(name: str):
        def say_goodbye():
            print("eee" + name)
        return say_goodbye

    link = say_name("aaa")
    link()
    link2 = say_name("yyy")
    link2()


    def counter(start=0):
        def step():
            nonlocal start
            start  += 1
            return start
        return step

    c1 = counter(10)
    c2 = counter()
    print(c1(), c2())  # => 11 1
    print(c1(), c2())  # => 12 2
    print(c1(), c2())  # => 13 3


    def strip_string(strip_chars=" "):
        def do_strip(string):
            return string.strip(strip_chars)
        return do_strip


    strip1 = strip_string()
    strip2 = strip_string(" ?!,.;")
    print(strip1("hello python!.. "))
    print(strip2("hello python!.. "))


    # def func_decorator(func):
    #     def wrapper():
    #         print("------ что-то делаем перед вызовом функции ------")
    #         func()
    #         print("------ что-то делаем после вызова функции ------")
    #     return wrapper
    #
    #
    # def some_func():
    #     print("Вызов функции some_func")
    #
    #
    # f = func_decorator(some_func())
    # f()

    class Base:
        # Инкапсуляция
        __attribut = 4
        def __init__(self):
            pass

        # Абстрактный метод, который должен быть переопределён у потомков
        def do(self):
            pass

        # Вспомогательный статический метод
        @staticmethod
        def get_attribut(): return Base.__attribut

    # Наследник
    class UnderBase(Base):
        def do(self):
            print("do")

        @staticmethod
        def p(s, sep=None, end=None):
            if sep is None: sep = ""
            if end is None: end = "\n"
            print(s, sep=sep, end=end)

    # Полиморфизм
    class Polimorph(Base):
        def get_attribut(self): return Base.get_attribut() + 2

    base = Base()
    under_base = UnderBase()
    polimorph = Polimorph()
    print(base.get_attribut())
    under_base.do()
    print(polimorph.get_attribut())

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None  # Левый потомок
            self.right = None  # Правый потомок

    # Создание узлов
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(2)
    root.left.right = Node(7)
    root.right.left = Node(3)
    root.right.right = Node(6)

    # Пример использования
    print(root.value)  # Выведет 10
    print(root.left.value)  # Выведет 5
    print(root.right.value)  # Выведет 15

    dodad = {"1": [10,
                    {"3": [5,
                           {"7": 3,
                            "6": 6}],
                    "2": [15,
                           {"5": [2],
                           "4": [7]}]
        }]}

    print(dodad["1"][1]["2"][1]["4"])

    class BinaryHeap:
        def __init__(self):
            self.heap = []  # Список для хранения элементов кучи
            self.size = 0  # Размер кучи

        def len_heap(self): return self.size

        def is_empty(self): return self.size == 0

        @staticmethod
        def parent(i): return (i - 1) // 2

        @staticmethod
        def left_child(i): return 2 * i + 1

        @staticmethod
        def right_child(i): return 2 * i + 2

        def swap(self, i, j): self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

        def insert(self, value):
            self.heap.append(value)
            self.size += 1
            self.heapify_up(self.size - 1)

        def heapify_up(self, i):
            while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
                self.swap(i, self.parent(i))
                i = self.parent(i)

        def delete_max(self):
            if self.is_empty(): return None

            if self.size == 1:
                self.size -= 1
                return self.heap.pop()

            max_element = self.heap[0]
            self.heap[0] = self.heap.pop()
            self.size -= 1
            self.heapify_down(0)

            return max_element

        def heapify_down(self, i):
            largest = i
            left = self.left_child(i)
            right = self.right_child(i)

            if left < self.size and self.heap[left] > self.heap[largest]: largest = left

            if right < self.size and self.heap[right] > self.heap[largest]: largest = right

            if largest != i:
                self.swap(i, largest)
                self.heapify_down(largest)  # Рекурсивно опускаем дальше

        def get_max_without_delete(self): return None if self.is_empty() else self.heap[0]

    heap = BinaryHeap()

    heap.insert(10)
    heap.insert(5)
    heap.insert(15)
    heap.insert(20)
    heap.insert(8)

    print("Куча:", heap.heap)  # Вывод: Куча: [20, 15, 10, 5, 8]

    max_value = heap.delete_max()
    print("Удаленный максимум:", max_value)  # Вывод: Удаленный максимум: 20
    print("Куча после удаления:", heap.heap)  # Вывод: Куча после удаления: [15, 8, 10, 5]
    print("Максимальный элемент:", heap.get_max_without_delete())  # Вывод: Максимальный элемент: 15
    print("Размер кучи:", heap.len_heap())  # Вывод: Размер кучи: 4

    while not heap.is_empty(): print("Удаленный максимум:", heap.delete_max())

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

    """Задача 3. Симметрическая разность. 
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
    Замечание: Для вывода можно использовать любой алгоритм сортировки."""

    def task3(data_task3: tuple) -> list:
        print("data", data_task3)
        result1 = []
        result2 = []
        i_task3 = 0
        while data_task3[i_task3] != 0:
            result1.append(data_task3[i_task3])
            i_task3 += 1
        i_task3 += 1
        while data_task3[i_task3] != 0:
            result2.append(data_task3[i_task3])
            i_task3 += 1
        print("set1", result1)
        print("set2", result2)

        result1_len = 0
        for _ in result1: result1_len += 1
        result2_len = 0
        for _ in result2: result2_len += 1

        similarities = []
        for i in range(result1_len):
            for j in range(result2_len):
                if result1[i] == result2[j]:
                    similarities.append(result1[i])

        print(similarities)
        difference = []
        for r_task3 in data_task3:
            if r_task3 in similarities or r_task3 == 0: continue
            else: difference.append(r_task3)

        print(difference)
        return difference

    # # data = 1 2 3 4 5 0 1 7 5 8 0
    # set_input = input("Numbers:_")
    # set_input_split = set_input.split()
    # set_numbers = map(int, set_input_split)
    # data = tuple(set_numbers)
    # print(heapsort(task3(data_task3=data)))


    def task4():
        """Задача 4. Два массива.
    Ограничение по времени: 2 с. Ограничение по памяти: 64 Mb.
    Даны два упорядоченных по возрастанию массива. Требуется найти количество
    таких элементов, которые присутствуют в обоих массивах. Например, в массивах (0, 0, 1, 1,
    2, 3) и (0, 1, 1, 2) имеется четыре общих элемента – (0, 1, 1, 2).
    Первая строка содержит размеры массивов N1 и N2. В следующих N1 строках
    содержатся элементы первого массива, в следующих за ними N2 строках – элементы
    второго массива.
    Программа должна вывести ровно одно число – количество общих элементов.
    Формат входных данных:
    Na, Nb
    a1
    a2
    …
    aNa
    b1
    b2
    …
    bNb
    Формат выходных данных:
    Одно целое число – количество общих элементов

    Примеры:
    Стандартный ввод
    5 5
    1
    1
    2
    2
    3
    0
    1
    3
    3
    4
    Стандартный вывод
    2"""
        # N1, N2 = map(int, input("Размеры двух массивов:_").split())
        # count = 1
        # m1 = []
        # while count < N1 + 1:
        #     na = int(input(f"Элемент {count} в первый массив:_"))
        #     m1.append(na)
        #     count += 1
        # count = 1
        # m2 = []
        # while count < N2 + 1:
        #     nb = int(input(f"Элемент {count} во второй массив:_"))
        #     m2.append(nb)
        #     count += 1

        m1 = (0, 0, 1, 1, 2, 3, 9)
        m2 = (0, 1, 1, 2, 2, 7, 8, 9, 5, 3, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9)
        new_m1 = list(m1)
        new_m2 = list(m2)
        new_m1_len = 0
        for _ in m1: new_m1_len += 1
        new_m2_len = 0
        for _ in m2: new_m2_len += 1

        similarities = []

        max_set = new_m1 if len(new_m1) > len(new_m2) else new_m2
        min_set = new_m2 if max_set == new_m1 else new_m1

        ii = 0
        while ii < len(min_set) + len(max_set):
            brek = False
            for i in range(len(max_set)):
                for j in range(len(min_set)):
                    if max_set[i] == min_set[j]:
                        similarities.append(max_set[i])
                        max_set.pop(i)
                        min_set.pop(j)
                        brek = True
                        break
                if brek: break
            ii += 1

        print("Вывод", len(similarities))

    some_file.console.log("console.log()", "erere", "erererer", sep="-")
    some_file.console.warn("ergeorjgperog")

    def test_yield():
        def my_generator():
            n = 0
            while n < 3:
                yield n
                n += 1

        # Использование генератора
        for value in my_generator():
            print(value)

        # Вывод:
        # 0
        # 1
        # 2

    def bubble_sort(s: str) -> str:
        symbols = list(s)
        length = 0
        for _ in s: length += 1

        for i in range(length):
            for j in range(length-i-1):
                if symbols[j] > symbols[j+1]:
                    symbols[j], symbols[j+1] = symbols[j+1], symbols[j]
        return "".join(symbols)


    def quick_sort(s):
        if len(s) <= 1: return s
        pivot = s[len(s)//2]
        left = [x for x in s if x < pivot]
        middle = [x for x in s if x == pivot]
        right = [x for x in s if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


    class Console:
        @staticmethod
        def log(*s, sep=None, end=None):
            if sep is None and end is None:
                print(*s)
            elif sep is None:
                print(*s, end=end)
            elif end is None:
                print(*s, sep=sep)
            else:
                print(*s, sep=sep, end=end)

        class Bcolors:
            HEADER = '\033[95m'
            OKBLUE = ('\033[94m', 'blue')
            OKCYAN = ('\033[96m', 'cyan')
            OKGREEN = ('\033[92m', 'green')
            WARNING = ('\033[93m', 'yellow')
            FAIL = ('\033[91m', 'red')
            ENDC = '\033[0m'
            BOLD = '\033[1m'
            UNDERLINE = '\033[4m'

        @staticmethod
        def warn(s): print(Console.Bcolors.WARNING[0] + s + Console.Bcolors.ENDC)

    class NotHashTable:
        def __init__(self, keys=None, values=None):
            if keys is None: keys = []
            if values is None: values = []
            self.__keys = keys
            self.__values = values

        def __str__(self):
            string_return = ""
            for ii in range(NotHashTable.get_size(self)):
                if ii == (NotHashTable.get_size(self) - 1):
                    string_return += str(self.__keys[ii]) + ": " + str(self.__values[ii])
                else:
                    string_return += str(self.__keys[ii]) + ": " + str(self.__values[ii]) + ", "
            return string_return

        def get_size(self):
            size = 0
            for _ in self.__keys: size += 1
            return size

        def get_keys(self):
            return self.__keys

        def get_values(self):
            return self.__values

        def get_value(self, key):
            for ii in range(NotHashTable.get_size(self)):
                if self.__keys[ii] == key: return self.__values[ii]
            return None

        def get_key(self, value):
            for ii in range(NotHashTable.get_size(self)):
                if self.__values[ii] == value: return self.__keys[ii]
            return None

        def get_all(self):
            lil = []
            for ii in range(NotHashTable.get_size(self)): lil.append([self.__keys[ii], self.__values[ii]])
            return lil

        def ad(self, key, value):
            self.__keys.append(key)
            self.__values.append(value)
            return NotHashTable.get_all(self)

        def delel_key(self, value):
            for ii in range(NotHashTable.get_size(self)):
                if self.__values[ii] == value:
                    self.__keys.pop(ii)
                    self.__values.pop(ii)
                    return ii
            return NotHashTable.get_all(self)

        def delel_value(self, key):
            for ii in range(NotHashTable.get_size(self)):
                if self.__keys[ii] == key:
                    self.__keys.pop(ii)
                    self.__values.pop(ii)
                    return ii
            return NotHashTable.get_all(self)

        def delel_at_index(self, indes: int):
            self.__keys.pop(indes)
            self.__values.pop(indes)
            return NotHashTable.get_all(self)

        def clear_all(self):
            self.__keys = []
            self.__values = []
            return NotHashTable.get_all(self)

        def edit_value(self, key, new_value):
            for ii in range(NotHashTable.get_size(self)):
                if self.__keys[ii] == key: self.__values[ii] = new_value
            return NotHashTable.get_all(self)

        def edit_key(self, key, new_key):
            for ii in range(NotHashTable.get_size(self)):
                if self.__keys[ii] == key: self.__keys[ii] = new_key
            return NotHashTable.get_all(self)

        def edit_at_index(self, indes: int, new_key=None, new_value=None):
            if new_value is None:
                self.__keys[indes] = new_key
            elif new_key is None:
                self.__values[indes] = new_value
            else:
                self.__keys[indes] = new_key
                self.__values[indes] = new_value
            return NotHashTable.get_all(self)

    console = Console()
    nothashtable = NotHashTable(["math", "physics"], ["2", "1"])
    nothashtable.ad("fa", 3)
    nothashtable.ad("loh", 45)
    print(nothashtable)
    print(nothashtable.get_values())
    print(nothashtable.get_keys())
    print(nothashtable.get_all())
    print(nothashtable.edit_value("math", "3"))
    print(nothashtable.edit_key("math", "mathematic"))
    print(nothashtable.edit_at_index(2, "ifa"))
    console.warn(str(nothashtable.edit_at_index(3, new_value=999)))
    console.warn(str(nothashtable))
    print(all([[], [], True]))

if __name__ == "__main__":
    main()

# import sqlite3 as sq
# with sq.connect("saper.db") as con:
#     cur = con.cursor()
#     cur.execute("DROP TABLE IF EXISTS 'new'")
#     cur.execute("""CREATE TABLE IF NOT EXISTS 'new'(
#     kofra TEXT DEFAULT '???',
#     numbrg INTEGER DEFAULT 0)""")


"""
Магараджа — это шахматная фигура, сочетающая возможности ферзя и коня. Таким
образом, магараджа может ходить и бить на любое количество клеток по диагонали,
горизонтали и вертикали (т.е. как ферзь), а также либо на две клетки по горизонтали и на
одну по вертикали, либо на одну по горизонтали и на две по вертикали (как конь).
Ваша задача — найти число способов расставить на доске N на N ровно K
магараджей так, чтобы они не били друг друга.
Формат входных данных:
Два целых числа: N и K (1 ≤ K ≤ N ≤ 10).
Формат выходных данных:
Число способов расставить на доске N на N ровно K магараджей так, чтобы они не били друг друга.
Примеры:
Входные данные: 3 1 Выходные данные: 9
Входные данные: 4 2 Выходные данные: 20
Входные данные: 5 3 Выходные данные: 48
"""
