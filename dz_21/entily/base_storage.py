from typing import Dict

from dz_21.entily.Errors import NoCountProduct, NoPlace
from dz_21.entily.Storage import Storage


class BaseStorage(Storage):

    def __init__(self, items: Dict[str, int], capacity: int):
        self.__items = items
        self.__capacity = capacity

    def add(self, name: str, amount: int):
        #- увеличивает запас items
        if self.get_free_space() < amount:
            raise NoPlace

        if name in self.__items:
            self.__items[name] += amount
        else:
            self.__items[name] = amount

    def remove(self, name: str, amount: int):
        #- уменьшает запас items
        if name not in self.__items or self.__items[name] < amount:
            raise NoCountProduct

        self.__items[name] -= amount
        if self.__items[name] == 0:
            self.__items.pop(name)


    def get_free_space(self):
        return self.__capacity - sum(self.__items.values())
        #- вернуть количество свободных мест

    def get_items(self):
        return self.__items
        #- возвращает сожержание склада в словаре {товар: количество}

    def get_unique_items_count(self):
        return len(self.__items)
        #- возвращает количество уникальных товаров.


