from time import sleep

class DIWebsite():
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
        self.Region = krawgs['RegionID']
        self.State = krawgs['State']
        self.Brand = krawgs['Brand']
        self.Driver = None

    def __repr__(self):
        return f"{self.Domain} {self.Brand}"
    
    def DI_SignIn(self):
        self.Driver.maximize_window()
        print(f'Navigating to {self.Domain}')
        self.Driver.get(self.Domain + 'wp/wp-login.php')
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
