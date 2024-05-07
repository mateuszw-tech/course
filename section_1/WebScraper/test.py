import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm
from functools import cache, lru_cache

# url = ("https://sprzedajemy.pl/szukaj?inp_distance=0&inp_category_id=5&inp_location_id=58819&sort=inp_srt_date_d"
#        "&items_per_page=30")
#
# response = requests.get(url)
#
# soup = BeautifulSoup(requests.get(url).content, "html.parser")
#
# x = soup.find_all(class_="name")
#
# print(x)
# # -------------------------------------------------------------------------------------------
#
# chrome_options = Options()
# chrome_options.add_argument("--headless")
#
# url_a = ("https://sprzedajemy.pl/wszystkie-ogloszenia?offset=0")
#
# response_a = requests.get(url)
#
# driver = webdriver.Chrome(options=chrome_options)
# driver.get(url_a)
#
# input_element = driver.find_element(By.ID, "inp-location-autocompleter")
#
# input_element.send_keys("Warszawa")
# time.sleep(2)
# input_element.send_keys(Keys.ENTER)
#
# print(driver.current_url)
#
# soup = BeautifulSoup(requests.get(driver.current_url).content, "html.parser")
#
# x = soup.find_all(class_="name")
#
# print(x)
# -------------------------------------------------------------------------------------------
# url = "https://sprzedajemy.pl/szukaj?inp_distance=0&inp_category_id=5&inp_location_id=58819&sort=inp_srt_date_d"
# "&items_per_page=30"
# soup = BeautifulSoup(requests.get(url).content, "html.parser")
# x = soup.find("ul", class_="cntPaginator").find_all("a")[4:5]
# test_soup = BeautifulSoup(str(x[0]), "html.parser")
# result = test_soup.find("span").get_text()
# print(result)
#
#
# @lru_cache(maxsize=10)
# def testdef(soup, result):
#     pages = []
#     for _ in tqdm(range(int(result) - 1)):
#         next_btn = soup.find("li", class_="next").find("a")
#         cnp = "https://sprzedajemy.pl" + next_btn.get("href")
#         pages.append(cnp)
#
#         url = cnp
#         soup = BeautifulSoup(requests.get(url).content, "html.parser")
#     return pages
#
#
# print(testdef(soup, result))
