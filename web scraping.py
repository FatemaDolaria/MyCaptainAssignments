# Web Scraping project

import requests
from bs4 import BeautifulSoup

url = "https://www.newegg.com/global/in-en/black-corsair-cf-9010041-ww-chair/p/N82E16826816174?Description=office%20chair&cm_re=office_chair-_-26-816-174-_-Product&quicklink=true"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
title = soup.find_all('h1', {'class':'product-title'})[0].get_text()
price = soup.find_all('div', {'class':'price-current'})[0].get_text()
print(title)
print(price)
