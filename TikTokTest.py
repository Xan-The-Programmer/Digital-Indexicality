from TikTokApi import TikTokApi
import asyncio
import os
import time
import random
import requests
import threading

sample=[]
sessions=3

def is_tiktok_usable(proxy):
    proxies = {"http": f"http://{proxy}","https": f"http://{proxy}"}
    try:
        r = requests.get(
            "https://www.tiktok.com/explore",
            proxies=proxies,
            timeout=3,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        html = r.text

        # Hard checks for real TikTok
        if "SIGI_STATE" in html and "Explore" in html:
            return True

        # If it's the bot/about page:
        return False

    except:
        return False
    
def ISHTTPS(proxy):
    proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
    try:
        res = requests.get("https://www.google.com", proxies=proxies, timeout=1)
        return res.status_code == 200
    except:
        return False

with open("Valid_Proxies.txt", "r") as file:
        proxy_list = file.read().split("\n")
        """prozy_list = {i: str for i in enumerate(proxy_list)} """
        print(f"{proxy_list}\n")

valid_proxies = []
used_proxies = set()
lock = threading.Lock()

def validate():
    global proxy_list, used_proxies, valid_proxies

    while True:
        with lock:
            # Filter out proxies already used by other threads
            available = [p for p in proxy_list if p not in used_proxies]

            if len(valid_proxies) >= sessions:
                return  # Enough proxies collected

            if not available:
                return  # No proxies left

            proxy = random.choice(available)
            used_proxies.add(proxy)

        print(f"Validating: {proxy}")

        # Phase 1: test HTTPS tunneling
        if not ISHTTPS(proxy):
            print(f"{proxy}: Phase 1 failed\n")
            continue

        print(f"{proxy}: Phase 1 passed\n")

        # Phase 2: test TikTok Explore
        if not is_tiktok_usable(proxy):
            print(f"{proxy}: Phase 2 failed\n")
            continue

        print(f"{proxy} PASSED ALL TESTS\n")

        with lock:
            valid_proxies.append(proxy)
            return  # This thread is done


threads = []

for i in range(10):
    t = threading.Thread(target=validate)
    threads.append(t)
    t.start()

print("All Threads have been initialized")

for t in threads:
    t.join()

print("All Threads have finished")

proxy_dicts = [{"server": f"http://{p}"} for p in valid_proxies]

async def trending_videos():
    async with TikTokApi() as api:

        ms_tokens = [
            'rBF2jooJ4qOsjr_daeSwkVYewwSUedUNdaDsrFwXEerkdcLoaR5IIaaD-p9ehLXa6KFlFIF32kssERSQQFIAxaxdY7ka7UOGKX38EMA8ePkieNf8Qvvv9_yVWWr68SVvan3vsDNF_wlw_4YlTeim_BbF',
            'uEtEIZDKmlUnInRCtu6npQh6lNt5R_2lhQpsej3kshiSELuCXctsdmKPftwP1NTo5saUZoW5MVOaiNSLVYhoJ7VAXzDJf7PEsT-5Qt_KttbiN4-yMk5eShIleAAxPM5_UgdNe8A-lnbx_kTYUCg4yuCbNw',
            'c22E3HYqD1XXL30X3cmjifZO6ERatQGXb3a7iIc8qjqrPM1HzdJcNAa_-SRQHZQVU3cOcWrqowta-JOoRd3oRgV42R97czoBncHteM9601o6GgyM61RDBCwZP_E7rOtn2XnDiArgNa0l_nuDwYdqBC_nyw'
        ]

        await api.create_sessions(ms_tokens=ms_tokens, proxies=proxy_dicts, num_sessions=1, sleep_after=3, browser=os.getenv("TIKTOK_BROWSER", "chromium"), headless=False)
        async for video in api.trending.videos(count=3):
            print(video)

            #pause for bot detection
            await asyncio.sleep(random.uniform(2, 5))

            hash_arr = [f"#{Hashtag.name}" for Hashtag in video.hashtags]
            sample.append(hash_arr)
            print(sample)

            async for comment in api.video(id=video.id).comments(5):
                print(comment.text)
                await asyncio.sleep(random.uniform(0.4, 1.4))  # human pause

if __name__ == "__main__":
    asyncio.run(trending_videos())