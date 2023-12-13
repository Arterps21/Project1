import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

URL_TEMPLATE ="https://ru.investing.com/search/?q=сбер&tab=news"
r = requests.get(URL_TEMPLATE)
src = r.text
soup = bs(src, "lxml")
page_h1 = soup.find("h1")
print(page_h1.text)
all_article_dives = soup.find_all("div", {"class": "articleItem"})
all_article_titles = [div.find("a", {"class": "title"}).text for div in all_article_dives]
all_article_titles = [t for t in all_article_titles if t != "{{title}}"]
k=0
for j in all_article_dives:
    for p in j.find_all('a', href=True):
        if p['href'] != "{{link}}":
            k += 1
            if k%2==0:
                print(all_article_titles[k//2-1], "https://ru.investing.com/"+p['href'])
for j in all_article_dives:
    for p in j.find_all('img', src=True):
        if p['src'] != "{{image}}":
            print(p['src'])
all_article_subs = [div.find("div", {"class": "articleDetails"}).text for div in all_article_dives]
all_article_subs = all_article_subs[:-2]
print(*all_article_subs)
