import concurrent
import time
from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor
from typing import List

from bs4 import BeautifulSoup
from tqdm import tqdm
import asyncio
import aiohttp

from utils import SprzedajemyUtils, ScraperUtils


class AdvertisementInfo:

    def __init__(
            self,
            title: str,
            username: str,
            location: str,
            phone_number: str,
            price: str,
            url: str,
    ):
        self.title = title
        self.username = username
        self.location = location
        self.phone_number = phone_number
        self.price = price
        self.url = url

    def display_information(self):
        print(
            "Title: "
            + self.title
            + "\nUsername: "
            + self.username
            + "\nLocation: "
            + self.location
            + "\nPhone Number: "
            + self.phone_number
            + "\nPrice: "
            + self.price
            + "\nURL: "
            + self.url
        )


class Fetcher(ABC):
    @abstractmethod
    def load_osint_data(self, offer_list) -> List[AdvertisementInfo]:
        raise NotImplementedError()


class SprzedajemyFetcher(Fetcher):

    def __init__(self, *cities):
        self.cities = cities
        self.current_data: list[AdvertisementInfo] = []

    def load_osint_data(self, offer_list: list[str]) -> List[AdvertisementInfo]:
        osint_data_futures = []
        results_list = []
        with ThreadPoolExecutor(max_workers=16) as executor:
            for offer in offer_list:
                osint_data_futures.append(executor.submit(SprzedajemyFetcher.load_data, offer))
            completed_futures, _ = concurrent.futures.wait(osint_data_futures)
            for future in completed_futures:
                results_list.append(future.result())
            osint_data = [results for results in results_list]

        return osint_data

    def get_all_offers_urls(self) -> List[str]:
        pages = ScraperUtils.get_all_pages_urls_from_different_cities(SprzedajemyUtils.get_all_pages_urls, *self.cities)
        offer_urls_futures = []
        results_list = []
        with ThreadPoolExecutor(max_workers=16) as executor:

            for page in pages:
                offer_urls_futures.append(executor.submit(SprzedajemyUtils.find_all_offers_in_selected_page, page))

            completed_futures, _ = concurrent.futures.wait(offer_urls_futures)
            for future in completed_futures:
                try:
                    results_list.append(future.result())
                except Exception:
                    pass

            offers = [result for results in results_list for result in results]

        return offers

    def change_cities(self, *cities) -> None:
        self.cities = cities

    @staticmethod
    def load_data(offer_url):
        soup = ScraperUtils.return_website_string_as_bs4_content(offer_url)
        title = SprzedajemyUtils.get_offer_title(soup)
        username = SprzedajemyUtils.get_offer_username(soup)
        location = SprzedajemyUtils.get_offer_location(soup)
        phone_number = SprzedajemyUtils.get_offer_phone_number(soup)
        price = SprzedajemyUtils.get_offer_price(soup)
        url = offer_url
        return AdvertisementInfo(title, username, location, phone_number, price, url)

    async def append_data(self, info: AdvertisementInfo) -> None:
        self.current_data.append(info)

    async def load_data_async(self, offer_url):
        try:
            async with aiohttp.ClientSession(trust_env=True, timeout=aiohttp.ClientTimeout(total=20)) as session:
                async with session.get(offer_url, timeout=25) as resp:
                    body = await resp.text()
                    soup = BeautifulSoup(body, 'html.parser')
                    title = SprzedajemyUtils.get_offer_title(soup)
                    username = SprzedajemyUtils.get_offer_username(soup)
                    location = SprzedajemyUtils.get_offer_location(soup)
                    phone_number = SprzedajemyUtils.get_offer_phone_number(soup)
                    price = SprzedajemyUtils.get_offer_price(soup)
                    url = offer_url
                    print("test " + offer_url)
            await self.append_data(AdvertisementInfo(title, username, location, phone_number, price, url))
        except Exception as e:
            pass

    async def load_osint_data_async(self, offer_list: list[str]) -> None:
        tasks = []
        # async with asyncio.Semaphore(500):
        for offer in offer_list:
            task = asyncio.create_task(self.load_data_async(offer))
            tasks.append(task)

        await asyncio.gather(*tasks)

    def get_osint_data(self):
        return self.current_data
