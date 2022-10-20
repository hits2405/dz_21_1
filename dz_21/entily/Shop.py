from dz_21.entily.Errors import СrowdedStore
from dz_21.entily.base_storage import BaseStorage


class Shop(BaseStorage):
    """В нем хранится **не больше 5 разных товаров**.
        Shop **не может быть наполнен**,
        если свободное место закончилось или в нем уже есть 5 разных товаров."""

    def add(self, name: str, amount: int):
        if self.get_unique_items_count() >= 5:
            raise СrowdedStore

        super().add(name, amount)


