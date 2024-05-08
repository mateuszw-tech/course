from abc import ABC, abstractmethod
from typing import List


class AdvertisementInfo:

    def __init__(self, name: str, location: str, phone_number: str, title: str, price: str):
        self.title = title
        self.name = name
        self.location = location
        self.phone_number = phone_number
        self.price = price


class Fetcher(ABC):
    @abstractmethod
    def load_osint_data(self) -> List[AdvertisementInfo]:
        raise NotImplementedError()


class SprzedajemyFetcher(Fetcher):
    def load_osint_data(self) -> List[AdvertisementInfo]:

        pass



