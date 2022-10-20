from typing import Dict, List

from dz_21.entily.Errors import NoTypeRequest, NoTypeShopOrStore
from dz_21.entily.Storage import Storage


class Request:
    def __init__(self, request: str, storages: Dict[str, Storage]):
        split_request: List[str] = request.strip().lower().split(' ')
        if len(split_request) < 7:
            raise NoTypeRequest

        self.amount = int(split_request[1])
        self.product = split_request[2]
        self.departure = split_request[4]
        self.destanation = split_request[6]

        if self.departure not in storages or self.destanation not in storages:
            raise NoTypeShopOrStore




