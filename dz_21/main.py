from typing import Dict

from dz_21.entily.Errors import Errors
from dz_21.entily.Request import Request
from dz_21.entily.Shop import Shop
from dz_21.entily.Storage import Storage

from dz_21.entily.Store import Store
from dz_21.entily.couers import Couers

store = Store(items={"яблоко": 5, "гранат": 10}, capacity=100)
shop = Shop(items={"гранат": 1}, capacity=20)
storages: Dict[str, Storage] = {'склад': store, 'магазин': shop}


def main():

    while True:
        print('Добрый день!\n')
        for storage_name, storage in storages.items():
            print(f'В {storage_name} хранится :\n{storage.get_items()}')
        input_user = str(input('Введите запрос в формате: Доставить 1 яблоко из склад в магазин\n'
                           'Введите стоп чтобы закончить'))
        if input_user in 'стоп':
            break

        try:
            request = Request(request=input_user, storages=storages)
        except Errors as error:
            print(error.message)
            continue

        couers = Couers(request=request, storages=storages)
        try:
            couers.move()
        except Errors as error:
            print(error.message)
            continue



if __name__ == '__main__':
    main()
