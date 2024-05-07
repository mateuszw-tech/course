import concurrent.futures

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import asyncio
import aiohttp

from concurrent.futures import ThreadPoolExecutor


class ScraperUtils:

    @staticmethod
    def return_website_string_as_bs4_content(website: str):
        content = requests.get(website)
        return BeautifulSoup(content.content, "html.parser")

    @staticmethod
    def replace_polish_characters(input_text):
        strange = "ą, ć, ę, ł, ń, ó, ś, ź, ż"

        ascii_replacements = "a, c, e, l, n, o, s, z, z"

        translator = str.maketrans(strange, ascii_replacements)

        return input_text.translate(translator)


class SprzedajemyUtils:

    @staticmethod
    def get_url_with_localization_input(city: str) -> str:
        city_formatted = ScraperUtils.replace_polish_characters(city)

        return f"https://sprzedajemy.pl/{city_formatted}"

    @staticmethod
    def get_amount_of_pages(soup) -> int:
        x = soup.find("ul", class_="cntPaginator").find_all("a")[4:5]
        test_soup = BeautifulSoup(str(x[0]), "html.parser")
        return int(test_soup.find("span").get_text()) - 1

    @staticmethod
    def get_all_pages_urls(city) -> list[str]:
        url = SprzedajemyUtils.get_url_with_localization_input(city)
        pages = [url]
        soup = ScraperUtils.return_website_string_as_bs4_content(url)
        for i in range(SprzedajemyUtils.get_amount_of_pages(soup)):
            cnp = url + f"?offset={30 + i * 30}"
            pages.append(cnp)
        return pages

    @staticmethod
    def find_all_offers_in_selected_page(page: str):
        offers = []
        soup = ScraperUtils.return_website_string_as_bs4_content(page)
        offer_titles = soup.find_all("h2", class_="title")
        for offer_title in offer_titles:
            offers.append(offer_title.find("a").get('href'))

        return offers

    @staticmethod
    def get_all_offers_urls(pages: list[str]):
        urls = []
        for page in tqdm(pages):
            offers = SprzedajemyUtils.find_all_offers_in_selected_page(page)
            for offer in offers:
                urls.append(f'https://sprzedajemy.pl{offer}')
        return urls

    # ================== Test z async ================== #

    @staticmethod
    def return_offer(url):
        return f'https://sprzedajemy.pl{url}'

    @staticmethod
    async def fetch_all(pages):
        urls = []
        for page in tqdm(pages):
            offers = SprzedajemyUtils.find_all_offers_in_selected_page(page)
            for offer in offers:
                urls.append(f'https://sprzedajemy.pl{offer}')
        res = await asyncio.gather(*urls)
        return res

    @staticmethod
    async def test():
        urls = SprzedajemyUtils.get_all_pages_urls("Głogów")
        async with aiohttp.ClientSession():
            return await SprzedajemyUtils.fetch_all(urls)

    # ================== Test z thread ================== #

    @staticmethod
    def t_test(pages: list[str]):
        urls = []
        for page in tqdm(pages):
            offers = SprzedajemyUtils.find_all_offers_in_selected_page(page)
            for offer in offers:
                urls.append(f'https://sprzedajemy.pl{offer}')
        return urls
