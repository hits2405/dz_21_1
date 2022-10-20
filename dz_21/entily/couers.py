from typing import Dict

from dz_21.entily.Request import Request
from dz_21.entily.Storage import Storage


class Couers:
    def __init__(self, request: Request, storages: Dict[str, Storage]):
        self.__request = request
        self.departure: Storage = storages[self.__request.departure]
        self.destanation: Storage = storages[self.__request.destanation]

    def move(self):
        self.departure.remove(name=self.__request.product, amount=self.__request.amount)
        print(f'Курьер забирает {self.__request.amount} {self.__request.product} из {self.__request.departure}')

        print(f'Курьер везет {self.__request.amount} {self.__request.product} со {self.__request.departure} '
              f'в {self.__request.destanation}')

        self.destanation.add(name=self.__request.product, amount=self.__request.amount)
        print(f'Курьер доставил {self.__request.amount} {self.__request.product} в {self.__request.destanation}')

