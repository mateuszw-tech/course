import time

import utils
from utils import SprzedajemyUtils, ScraperUtils
import asyncio
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
from fetcher import SprzedajemyFetcher

start = time.perf_counter()
fetcher = SprzedajemyFetcher("Malbork")
urls = fetcher.get_all_offers_urls()
fetcher.load_osint_data(urls)[77].display_information()
stop = time.perf_counter()
print("Elapsed time: ", stop - start)
