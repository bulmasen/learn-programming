# Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь
# определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
#
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
#
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на
# этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Cloth(ABC):
    @abstractmethod
    def fabricExpend(self):
        pass


class Coat(Cloth):
    def __init__(self, size):
        self.size = size

    @property
    def fabricExpend(self):
        return self.size / 6.5 + .5

    def __str__(self):
        return f'Пальто {self.size} размера.'


class Suit(Cloth):
    def __init__(self, height):
        self.height = height

    @property
    def fabricExpend(self):
        return self.height * 2 + .3

    def __str__(self):
        return f'Костюм {self.height} роста.'


class Warehouse:
    def __init__(self):
        self.goods = []

    def addGoods(self, item):
        self.goods.append(item)

    def totalFabricExpend(self):
        __totalFabric = 0
        for i in self.goods:
            __totalFabric += i.fabricExpend
        return __totalFabric

    def __str__(self):
        __goodsList = ''
        if self.goods:
            __goodsList = 'Над складе хранится:'
            for i in self.goods:
                __goodsList += f'\n\t{i}'
            return __goodsList
        else:
            return 'Склад пуст.'


warehouse1 = Warehouse()
warehouse1.addGoods(Suit(40))
warehouse1.addGoods(Suit(38))
warehouse1.addGoods(Coat(40))
warehouse1.addGoods(Coat(42))

print(warehouse1)
warehouse1.totalFabricExpend
