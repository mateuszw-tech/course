import time

import utils
from utils import SprzedajemyUtils
import asyncio
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
from fetcher import SprzedajemyFetcher

# with ThreadPoolExecutor(max_workers=100) as executor:
#     offer_urls_futures = []
#     for i in range(100):
#         offer_urls_futures.append(executor.submit(SprzedajemyUtils.get_all_pages_urls, "Głogów"))
#
#     completed_futures, _ = concurrent.futures.wait(offer_urls_futures)
#     results_list = []
#     for future in completed_futures:
#         results_list.append(future.result())
#
#         #wrzucić to w jakąś metodę #int ile wątków


adapter = SprzedajemyFetcher()
advertisement_info_list = adapter.load_osint_data()

print(utils.ScraperUtils.get_all_pages_urls_from_different_cities(SprzedajemyUtils.get_all_pages_urls, "Elbląg", "Warszawa"))
