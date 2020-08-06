from O_Days import *
from O_Selenium import *
import requests
from bs4 import BeautifulSoup


class Website_DealerInspire(Selenium):
    def __init__(self, Driver):
        self.LoginPage = 'wp/wp-admin/'
        self.SrpNew = ''
        self.SrpUsed = ''
        self.SrpAll = ''
        self.SpecialsNew = ''
        self.SpecialsUsed = ''
        self.SpecialsAll = ''

class Website_DealerDotCom():
    def __init__(self):
        self.LoginPage = 'https://dealer.signin.coxautoinc.com/solutionlauncher'
        self.Search = 'all-inventory/index.htm?search='     
        self.SearchFailed = 'all-inventory/no-results.htm?category=AUTO&search='
        self.SpecialsNew = ''
        self.SpecialsUsed = ''
        self.SpecialsAll = ''
        self.driver = Selenium.CHROME

    def login_to_website(self,UserName,Password):
        self.driver.get(self.LoginPage)
        self.driver.find_element_by_id('solutionInputRequired').click()
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/div[1]/select/option[3]').click()
        self.driver.find_element_by_id('submit').click()
        self.driver.find_element_by_id('username').send_keys(UserName)
        self.driver.find_element_by_id('signIn').click()


    def search_vehicle_page(self, Domain,SRP_Query, VIN, acquire_image):
        page = self.driver.get(f'{Domain}{SRP_Query}{VIN}')
        '/html/body/div[4]/div[2]/div[1]/div/div[2]/div/div[3]/div/div[2]/ul/li[1]/img'
        '/html/body/div[4]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/ul/li[1]/img'

        '/html/body/div[4]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/ul/li[1]/img'
        '/html/body/div[4]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/ul/li[1]/img'
        '/html/body/div[4]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/ul/li[1]/img'
        '#media1-app-root > div > div.blurred-container > div.photo-carousel.image-mode.add-border > div > div.slider-frame > ul > li:nth-child(1) > img'
        '#media1-app-root > div > div.blurred-container > div.photo-carousel.image-mode.add-border > div > div.slider-frame > ul > li:nth-child(1) > img'
        '#media1-app-root > div > div.blurred-container > div.photo-carousel.image-mode.add-border > div > div.slider-frame > ul > li:nth-child(1) > img'

        '#media1-app-root > div > div.blurred-container > div.photo-carousel.image-mode.add-border > div > div.slider-frame > ul > li:nth-child(1) > img '

        '#compareForm > div > div.bd > ul:nth-child(1) > li:nth-child(1) > div.hproduct.auto.subaru > div > div.media > a'

        '#compareForm > div > div.bd > ul > li > div.hproduct.auto.audi > div > div.media > a'
        '#media1-app-root > div > div.blurred-container > div.photo-carousel.image-mode.add-border > div > div.slider-frame > ul > li:nth-child(1) > img'

        '#dynamic_filters > tr:nth-child(3) > td.results.gridview > div.grid-view-results-wrapper > div.vehicle-wrap > div.hidden-xs.vehicle.grid-view.new-vehicle.publish.vehicle-visited-grid > div.vehicle-image > a'
        '/html/body/div[3]/div[6]/div[2]/div/main/div/div/div/table/tbody/tr[3]/td[2]/div[1]/div[1]/div[1]/div[3]/a'
        '#gallery-carousel > div.owl-wrapper-outer > div > div:nth-child(1) > div > img'
        '//*[@id="gallery-carousel"]/div[1]/div/div[1]/div/img'

        '#dynamic_filters > tr:nth-child(3) > td.results.gridview > div.grid-view-results-wrapper > div.vehicle-wrap > div.hidden-xs.vehicle.grid-view.new-vehicle.publish.vehicle-visited-grid > div.vehicle-image > a'
        '/html/body/div[4]/div[6]/div[2]/div/main/div/div/div/table/tbody/tr[3]/td[2]/div[1]/div[1]/div[1]/div[3]/a'
        '#gallery-carousel > div.owl-wrapper-outer > div > div:nth-child(1) > div > img'
        '/html/body/div[3]/div[6]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div/div[1]/div/img'

        '#dynamic_filters > tr:nth-child(3) > td.results.gridview > div.grid-view-results-wrapper > div.vehicle-wrap > div.hidden-xs.vehicle.grid-view.new-vehicle.publish.vehicle-visited-grid > div.vehicle-image > a'
        '#gallery-carousel > div.owl-wrapper-outer > div > div:nth-child(1) > div > img'

        '#card-view\/card\/23d16170-46df-4977-9bd2-3e7be7bdac31 > div.content > div.media > figure > a'
        '/html/body/main/section/div[3]/section[1]/div[3]/section[2]/div[3]/section/div[1]/div[3]/figure/a'
        '#card-view\/card\/23d16170-46df-4977-9bd2-3e7be7bdac31 > div.content > div.media > figure > a'
        '#vdp-photos-dealershipPhotoGallery-557b6520-db08-4297-a3a1-b889db348e62 > div.content > div.media > figure > img'
        '/html/body/main/section/div[3]/section[2]/div[3]/section[1]/div[3]/section[1]/div[1]/div[2]/figure/img'
        '#vdp-photos-manufacturerPhotoGallery-caac439d-c9f8-4abd-8dea-7ea5541731c2 > div.content > div.media > figure > img'
        '/html/body/main/section/div[3]/section[2]/div[3]/section[1]/div[3]/section/div[1]/div[2]/figure/img'

    def find_vdp(self, Domain, VIN, acquire_image):
        print('Running Find VDP')        
        page = requests.get(f'https://www.google.com/search?q={VIN}')
        soup = BeautifulSoup(page.content, 'html.parser')
        url = ''
        for link in soup.find_all('a'):
            if f'{Domain}' in link['href']:
                print(link['href'])
                url = link['href']
                break
        success = True
        
        url = url.split('=')
        print(url)
        url = url[1].split('&')
        print(url)
        url = url[0]
        print(url)
        page = requests.get(f'{Domain}')
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        print(soup)
        for image in soup.find_all('img'):
            print(image['src'])
            if f'http://images.dealer.com/' in image['src']:
                print('SRC')
                print(link['src'])
                url = link['href']
                break


        UrlPicture = None
        while success:
            self.driver.get(url)
            try:
                if acquire_image == True:
                    image = self.driver.find_element_by_xpath('//*[@id="media1-app-root"]/div/div[2]/div/div[2]/ul/li/div/img')
                    '//*[@id="media1-app-root"]/div/div[2]/div/div[2]/ul/li[1]/div/img'
                    UrlPicture = image.get_attribute('src')
                print('Found Everything')
                break
            except:
                if url == f'{Domain}{self.SearchFailed}{VIN}':
                    success = False
                    break
                else:
                    print('Found Nothing')
                    sleep(.5)
        return [success,url,UrlPicture]



    #URL = 'https://www.nissankendall.com/inventory/new-2019-nissan-leaf-sv-fwd-4d-hatchback-1n4az1cp6kc321458'
    #
    #page = requests.get(URL)
    #soup = BeautifulSoup(page.content, 'html.parser')
    #
    #for div in soup.find_all('div', class_='swiper-slide'):
    #    if 'data-src' in div.img.attrs.keys():
    #        print(div.img['data-src'])
    #        break


    #def find_vdp(self, Domain, VIN, acquire_image):
    #    print('Running Find VDP')
    #    page = requests.get(f'https://www.google.com/search?q={VIN}')
    #    soup = BeautifulSoup(page.content, 'html.parser')
    #    
    #    for link in soup.find_all('a'):
    #        if f'{Domain}new' in link['href']:
    #            print(link['href'])
    #            break
    
        #for row in range(1,10):
        #    element = self.driver.find_element_by_xpath(f'/html/body/div[6]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[{row}]/div/div[1]/a')
        #    query_url = element.text
        #    print(query_url)
        #    if f'{Domain}' in query_url and f'{VIN}' in query_url:
        #        element.click()

class Website_CDK(Selenium):
    def __init__(self):
        self.LoginPage = ''
        self.SrpNew = ''
        self.SrpUsed = ''
        self.SrpAll = ''
        self.SpecialsNew = ''
        self.SpecialsUsed = ''
        self.SpecialsAll = ''

#website = Website_DealerDotCom()
#image_data = website.find_vdp('https://www.walser-subaru.com/','4S4WMAPD7L3476130')
#print(image_data)

#website.login_to_website('User','Pass')