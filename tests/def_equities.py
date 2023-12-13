import requests
from bs4 import BeautifulSoup

def equities(name):
    """
        :param name: piece of link on security investment
        :type name: str
        :returns: the price of the security
        :rtype: str
    """
    link_part = "https://ru.investing.com/" + name
    r = requests.get(link_part)
    src = r.text
    soup = BeautifulSoup(src, "lxml")
    kot_dives = soup.find("div", {"class": "flex flex-wrap gap-x-4 gap-y-2 items-center md:gap-6 mb-3 md:mb-0.5"})
    return kot_dives.text.replace('+', '\n+', 1).replace("(", " (").replace('-', '\n-', 1)

def equitiesfortest(name):
    link_part = "https://ru.investing.com/" + name
    r = requests.get(link_part)
    test_value = r.status_code
    src = r.text
    soup = BeautifulSoup(src, "lxml")
    kot_dives = soup.find("div", {"class": "flex flex-wrap gap-x-4 gap-y-2 items-center md:gap-6 mb-3 md:mb-0.5"})
    return test_value
