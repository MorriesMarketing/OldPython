    
class OfferTypeContainer():
   
    def __init__(self, v, driver, w, ot):
        
        self.v = v
        self.driver = driver
        self.w = w
        self.ot = ot
        self.value_list = []

    def offer_type_clicks(self):
        element = self.driver.find_element_by_xpath('//*[@id="typediv"]/button/span[2]')
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        print('found element')

        while True:
            try:
                for i in self.value_list:
                    print(i)
                    self.driver.find_element_by_id(i).click()
                    sleep(.1)
                break
            except:
                sleep(.1)   
      
    def select_group_offertypes(self):
        domain = self.w.Domain
        if domain == 'https://www.walserautocampus.com/':
            print('campus')
            self.value_list = [self.ot.WAC_Brand, self.ot.WAC_Fixed, self.ot.WAC3_Fixed, self.ot.WAC4_Fixed]
        elif domain == 'https://www.walser.com/':
            print('not campus')
            self.value_list = [self.ot.WAG_Fixed, self.ot.WAG_StateCode, self.ot.WAG_New, self.ot.WAG_Walser]
        else:
            self.value_list = [self.ot.StoreType]
        print(f'List: {value_list}')
        self.offer_type_clicks(self)

    def select_one_pay_offertypes(self):
        
        self.value_list = [self.ot.OnePay]
        self.offer_type_clicks(self)
