"""
Модуль: Interval

Данный модуль предоставляет класс `Interval` для представления и работы с интервалами
вещественных чисел. Класс поддерживает основные математические операции, сравнения и
утилитарные методы для интервального анализа.

Классы:
    Interval: Представляет интервал [start, end] и поддерживает операции сложения,
              вычитания, умножения, деления, а также проверки принадлежности элемента интервалу.

Пример использования:
    >>> i1 = Interval(1, 3)
    >>> i2 = Interval(2, 5)
    >>> i1 + i2
    [3, 8]
    >>> i1 * i2
    [2, 15]
"""


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"[{self.start}, {self.end}]"

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __hash__(self):
        return hash((self.start, self.end))

    def __contains__(self, item):
        return self.start <= item <= self.end

    def __len__(self):
        return self.end - self.start

    def __add__(self, other):
        return Interval(self.start + other.start, self.end + other.end)

    def __sub__(self, other):
        return Interval(self.start - other.end, self.end - other.start)

    def __mul__(self, other):
        multiplications = (
            self.start * other.start,
            self.start * other.end,
            self.end * other.start,
            self.end * other.end,
        )
        return Interval(min(multiplications), max(multiplications))

    def __truediv__(self, other):
        if 0 in other:
            raise ZeroDivisionError
        return self * Interval(1 / other.start, 1 / other.end)

    def __neg__(self):
        return Interval(-self.end, -self.start)
