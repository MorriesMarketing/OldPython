from O_Days import Today
from U_VehicleSpecialObject import VehicleSpecialObject
from O_Selenium import SeleniumDrivers
from time import sleep


class OfferTypeContainer(VehicleSpecialObject):
    GROUP = 0
    ONEPAY = 1

    def offer_type_clicks(self):
        element = self.driver.find_element_by_xpath('//*[@id="typediv"]/button/span[2]')
        SeleniumDrivers.move_to_element(driver=self.driver,element=element)
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
        self.offer_type_clicks()
    
    def select_one_pay_offertypes(self):
        
        self.value_list = ['in-type-801']
        self.offer_type_clicks()

    def error_check(self):
        error_occured = False
        try:
            assert self.driver.switch_to.alert.text == "Vehicle Stock or VIN not found"
            error_occured = True
        except:
            error_occured = False
        print(f'\n\tError: {error_occured}\n')
        return error_occured

    def run(self, input):
        success_check = True
        if self.error_check():
            success_check = False
        if input == OfferTypeContainer.GROUP:
            Today.time_taken(self.select_group_offertypes)
        elif input == OfferTypeContainer.ONEPAY:
            Today.time_taken(self.select_one_pay_offertypes)

        return success_check
