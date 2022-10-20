import aiohttp
import asyncio
from bs4 import BeautifulSoup
import requests
"""
https://ozon.by/product/krem-dlya-litsa-l-oreal-paris-vozrast-ekspert-45-lifting-uhod-protiv-morshchin-dnevnoy-50-ml-654856567/?asb2=nt6OFcKIyI1UvEMR4L1sITRpzb1beZvWBWFeSFZVbtSkEI-sYtTvMXnlW28X830a&avtc=1&avte=2&avts=1666285172&sh=RTH7QNSFdA
"""
def parse_item(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "lxml")

    result = soup.find_all("li", class_="le4")
    code = soup.find("span", class_="m7v v7m").text[12::]
    brand = result[len(result) - 1].text
    name = soup.find("h1", class_="n6v").text
    return {
        "code": code,
        "brand": brand,
        "name": name
    }
