from O_Days import Today
from R_VehicleSpecialsNew import VehicleSpecial

class AdvancedOptions(VehicleSpecial, Today):

    def __init__(self):
        print('Created AdvancedOptions Class')


    def ao_tab_step1(self):
        self.driver.find_element_by_link_text( "Advanced Options").click()
        self.driver.find_element_by_link_text( "Add Discount").click()
        self.driver.find_element_by_link_text( "Add Discount").click()

    def ao_tab_step2_offer_path(self, count, table): 
        if self.vehicle.Brand == 'FCA' and 'https://www.walsercjd.com/' in self.driver.current_url or 'https://www.walserpolarmazda.com/' in self.driver.current_url:
            return f'/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div[2]/div/div[3]/div[1]/div[{w.Region}]/div/div[36]/div[2]/div/table/tbody/tr[{count}]/td[{table}]/div/div'
        return f'/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div[2]/div/div[3]/div[1]/div[{w.Region}]/div/div[37]/div[2]/div/table/tbody/tr[{count}]/td[{table}]/div/div'

    def ao_tab_step2(self):

        offer_input = self.driver.find_element_by_xpath(self.ao_tab_step2_offer_path(1, 2))
        offer_input_css = offer_input.find_element_by_css_selector('input')
        offer_type_input = self.driver.find_element_by_xpath(self.ao_tab_step2_offer_path(1, 3))
        offer_type_input_css = offer_type_input.find_element_by_css_selector('input')
        for o in self.vehicle.Offers:
            if '10% Down Lease Special' in o.LeaseSpecial or 'OEM' in o.LeaseSpecial:
                self.driver.execute_script(f'arguments[0].value = "{o.LeaseOffer}";', offer_input_css)
                special = f'\<br\>{o.LeaseSpecial}\<br\>{o.DueAtSigning} Due at Signing'
                self.driver.execute_script(f'arguments[0].value = "{special}";', offer_type_input_css)
                
        offer_input = self.driver.find_element_by_xpath(self.ao_tab_step2_offer_path(driver, self.website.RegionID, 2, 2))
        offer_input_css = offer_input.find_element_by_css_selector('input')
        self.driver.execute_script('arguments[0].value = "CLICK HERE FOR MORE OFFERS";', offer_input_css)
        
    def use_advanced_options_tab(self):
        while True: # Advanced Options Tab
            self.time_taken(self.ao_tab_step1)
            self.time_taken(self.ao_tab_step2)
            break
