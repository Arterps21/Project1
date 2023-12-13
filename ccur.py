import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

URL_TEMPLATE ="https://ru.investing.com/currencies/eur-rub"
r = requests.get(URL_TEMPLATE)
src = r.text
soup = bs(src, "lxml")
kot_dives = soup.find("div", {"class": "instrument-price_instrument-price__2w9MW flex items-end flex-wrap font-bold"})
print(kot_dives.text.replace('+', '\n+', 1).replace("(", " (").replace('-', '\n-', 1))
