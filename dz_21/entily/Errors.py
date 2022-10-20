class Errors(Exception):
    message = 'базовая ошибка'


class NoCountProduct(Errors):
    message = 'Нет нужного количества товара'

class NoPlace(Errors):
    message = 'Нет свободного места'

class NoTypeRequest(Errors):
    message = 'Что то не так в запросе'

class NoTypeShopOrStore(Errors):
    message = 'Неверно указан склад или магазин'

class СrowdedStore(Errors):
    message = 'Склад переполнен'
