import requests
from bs4 import BeautifulSoup

URL = 'https://www.nissankendall.com/inventory/new-2019-nissan-leaf-sv-fwd-4d-hatchback-1n4az1cp6kc321458'
 
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

for div in soup.find_all('div', class_='swiper-slide'):
    if 'data-src' in div.img.attrs.keys():
        print(div.img['data-src'])
        break