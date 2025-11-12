def task1():
    """
    Опишите функции add(), add_by_note(), find(), amount() .
С чего начать
Не пытайтесь сделать всю работу одновременно: выполняйте её по шагам.
Объявите словарь goods, добавьте в него пару продуктов — их можно скопировать из приведённых примеров.
Займитесь функцией add() — научите её добавлять продукты в словарь. Протестируйте работу этой функции и переходите к следующей. На каждом этапе перечитывайте подсказки и описания, относящиеся к функции, над которой вы работаете.
Каждую готовую функцию вызовите несколько раз с разными аргументами:
с необязательными аргументами и без них,
со вчерашней и завтрашней датой (через сто лет — тоже попробуйте),
передайте в add() и add_by_note() новые продукты и те, что уже есть в словаре goods.
Тестирование программы — значительная и обязательная часть работы, не пренебрегайте ей.
Подсказки
Формат даты можно определить константой date_format = '%Y-%m-%d'.
Функция add().
Проверить, есть ли название продукта (title) в словаре items.
Преобразовать строку с датой в тип date с помощью модуля datetime.
Применить list.append() для добавления словаря с ключами 'amount' и 'expiration_date' в список партий продукта с конкретным title.
Функция add_by_note().
Разделить строку на части по пробелам с помощью str.split.
Определить, является ли последняя часть строки датой.
Ту часть строки, где указано количество продукта, конвертировать в число типа Decimal
Оставшуюся часть строки объединить, чтобы получить название продукта: если название состояло из нескольких слов — функция str.split разобъёт его на части.
Вызвать функцию add(), передав в неё получившиеся данные — название, количество и срок хранения.
Функция find().
Перебрать ключи словаря.
При переборе применить к ключам функцию lower, чтобы провести поиск без учёта регистра.
Найденные названия продуктов добавить в список с результатами поиска при помощи функции append.
Функция amount().
Применить функцию find() для получения списка подходящих товаров.
Суммировать значения amount найденных продуктов для вычисления количества каждого найденного товара.
    """
    import datetime
    from decimal import Decimal

    date_format = '%Y-%m-%d'

    today_day = datetime.date.today().strftime(date_format)
    tomorrow_day = (datetime.date.today() + datetime.timedelta(days=1)).strftime(date_format)
    future_day = (datetime.date.today() + datetime.timedelta(days=365 * 100)).strftime(date_format)

    def add(items, title, amount, expiration_date=None):
        if isinstance(expiration_date, str):
            expiration_date = datetime.datetime.strptime(expiration_date, date_format).date()

        new_batch = {
            'amount': Decimal(str(amount)),
            'expiration_date': expiration_date
        }

        if title in items:
            items[title].append(new_batch)
        else:
            items[title] = [new_batch]
        print(f"Добавлено: {title}, Количество: {amount}, Годен до: {expiration_date}")

    def add_by_note(items, note):
        parts = note.split()

        expiration_date = None
        amount_str = None

        if len(parts) >= 3:
            datetime.datetime.strptime(parts[-1], date_format)
            expiration_date = parts[-1]
            parts.pop()

        if parts and len(parts) >= 2:
            Decimal(parts[-1])
            amount_str = parts[-1]
            parts.pop()

        title = " ".join(parts)
        add(items, title, amount_str, expiration_date)

    def find(items, needle):
        results = []
        needle_lower = needle.lower()

        for title in items.keys():
            if needle_lower in title.lower():
                results.append(title)

        return results

    def amount(items, needle):
        found_titles = find(items, needle)
        total_amount = Decimal('0')

        if not found_titles:
            return total_amount

        for title in found_titles:
            for batch in items[title]:
                total_amount += batch['amount']

        return total_amount


def main(): task1()
if __name__ == '__main__': main()