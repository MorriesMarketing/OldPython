from U_JsTextBox import JsTextBox
from O_Days import Today
from U_VehicleSpecialObject import VehicleSpecialObject

class TabOfferContainer(VehicleSpecialObject):
    GROUP = 0
    ONEPAY = 1

    def __init__(self):
        self.order_list = []
    
    
    def edit_button_links(self):
        self.driver.find_element(By.LINK_TEXT, "Offer").click()# Click OFFER Tab 
        text_box1 = self.driver.find_element(By.ID, "acf-field_569c2e95a3d27")
        JsTextBox.fix_text_box(driver=self.driver, text="View Vehicle Details", element_path=text_box1)#Primary Button Label

        vehicle = f'{self.vehicle.Year} {self.vehicle.MakeName} {self.vehicle.ModelName}'.replace(' ','-')
        text_path = f'/new-vehicles/#action=im_ajax_call&perform=get_results&search={vehicle}&page=1'
        element_path = self.driver.find_element(By.ID, "acf-field_569c2aa7a3d24")#Secondary Button Link
        JsTextBox.fix_text_box(driver=self.driver, text=text_path, element_path=element_path)
        text_path = "View Inventory"
        element_path = driver.find_element(By.ID, "acf-field_569c2bb9a3d26")
        JsTextBox.fix_text_box( driver=self.driver, text=text_path, element_path=element_path)#Secondary Link 

    def offer_labels(self):
        for i in self.order_list:
            print(i)
            if i[1] == 'True':
                for o in self.vehicle.Offers:
                    if o.OfferTypeID == i[0]:
                        self.driver.find_element_by_link_text("Add Line").click()
        count = 0
        for i in self.order_list:
            print(i)
            if i[1] == 'True':
                for o in self.vehicle.Offers:
                    print(f'o.OfferTypeID: {o.OfferTypeID}\ni: {i[0]}')
                    if o.OfferTypeID == i[0]:
                        table = self.driver.find_elements_by_css_selector('.ui-sortable')[6]
                        row = table.find_elements_by_css_selector('.acf-row')[count]
                        tile = row.find_elements_by_css_selector('.acf-field')[0]
                        child1 = tile.find_element_by_css_selector('.acf-input')
                        child2 = child1.find_element_by_css_selector('.acf-input-wrap')
                        Input = child2.find_element_by_css_selector('input')
                        # OFFER
                        if o.OfferTypeID == 5:
                            JsTextBox.fix_text_box(driver=self.driver, text=o.DueAtSigning, element_path=Input)
                        else:
                            JsTextBox.fix_text_box(driver=self.driver, text=o.LeaseOffer, element_path=Input)

                        table = self.driver.find_elements_by_css_selector('.ui-sortable')[6]
                        row = table.find_elements_by_css_selector('.acf-row')[count]
                        tile = row.find_elements_by_css_selector('.acf-field')[1]
                        child1 = tile.find_element_by_css_selector('.acf-input')
                        child2 = child1.find_element_by_css_selector('.acf-input-wrap')
                        Input = child2.find_element_by_css_selector('input')
                        # SPECIAL
                        if o.OfferTypeID == 5:
                            onepay = ''
                            onepay += f'<div style="font-size: 16px;">{o.LeaseSpecial}</div>'
                            onepay += f'<div style="font-size: 12px;">{o.LeaseOffer}</div>'
                            JsTextBox.fix_text_box(driver=self.driver, text=onepay, element_path=Input)
                        else:
                            special = ''
                            special += '<div style="font-size: 16px;">'
                            special += str(o.LeaseSpecial)
                            special += '</div>'
                            if 'APR Finance Special' in o.LeaseSpecial:
                                special += ''
                            else:
                                special += '<div style="font-size: 12px;"><strong>'
                                special += str(o.DueAtSigning)
                                special += '</strong> Due at Signing</div>'
                            JsTextBox.fix_text_box(driver=self.driver, text=special, element_path=Input)

                        count += 1

    def offer_description(self):
        media_edit = self.driver.find_element(By.XPATH, f"/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div[2]/div/div[3]/div[1]/div[{self.website.RegionID}]/div/div[30]/div[2]/div/div[2]/textarea")
        text = ''
        text += '<center>Located at: ' + self.website.OfferType.DealerName + '</center>\n'
        text += f'<ul>All Walser branded locations offer: <li>FREE test drive delivery option for customers located in '
        if v.State == 'KS':
            text += f'the greater Wichita metropolitan area and beyond. '
        elif v.State == 'MN':
            text += f'the twin cities metro area. '
        text += f'Test drive delivery based on schedule availability and distance.*</li>'
        text += f'<li>FREE vehicle home delivery option for customers located up to '
        if v.State == 'KS':
            text += f'120'
        elif v.State == 'MN':
            text += f'100' 
        text += f' miles from {self.website.OfferType.DealerName}. Nationwide home delivery is available, please contact dealer for a personalized quote.*'
        text += f'</li></ul>'
        #media_edit.send_keys(text)
        JsTextBox.fix_text_box(driver=self.driver, text=text, element_path=media_edit)

    def offer_disclaimer(self):
        text_area = self.driver.find_element_by_id("acf-field_5577c0782430f")
        disclaimers = ''
        if self.vehicle.MakeName == 'Toyota':
            disclaimers += 'ALL OFFERS INCLUDE $100 DOC FEE'
        disclaimers += '\n<ol><strong>'
        disclaimers += str(self.vehicle.Year) + ' '
        disclaimers += str(self.vehicle.MakeName) + ' '
        disclaimers += str(self.vehicle.ModelName) + ' '
        disclaimers += str(self.vehicle.Trim.replace('""', r'\"'))
        disclaimers += ' Lease and Finance Deals</strong>'
        for i in order_list:
            if i[1] == 'True':
                for o in self.vehicle.Offers:
                    if o.OfferTypeID == i[0]:
                        disclaimers += '\n\n<li><strong>'
                        disclaimers += str(o.LeaseOffer)
                        disclaimers += str(o.LeaseSpecial)
                        disclaimers += '</strong></li>\n'
                        disclaimers += str(o.Disclaimer)
        disclaimers += '</ol>'
        disclaimers += '*Delivery availability may vary, some exclusions apply. Message dealer for details.'
        JsTextBox.fix_text_box(driver=self.driver, text=disclaimers, element_path=text_area)
    
    def use_offer_tab_group(self):
        while True: # Offer Tab
            try:
                Today.time_taken(self.edit_button_links)
                
                self.order_list = [[3, self.website.OfferType.OfferTypeID3], [2, self.website.OfferType.OfferTypeID2], [1, self.website.OfferType.OfferTypeID1], [4, self.website.OfferType.OfferTypeID4], [6, self.website.OfferType.OfferTypeID6], [7, self.website.OfferType.OfferTypeID7]]
                Today.time_taken(self.offer_labels)
                Today.time_taken(self.offer_description)                
                Today.time_taken(self.offer_disclaimer)
                break
            except:
                assert self.driver.switch_to.alert.text == "Vehicle Stock or VIN not found"
                continue

    def use_offer_tab_onepay(self):
        while True: # Offer Tab
            try:
                Today.time_taken(self.edit_button_links)
                
                self.order_list = [[5, self.website.OfferType.OfferTypeID5]]
                Today.time_taken(self.offer_labels)
                Today.time_taken(self.offer_description)                
                Today.time_taken(self.offer_disclaimer)
                break
            except:
                assert self.driver.switch_to.alert.text == "Vehicle Stock or VIN not found"
                continue

    def run(self,input):
        if input == TabOfferContainer.GROUP:
            self.use_offer_tab_group()
        elif input == TabOfferContainer.ONEPAY:
            self.use_offer_tab_onepay()