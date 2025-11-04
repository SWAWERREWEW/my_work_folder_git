def task13():
    """Задача 13. Большая книжка
Ограничение по времени: 5 секунды Ограничение по памяти: 4 мегабайта.
Заказчику понравилось решение нашей задачи по
созданию записной книжки и он предложил нам более сложную задачу: создать простую базу данных, которая хранит много
записей вида ключ: значение. Для работы с книжкой предусмотрены 4 команды:

ADD KEY VALUE — добавить в базу запись с ключом KEY и значением VALUE. Если такая запись уже есть, вывести ERROR.

DELETE KEY — удалить из базы данных запись с ключом KEY. Если такой записи нет — вывести ERROR.

UPDATE KEY VALUE — заменить в записи с ключом KEY значение на VALUE. Если такой записи нет — вывести ERROR.

PRINT KEY — вывести ключ записи и значение через пробел. Если такой записи

нет — вывести ERROR.
Количество входных строк в файле с данными не превышает 300000, количество первоначальных записей равно половине
количества строк (первые N/2 команд есть команды ADD).
Длины ключей и данных не превосходят 4096. Ключи и данные содержат только буквы латинского алфавита и цифры и не
содержат пробелов. Особенность задачи: все данные не поместятся в оперативной памяти и поэтому придется использовать
внешнюю. Примеры

Стандартный ввод
10
ADD JW SJXO
ADD RZBR YMW
ADD ADX LVT
ADD LKFLG UWM
PRINT ADX
UPDATE HNTP JQPVG
PRINT QURWB
DELETE MB

Стандартный вывод
ADX LVT
ERROR
QURWB MEGW
ERROR

Стандартный ввод
15
ADD RWJSN JFTF
ADD ZDH GOON
ADD FCDS TCAY
ADD HMGVI BWK
ADD JTDU TLWWN
ADD IXRJ ERF
ADD IAOD GRDO
PRINT IXRJ
PRINT JTDU
PRINT IXRJ
UPDATE ZDH IOX
PRINT ZDH
ADD GVWU RTA
DELETE ZDH
ADD FCDS IVFJV

Стандартный вывод
IXRJ ERF
JTDU TLWWN
IXRJ ERF
ZDH IOX
ERROR
    """
    class Dictionary:
        def __init__(self, keys, values):
            self.__keys = keys
            self.__values = values

        def get_size(self):
            n = 0
            for _ in self.__keys: n += 1
            return n

        def print_key(self, key):
            has_key = False
            for i in range(Dictionary.get_size(self)):
                if key == self.__keys[i]:
                    print(self.__keys[i], self.__values[i])
                    has_key = True
            if not has_key: print("ERROR")

        def add_key_value(self, key, value):
            has_key = False
            for i in range(Dictionary.get_size(self)):
                if key == self.__keys[i]:
                    has_key = True
                    print("ERROR")
                    break
            if not has_key:
                self.__keys.append(key)
                self.__values.append(value)

        def delete_key(self, key):
            has_key = False
            for i in range(Dictionary.get_size(self)):
                if key == self.__keys[i]:
                    self.__keys.pop(i)
                    self.__values.pop(i)
                    has_key = True
                    break
            if not has_key: print("ERROR")

        def update_key_value(self, key, value):
            has_key = False
            for i in range(Dictionary.get_size(self)):
                if key == self.__keys[i]:
                    self.__keys[i] = key
                    self.__values[i] = value
                    has_key = True
                    break
            if not has_key: print("ERROR")


    # n = int(input("n="))
    # lil = []
    # for i in range(n):
    #     line = input("command:")
    #     lil.append(line.split())
    # print(lil)

    s = """ADD RWJSN JFTF
    ADD ZDH GOON
    ADD FCDS TCAY
    ADD HMGVI BWK
    ADD JTDU TLWWN
    ADD IXRJ ERF
    ADD IAOD GRDO
    PRINT IXRJ
    PRINT JTDU
    PRINT IXRJ
    UPDATE ZDH IOX
    PRINT ZDH
    ADD GVWU RTA
    DELETE ZDH
    ADD FCDS IVFJV"""
    lil = s.split("\n")
    lil = [x.split() for x in lil if x != ""]
    print(lil)

    data = Dictionary([], [])
    for command in lil:
        if command[0] == "ADD": data.add_key_value(command[1], command[2])
        elif command[0] == "PRINT": data.print_key(command[1])
        elif command[0] == "DELETE": data.delete_key(command[1])
        elif command[0] == "UPDATE": data.update_key_value(command[1], command[2])
        else: print("?")


if __name__ == '__main__': task13()