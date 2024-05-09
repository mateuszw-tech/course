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

    def load_osint_data(self) -> List[AdvertisementInfo]:
        pass

    # todo: add multiple cities argument
    @staticmethod
    def get_all_offers_urls(city: str, threads: int) -> List[str]:
        # pages = ScraperUtils.get_all_pages_urls_from_different_cities(SprzedajemyUtils.get_all_pages_urls, cities)
        pages = SprzedajemyUtils.get_all_pages_urls(city)
        offer_urls_futures = []
        results_list = []
        with ThreadPoolExecutor(max_workers=threads) as executor:
            for page in pages:
                offer_urls_futures.append(executor.submit(SprzedajemyUtils.find_all_offers_in_selected_page, page))

            completed_futures, _ = concurrent.futures.wait(offer_urls_futures)
            for future in completed_futures:
                results_list.append(future.result())
        return results_list
