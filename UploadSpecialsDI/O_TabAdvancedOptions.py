from O_Days import Today
from U_VehicleSpecialObject import VehicleSpecialObject
from U_JsTextBox import JsTextBox

class TabAdvancedOptions(VehicleSpecialObject):

    def ao_tab_step1(self):
        self.driver.find_element_by_link_text( "Advanced Options").click()
        self.driver.find_element_by_link_text( "Add Discount").click()
        self.driver.find_element_by_link_text( "Add Discount").click()

    def ao_tab_step2_offer_path(self, count, table): 
        if self.vehicle.Brand == 'FCA' and 'https://www.walsercjd.com/' in self.driver.current_url or 'https://www.walserpolarmazda.com/' in self.driver.current_url:
            return f'/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div[2]/div/div[3]/div[1]/div[{self.website.RegionID}]/div/div[36]/div[2]/div/table/tbody/tr[{count}]/td[{table}]/div/div'
        return f'/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div[2]/div/div[3]/div[1]/div[{self.website.RegionID}]/div/div[37]/div[2]/div/table/tbody/tr[{count}]/td[{table}]/div/div'

    def ao_tab_step2(self):
        #This decides which offer to run for the VRP display.
        
        count = 10
        while True:
            try:
                self.driver.find_element_by_xpath(self.ao_tab_step2_offer_path(1, 2))
                break
            except:
                sleep(.1)
                count -= 1
            if count == 0:
                break
        

        discount_value1 = self.driver.find_element_by_xpath(self.ao_tab_step2_offer_path(1, 2))
        input_discount_value1 = discount_value1.find_element_by_css_selector('input')

        discount_label1 = self.driver.find_element_by_xpath(self.ao_tab_step2_offer_path(1, 3))
        input_discount_label1 = discount_label1.find_element_by_css_selector('input')
        for o in self.vehicle.Offers:
            if '10% Down Lease Special' in o.LeaseSpecial or 'OEM' in o.LeaseSpecial:
                JsTextBox.fix_text_box(driver=self.driver, text=o.LeaseOffer, element_path=input_discount_value1)
                special = f'<br>{o.LeaseSpecial}<br>{o.DueAtSigning} Due at Signing'
                JsTextBox.fix_text_box(driver=self.driver, text=special, element_path=input_discount_label1)
                
        discount_value2 = self.driver.find_element_by_xpath(self.ao_tab_step2_offer_path(2, 2))
        input_discount_value2 = discount_value2.find_element_by_css_selector('input')
        text = "CLICK HERE FOR MORE OFFERS"
        JsTextBox.fix_text_box(driver=self.driver,text=text,element_path=input_discount_value2)

    
    def run(self):
        success_check = True
        try:
            Today.time_taken(self.ao_tab_step1)
            Today.time_taken(self.ao_tab_step2)
        except:
            success_check = False
       
        return success_check