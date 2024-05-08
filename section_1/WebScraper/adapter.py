from abc import ABC, abstractmethod
from typing import List


class AdvertisementInfo:

    def __init__(self, name: str, location: str, phone_number: str, title: str, price: str):
        self.title = title
        self.name = name
        self.location = location
        self.phone_number = phone_number
        self.price = price


class Adapter(ABC):
    @abstractmethod
    def load_osint_data(self) -> List[AdvertisementInfo]:
        raise NotImplementedError()


class SprzedajemyAdapter(Adapter):
    def load_osint_data(self) -> List[AdvertisementInfo]:

        pass



