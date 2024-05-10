import concurrent.futures

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

from concurrent.futures import ThreadPoolExecutor


class ScraperUtils:

    @staticmethod
    def return_website_string_as_bs4_content(website: str):
        content = requests.get(website)
        return BeautifulSoup(content.content, "html.parser")

    @staticmethod
    def replace_polish_characters(input_text: str) -> str:
        strange = "ą, ć, ę, ł, ń, ó, ś, ź, ż"

        ascii_replacements = "a, c, e, l, n, o, s, z, z"

        translator = str.maketrans(strange, ascii_replacements)

        return input_text.translate(translator)

    # todo: Add Threading
    @staticmethod
    def get_all_pages_urls_from_different_cities(pages_scraping_method, *args):
        pages = [result for arg in args for result in pages_scraping_method(arg)]
        return pages


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
            offers.append(f'https://sprzedajemy.pl{offer_title.find("a").get('href')}')

        return offers

    @staticmethod
    def get_all_offers_urls(pages: list[str]):
        urls = []
        for page in tqdm(pages):
            offers = SprzedajemyUtils.find_all_offers_in_selected_page(page)
            for offer in offers:
                urls.append(offer)
        return urls

    @staticmethod
    def get_offer_title(soup: BeautifulSoup) -> str:
        return soup.find("span", class_="isUrgentTitle").get_text()

    @staticmethod
    def get_offer_username(soup: BeautifulSoup) -> str:
        return soup.find("strong", class_="name").get_text()

    @staticmethod
    def get_offer_location(soup: BeautifulSoup) -> str:
        return soup.find("span", class_="locationName").find("strong").get_text()

    @staticmethod
    def get_offer_phone_number(soup: BeautifulSoup) -> str:
        try:
            phone_number = (
                    soup.find("span", class_="phone-number-truncated").find("span").get_text()
                    + " "
                    + soup.find("span", class_="phone-number-truncated").get("data-phone-end")
            )
        except AttributeError:
            phone_number = "Unknown"
        return phone_number

    @staticmethod
    def get_offer_price(soup: BeautifulSoup) -> str:
        try:
            return soup.find("strong", class_="price").find("span").get_text()
        except AttributeError:
            return "Unknown"
