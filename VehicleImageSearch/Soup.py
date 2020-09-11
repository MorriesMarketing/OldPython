import requests
from bs4 import BeautifulSoup
import re


class Soup():
    DEALER_INSPIRE_XML = 'dealer-inspire-inventory/inventory_sitemap.xml'
    CDK_XML = 'sitemap-inventory-sincro.xml'
    DEALER_DOT_COM_XML = 'sitemap.xml'

    def __init__(self,Domain,Flag):
        self.domain = Domain
        self.flag = Flag
        self.sitemap_xml = f'{Domain}{Flag}'
    
    def identify_xml_page(self):
        page = None
        if self.domain == None or self.flag == None:
            pass
        else:
            if self.flag == Soup.DEALER_INSPIRE_XML:
                page = f'{self.domain}{Soup.DEALER_INSPIRE_XML}'
            elif self.flag == Soup.CDK_XML:
                page = f'{self.domain}{Soup.CDK_XML}'
            elif self.flag == Soup.DEALER_DOT_COM_XML:
                page = f'{self.domain}{Soup.DEALER_DOT_COM_XML}'
        
        return page

    @staticmethod
    def scrape_xml_page(Domain, Page):
        print(f'Scraping XML Page: {Page} for Inventory URLs')
        page = requests.get(Page)
        soup = BeautifulSoup(page.content, 'xml')
        pages = []
        for div in soup.find_all('loc'):
            try:
                string = str(div)
                string = string.split('<loc>')
                string = string[1].split('</loc>')
                string = string[0]
                if f'{Domain}new' in string or f'{Domain}used' in string or f'{Domain}inventory/' in string or f'{Domain}VehicleDetails/' in string:
                    string = string.split(f'{Domain}')
                    string = string[1]
                    last_item = string[-1]
                    if last_item == '/':
                        string = string[:-1]
                    pages.append(string)
            except:
                pass
        print(f'Completed Scraping {Page} - Possible VDPs Found: {len(pages)}')
        return pages

    @staticmethod
    def trim_list_of_pre_existing_values(list1,list2):
        print(f'Checking VDPs found to current Database list')
        if list1 == None:
            print(f'Image list is empty')
        else:
            for l1 in list1:
                for l2 in list2:
                    if l1.UrlVdp == l2:
                        list2.remove(l2)
        print(f'Completed Check')
        return list2

    @staticmethod
    def vin_checker(string):
        spliter_list = ['-',',',' ','|',':']
        last_item = string[-1]
        if last_item == '/':
            string = string[:-1]

        for sl in spliter_list:
            string_list = string.split(sl)
            for s in string_list:
                pattern = re.compile(r"^[a-hj-npr-zA-HJ-NPR-Z0-9]{17}$")
                if bool(pattern.match(s)):
                    return s

        return None

    def scrap_image_and_vin(self, Page):
        print(f'Scanning Page: {Page}')
        page = requests.get(Page)
        soup = BeautifulSoup(page.content, 'html.parser')
        vin = self.vin_checker(Page)
        imageurl = None
        content = None
        #Search through 'meta' data of website
        for tag in soup.head.find_all('meta'):
            if tag.get('property') == 'og:image' or tag.get('name') == 'og:image':
                imageurl = tag.get('content')
        
            elif self.flag == self.DEALER_DOT_COM_XML and vin == None:
                if tag.get('name') == 'og:title':
                    content = tag.get('content')
                    vin = self.vin_checker(content)
                elif tag.get('name') == 'y_key' and vin == None:
                    content = tag.get('content')
                    vin = self.vin_checker(content)

            elif self.flag == self.CDK_XML and vin == None:
                if tag.get('name') == 'keywords':
                    content = tag.get('content')
                    vin = self.vin_checker(content)
        #Search through 'input' data of website
        if vin == None and self.flag == self.DEALER_DOT_COM_XML:
            for tag in soup.find_all('input'):
                if tag.get('name') == 'vin':
                    content = tag.get('value')
                    vin = self.vin_checker(content)

        if imageurl == None or imageurl == 'None':
            for tag in soup.find_all('link'):
                if tag.get('rel') == 'image_src':
                    imageurl = f"{self.domain}{tag.get('href')}"
        
        data = {
            'ImageUrl': imageurl,
            'VIN': vin
            }
        return data