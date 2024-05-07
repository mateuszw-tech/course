import time

import utils
from utils import SprzedajemyUtils
import asyncio
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=100) as executor:
    offer_urls_futures = []
    for i in range(100):
        offer_urls_futures.append(executor.submit(SprzedajemyUtils.get_all_pages_urls, "Głogów"))

    completed_futures, _ = concurrent.futures.wait(offer_urls_futures)
    results_list = []
    for future in completed_futures:
        results_list.append(future.result())

