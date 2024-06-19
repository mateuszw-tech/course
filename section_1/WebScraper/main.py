import time
import asyncio
from fetcher import SprzedajemyFetcher

start = time.perf_counter()
fetcher = SprzedajemyFetcher("Malbork")
urls = fetcher.get_all_offers_urls()
asyncio.run(fetcher.load_osint_data_async(urls))
fetcher.get_osint_data()[3].display_information()
stop = time.perf_counter()
print("Elapsed time: ", stop - start)
