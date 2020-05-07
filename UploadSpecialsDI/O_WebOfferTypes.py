from O_Days import Today
from R_VehicleSpecialsNew import VehicleSpecial    

class OfferTypeContainer(VehicleSpecial):
    GROUP = 0
    ONEPAY = 1

    def __init__(self):
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
        
        if self.website.Domain == 'https://www.walserautocampus.com/':
            print('campus')
            self.value_list = [self.website.OfferType.WAC_Brand, self.website.OfferType.WAC_Fixed, self.website.OfferType.WAC3_Fixed, self.website.OfferType.WAC4_Fixed]
            
        elif self.website.Domain == 'https://www.walser.com/':
            print('not campus')
            self.value_list = [self.website.OfferType.WAG_Fixed, self.website.OfferType.WAG_StateCode, self.website.OfferType.WAG_New, self.website.OfferType.WAG_Walser]
        else:
            self.value_list = [self.website.OfferType.StoreType]
        print(f'List: {self.value_list}')
        self.offer_type_clicks(self)
    
    def select_one_pay_offertypes(self):
        
        self.value_list = [self.website.OfferType.OnePay]
        self.offer_type_clicks(self)

    def run(self, input):
        if input == OfferTypeContainer.GROUP:
            Today.time_taken(self.select_group_offertypes)
        elif input == OfferTypeContainer.ONEPAY:
            Today.time_taken(self.select_one_pay_offertypes)
