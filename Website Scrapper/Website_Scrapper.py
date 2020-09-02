import requests
from bs4 import BeautifulSoup


URL = 'https://www.walser.com/inventory/new-2019-mercedes-benz-sprinter-2500-class-rwd-full-size-passenger-van-wdzpf0cd9kp100071'
 
page = requests.get(URL)


def scrap_xml_file(page):
    soup = BeautifulSoup(page.content, 'xml')
    for div in soup.find_all('loc'):
        try:
            string = str(div)
            string = string.split('<loc>')
            string = string[1].split('</loc>')
            string = string[0]
            print(string)
        except:
            pass

def scrap_image(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    for tag in soup.find_all('meta'):
        if tag.get('property') == 'og:image' or tag.get('name') == 'og:image':
            print(f"VDP Image URL: {tag.get('content')}")
        
        if vdp_url == dealer_inspire:
            print(f'{page}')
            print()

        if vdp_url == dealer_dot_com:
            if tag.get('name') == 'og:title':
                print(f"VDP Image URL: {tag.get('content')}")
                print()
        if vdp_url == cdk:
            if tag.get('name') == 'keywords':
                print(f"VDP Image URL: {tag.get('content')}")
                print()


def return_page(page):
    soup = BeautifulSoup(page.content, 'html5lib')
    print(soup)

scrap_image(page)