import requests

def proxy__switch(function,list,index):
    with open("Valid_Proxies.txt", "r") as f:
        proxies = f.read().split("\n")
    
    counter = 0

    for index in list:
        try:
            print(f"Using proxy: {proxies[counter]}")

        except:
            print("Failed")

        finally:
            counter += 1