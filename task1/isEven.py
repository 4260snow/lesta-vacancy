def is_even(val):
    """
    Минусы:
        1) Не используется то, что "val % 2" уже 0 или 1
        2) Создаётся новый объект "0" (лишние действие и память)
    """
    return val % 2 == 0


def is_even_v2(val):
    """
    Плюс: решает минусы is_even
    Всё что не 0 not преобразует в False, а 0 - в True
    """
    return not val % 2


def is_odd(val):
    """
    Минусы:
        1) лишняя память под преобразования типа
        2) Дополнительный шаг для выполнения преобразования
    """
    return bool(val % 2)


def is_odd_v2(val):
    """
    Плюс: решает минус первый минус is_even и минусы is_odd
    Овечает на вопрос: "Число нечётно?". 0 - не нечётно => чётно, 1 - нечётно
    """
    return val % 2


"""
Немного сложнее воспринимается, но действия эквивалентны is_even
def is_even_v3(val):
    return val % 2 != 1

Плохие реализации (лишние дейсвия и избыточное использование памяти):
def is_even_v4(val):
    return [True, False][val % 2]

def is_even_v5(val):
    parity = {0: True,
              1: False}
    return parity[val % 2]

def is_even_v6(val):
    return val % 2 in range(0, 10, 2)
"""
