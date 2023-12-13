import requests
from bs4 import BeautifulSoup


def news(name):
    """
        :param name: name of security investment
        :type name: str
        :returns: 3 titles, links and links on images in category news and
        3 titles, links and links on images in category analysis
        :rtype: list
    """
    link_part = "https://ru.investing.com/search/?q=" + name.replace(' ', '%20') + "&tab=news"
    r = requests.get(link_part)
    src = r.text
    soup = BeautifulSoup(src, "lxml")

    all_article_dives = soup.find_all("div", {"class": "articleItem"})
    all_article_titles = [div.find("a", {"class": "title"}).text for div in all_article_dives]
    all_article_titles = [t for t in all_article_titles if t != "{{title}}"]
    all_texts = []
    title_link = 0
    for link in all_article_dives:
        for p in link.find_all('a', href=True):
            if p['href'] != "{{link}}":
                title_link += 1
                if title_link % 2 == 0:
                    all_texts += [
                        str("[" + all_article_titles[title_link // 2 - 1] + "]" + "(https://ru.investing.com/" + p[
                            'href'] + ")")]
    for j in all_article_dives:
        for p in j.find_all('img', src=True):
            if p['src'] != "{{image}}":
                all_texts += [p['src']]
    return all_texts


def newsfortest(name):
    """
        :param name: name of security investment
        :type name: str
        :returns: 3 titles, links and links on images in category news and
        3 titles, links and links on images in category analysis
        :rtype: list
    """
    link_part = "https://ru.investing.com/search/?q=" + name.replace(' ', '%20') + "&tab=news"
    r = requests.get(link_part)
    test_value = r.status_code
    src = r.text
    soup = BeautifulSoup(src, "lxml")

    all_article_dives = soup.find_all("div", {"class": "articleItem"})
    all_article_titles = [div.find("a", {"class": "title"}).text for div in all_article_dives]
    all_article_titles = [t for t in all_article_titles if t != "{{title}}"]
    all_texts = []
    title_link = 0
    for link in all_article_dives:
        for p in link.find_all('a', href=True):
            if p['href'] != "{{link}}":
                title_link += 1
                if title_link % 2 == 0:
                    all_texts += [
                        str("[" + all_article_titles[title_link // 2 - 1] + "]" + "(https://ru.investing.com/" + p[
                            'href'] + ")")]
    for j in all_article_dives:
        for p in j.find_all('img', src=True):
            if p['src'] != "{{image}}":
                all_texts += [p['src']]
    return test_value
print(newsfortest("сбер"))