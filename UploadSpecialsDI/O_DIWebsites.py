from time import sleep

class DIWebsite():
    DI_LOGIN = 'wp/wp-login.php'
    DI_EDIT = 'wp/wp-admin/edit.php?post_type=special_offers'
    DI_POST = 'wp/wp-admin/post-new.php?post_type=special_offers'
    DI_REORDER = 'wp/wp-admin/edit.php?post_type=special_offers&page=order-post-types-special_offers' 
    DI_RELOADCACHE = 'wp/wp-admin/edit.php?post_type=special_offers'
    DI_INVENTORY_PAGE = 'wp/wp-admin/edit.php?post_type=inventory&page=inventory_listview'
    DI_INVENTORY_VIN = 'wp/wp-admin/edit.php?post_type=inventory&page=inventory_listview&action=edit&vin='

    def __init__(self, **krawgs):
        self.WebsiteID = krawgs['WebsiteID']
        self.Domain = krawgs['Domain']
        self.UserName = krawgs['UserName']
        self.Password = krawgs['Password']
        self.RegionID = krawgs['RegionID']
        self.State = krawgs['State']
        self.Brand = krawgs['Brand']
        self.OfferTypeID1 = krawgs['OfferTypeID1']
        self.OfferTypeID2 = krawgs['OfferTypeID2']
        self.OfferTypeID3 = krawgs['OfferTypeID3']
        self.OfferTypeID4 = krawgs['OfferTypeID4']
        self.OfferTypeID5 = krawgs['OfferTypeID5']
        self.OfferTypeID6 = krawgs['OfferTypeID6']
        self.OfferTypeID7 = krawgs['OfferTypeID7']
        self.Driver = None

    def __repr__(self):
        return f"{self.Domain} {self.Brand}"
    
    def DI_SignIn(self):
        self.Driver.maximize_window()
        print(f'Navigating to {self.Domain}')
        self.Driver.get(f'{self.Domain}{DIWebsite.DI_LOGIN}')
        sleep(1)
        #1. navigate to website
        self.Driver.find_element_by_id('user_login').send_keys(self.UserName)
        print(self.UserName)
        #2. Enter text in user name text box
        self.Driver.find_element_by_id('user_pass').send_keys(self.Password)
        print(self.Password)
        #3. Enter text in password box
        self.Driver.find_element_by_id('wp-submit').click()
        #4. Click sign in

    def delete_all_specials(self):
        print('Running delete_offers')
        while True:
            try:
                edit = f'{self.Domain}{DIWebsite.DI_EDIT}'
                self.driver.get(edit)
                break
            except:
                sleep(.1)
        while True:
            try:
                number = self.driver.find_element_by_xpath('//*[@id="wpbody-content"]/div[3]/ul/li[1]/a/span').text
                if number != '(0)':
                    try:
                        self.driver.find_element_by_xpath('//*[@id="cb-select-all-1"]').click()
                        self.driver.find_element_by_xpath('//*[@id="bulk-action-selector-top"]').click()
                        self.driver.find_element_by_xpath('//*[@id="bulk-action-selector-top"]/option[3]').click()
                        self.driver.find_element_by_xpath('//*[@id="doaction"]').click()
                    except:
                        sleep(1)
                else:
                    break
            except:
                sleep(.1)
