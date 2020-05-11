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

        offer_input = self.driver.find_element_by_xpath(self.ao_tab_step2_offer_path(1, 2))
        offer_input_css = offer_input.find_element_by_css_selector('input')
        offer_type_input = self.driver.find_element_by_xpath(self.ao_tab_step2_offer_path(1, 3))
        offer_type_input_css = offer_type_input.find_element_by_css_selector('input')
        for o in self.vehicle.Offers:
            if '10% Down Lease Special' in o.LeaseSpecial or 'OEM' in o.LeaseSpecial:
                JsTextBox.fix_text_box(driver=self.driver,text=o.LeaseOffer,element_path=offer_input_css)
                special = f'\<br\>{o.LeaseSpecial}\<br\>{o.DueAtSigning} Due at Signing'
                JsTextBox.fix_text_box(driver=self.driver,text=special,element_path=offer_type_input_css)
                
        offer_input = self.driver.find_element_by_xpath(self.ao_tab_step2_offer_path(2, 2))
        offer_input_css = offer_input.find_element_by_css_selector('input')
        text = "CLICK HERE FOR MORE OFFERS"
        JsTextBox.fix_text_box(driver=self.driver,text=special,element_path=offer_input_css)

    def run(self):
        Today.time_taken(self.ao_tab_step1)
        Today.time_taken(self.ao_tab_step2)