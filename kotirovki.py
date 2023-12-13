import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

#URL_TEMPLATE ="https://ru.investing.com/equities/apple-computer-inc"
#r = requests.get(URL_TEMPLATE)
#src = r.text
#soup = bs(src, "lxml")
#kot_dives = soup.find("div", {"class": "flex flex-wrap gap-x-4 gap-y-2 items-center md:gap-6 mb-3 md:mb-0.5"})
#print(kot_dives.text.replace('+', '\n+', 1).replace("(", " (").replace('-', '\n-', 1))

def equitities(name):
    URL_TEMPLATE = "https://ru.investing.com/"+name
    r = requests.get(URL_TEMPLATE)
    src = r.text
    soup = bs(src, "lxml")
    kot_dives = soup.find("div", {"class": "flex flex-wrap gap-x-4 gap-y-2 items-center md:gap-6 mb-3 md:mb-0.5"})
    return (kot_dives.text.replace('+', '\n+', 1).replace("(", " (").replace('-', '\n-', 1))

print(equitities("equities/sberbank_rts"))

def currencies(name):
    URL_TEMPLATE = "https://ru.investing.com/"+name
    r = requests.get(URL_TEMPLATE)
    src = r.text
    soup = bs(src, "lxml")
    kot_dives = soup.find("div", {"class": "instrument-price_instrument-price__2w9MW flex items-end flex-wrap font-bold"})
    return (kot_dives.text.replace('+', '\n+', 1).replace("(", " (").replace('-', '\n-', 1))

print(currencies("currencies/cny-rub"))