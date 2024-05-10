import concurrent
from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor
from typing import List
from utils import SprzedajemyUtils, ScraperUtils


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

    def __init__(self, *cities):
        self.cities = cities

    def load_osint_data(self) -> List[AdvertisementInfo]:
        pass

    def get_all_offers_urls(self, threads: int) -> List[str]:
        pages = ScraperUtils.get_all_pages_urls_from_different_cities(SprzedajemyUtils.get_all_pages_urls, *self.cities)
        offer_urls_futures = []
        results_list = []
        with ThreadPoolExecutor(max_workers=threads) as executor:
            for page in pages:
                offer_urls_futures.append(executor.submit(SprzedajemyUtils.find_all_offers_in_selected_page, page))

            completed_futures, _ = concurrent.futures.wait(offer_urls_futures)
            for future in completed_futures:
                results_list.append(future.result())

            offers = [result for results in results_list for result in results]
        return offers

    def change_cities(self, *cities) -> None:
        self.cities = cities

