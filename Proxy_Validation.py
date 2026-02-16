import threading
import queue
import time

import requests

q = queue.Queue()
valid_proxies = []

RESETVALID = True

if RESETVALID:
    with open("Valid_Proxies.txt","w") as Val:
        Val.write("")

with open(r"C:\Users\david\OneDrive - Osceola County School District\2025-2026 School Year\AP Research Evans Xan\Data Collection\Code\Setup\Proxy_List.txt", "r") as f:

    proxies = f.read().split("\n")
    for p in proxies:
        q.put(p)

def check_proxies():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            res = requests.get("http://ipinfo.io/json",
                              proxies={"http" : proxy,
                                       "https": proxy},
                                       timeout=10)

        except requests.exceptions.ReadTimeout:
            print(f"{proxy} took too long to respond \n")
        except:

            print(f"{proxy} failed to fetch \n")
            continue
        
        else:
            if res.status_code == 200:
                print(f"{proxy} \n")
                with open("Valid_Proxies.txt", "a") as valid:
                    valid.write(proxy)
                    valid.write("\n")

    print("Validation Complete \n")

for _ in range(10):
    threading.Thread(target=check_proxies).start()
