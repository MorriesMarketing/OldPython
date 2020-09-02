import requests
from bs4 import BeautifulSoup


class Soup():
    DEALER_INSPIRE_XML = 'dealer-inspire-inventory/inventory_sitemap.xml'
    CDK_XML = 'sitemap-inventory-cdk.xml'
    DEALER_DOT_COM_XML = 'sitemap.xml'

    def __init__(self,Domain,Flag):
        self.domain = Domain
        self.flag = Flag
    
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
                    pages.append(string)
            except:
                pass
        print(f'{Page} - VDPs Found: {len(pages)}')
        return pages



    def scrap_image(self, Page):
        page = requests.get(Page)
        soup = BeautifulSoup(page.content, 'html.parser')
        for tag in soup.find_all('meta'):
            if tag.get('property') == 'og:image' or tag.get('name') == 'og:image':
                
                print(f"VDP Image URL: {tag.get('content')}")
                print(Page)
                print()
        
            #if self.flag == Soup.DEALER_INSPIRE_XML:
            #    print(f'{Page}')
            #    print()

            elif self.flag == Soup.DEALER_DOT_COM_XML:
                if tag.get('name') == 'og:title':
                    print(f"VDP Image URL: {tag.get('content')}")
                    print()
            elif self.flag == Soup.CDK_XML:
                if tag.get('name') == 'keywords':
                    print(f"VDP Image URL: {tag.get('content')}")
                    print()