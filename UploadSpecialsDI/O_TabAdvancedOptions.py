

class AdvancedOptions():

    def __init__(self, v, driver, w):
    
        self.driver = driver
        self.v = v
        self.w = w


    def ao_tab_step1(self):
        self.driver.find_element(By.LINK_TEXT, "Advanced Options").click()
        self.driver.find_element(By.LINK_TEXT, "Add Discount").click()
        self.driver.find_element(By.LINK_TEXT, "Add Discount").click()


    def ao_tab_step2_offer_path(self, count, table): 
        if self.v.Brand == 'FCA' and 'https://www.walsercjd.com/' in self.driver.current_url or 'https://www.walserpolarmazda.com/' in self.driver.current_url:
            return f'/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div[2]/div/div[3]/div[1]/div[{Region}]/div/div[36]/div[2]/div/table/tbody/tr[{count}]/td[{table}]/div/div'
        return f'/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div[2]/div/div[3]/div[1]/div[{Region}]/div/div[37]/div[2]/div/table/tbody/tr[{count}]/td[{table}]/div/div'


    def ao_tab_step2(self):

        offer_input = self.driver.find_element_by_xpath(self.ao_tab_step2_offer_path(self, 1, 2))
        offer_input_css = offer_input.find_element_by_css_selector('input')
        offer_type_input = self.driver.find_element_by_xpath(self.ao_tab_step2_offer_path(self, 1, 3))
        offer_type_input_css = offer_type_input.find_element_by_css_selector('input')
        for o in self.v.Offers:
            if '10% Down Lease Special' in o.LeaseSpecial or 'OEM' in o.LeaseSpecial:
                self.driver.execute_script(f'arguments[0].value = "{o.LeaseOffer}";', offer_input_css)
                special = f'\<br\>{o.LeaseSpecial}\<br\>{o.DueAtSigning} Due at Signing'
                self.driver.execute_script(f'arguments[0].value = "{special}";', offer_type_input_css)
                
        offer_input = self.driver.find_element_by_xpath(self.ao_tab_step2_offer_path(driver, self.w.RegionID, 2, 2))
        offer_input_css = offer_input.find_element_by_css_selector('input')
        self.driver.execute_script('arguments[0].value = "CLICK HERE FOR MORE OFFERS";', offer_input_css)
        

    def use_advanced_options_tab(self):
        while True: # Advanced Options Tab
            Today.time_taken(self.ao_tab_step1, self)
            Today.time_taken(self.ao_tab_step2, self)
            break
