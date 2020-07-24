from O_Days import *
from O_Selenium import *



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

    def find_vdp(self, Domain, VIN, acquire_image):
        self.driver.get(f'{Domain}{self.Search}{VIN}')
        success = True
        try:
            self.driver.find_element_by_xpath('//*[@id="compareForm"]/div/div[2]/ul/li/div[1]/div/div[1]/a[1]/img').click()
        except:
            success = False
        url = self.driver.current_url
        
        if url == f'{Domain}{self.SearchFailed}{VIN}':
            success = False
        UrlPicture = None
        while success:
            
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

def find_vdp(self, Domain, VIN, acquire_image):
    self.driver.get(f'https://www.google.com/search?q={VIN}')
    
    for row in range(1,10):
        element = self.driver.find_element_by_xpath(f'/html/body/div[6]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[{row}]/div/div[1]/a')
        query_url = element.value()
        print(query_url)
            if f'{Domain}' in query_url and f'{Domain}' in query_url:

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