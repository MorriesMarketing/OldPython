from U_JsTextBox import JsTextBox
from O_Days import *

class OfferContainer():

    def __init__(self, v, driver, w, ot):
        self.v = v
        self.driver = driver
        self.w = w
        self.ot = ot
        self.order_list = []


    def edit_button_links(self):
        self.driver.find_element(By.LINK_TEXT, "Offer").click()# Click OFFER Tab 
        text_box1 = self.driver.find_element(By.ID, "acf-field_569c2e95a3d27")
        Today.time_taken(JsTextBox, self.driver, "View Vehicle Details", text_box1)#Primary Button Label

        vehicle = f'{self.v.Year} {self.v.MakeName} {self.v.ModelName}'.replace(' ','-')
        x = f'/new-vehicles/#action=im_ajax_call&perform=get_results&search={vehicle}&page=1'
        z = self.driver.find_element(By.ID, "acf-field_569c2aa7a3d24")#Secondary Button Link
        Today.time_taken(JsTextBox, self.driver, x, z)
        Today.time_taken(JsTextBox, self.driver, "View Inventory", driver.find_element(By.ID, "acf-field_569c2bb9a3d26"))#Secondary Link 
    

    def offer_labels(self):
        for i in self.order_list:
            print(i)
            if i[1] == 'True':
                for o in self.v.Offers:
                    if o.OfferTypeID == i[0]:
                        self.driver.find_element(By.LINK_TEXT, "Add Line").click()
        count = 0
        for i in self.order_list:
            print(i)
            if i[1] == 'True':
                for o in self.v.Offers:
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
                            Today.time_taken(JsTextBox, self.driver, o.DueAtSigning, Input)
                            
                        else:
                            Today.time_taken(JsTextBox, self.driver, o.LeaseOffer, Input)

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
                            Today.time_taken(JsTextBox, self.driver, onepay, Input)
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
                            Today.time_taken(JsTextBox, self.driver, special, Input)

                        count += 1
    
    @staticmethod
    def offer_description(v, driver, w, ot):
        media_edit = driver.find_element(By.XPATH, f"/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div[2]/div/div[3]/div[1]/div[{w.RegionID}]/div/div[30]/div[2]/div/div[2]/textarea")
        text = ''
        text += '<center>Located at: ' + ot.DealerName + '</center>\n'
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
        text += f' miles from {ot.DealerName}. Nationwide home delivery is available, please contact dealer for a personalized quote.*'
        text += f'</li></ul>'
        #media_edit.send_keys(text)
        Today.time_taken(VehicleSpecialsNew.fix_text_box, driver, text, media_edit)

    @staticmethod
    def offer_disclaimer(v, driver, w, order_list):
        text_area = driver.find_element(By.ID, "acf-field_5577c0782430f")
        disclaimers = ''
        if v.MakeName == 'Toyota':
            disclaimers += 'ALL OFFERS INCLUDE $100 DOC FEE'
        disclaimers += '\n<ol><strong>'
        disclaimers += str(v.Year) + ' '
        disclaimers += str(v.MakeName) + ' '
        disclaimers += str(v.ModelName) + ' '
        disclaimers += str(v.Trim.replace('""', r'\"'))
        disclaimers += ' Lease and Finance Deals</strong>'
        for i in order_list:
            if i[1] == 'True':
                for o in v.Offers:
                    if o.OfferTypeID == i[0]:
                        disclaimers += '\n\n<li><strong>'
                        disclaimers += str(o.LeaseOffer)
                        disclaimers += str(o.LeaseSpecial)
                        disclaimers += '</strong></li>\n'
                        disclaimers += str(o.Disclaimer)
        disclaimers += '</ol>'
        disclaimers += '*Delivery availability may vary, some exclusions apply. Message dealer for details.'
        Today.time_taken(VehicleSpecialsNew.fix_text_box, driver, disclaimers, text_area)

    def use_offer_tab_original(self):
        while True: # Offer Tab
            try:
                Today.time_taken(self.edit_button_links, self)
                
                self.order_list = [[3, self.w.OfferTypeID3], [2, self.w.OfferTypeID2], [1, self.w.OfferTypeID1], [4, self.w.OfferTypeID4], [6, self.w.OfferTypeID6], [7, self.w.OfferTypeID7]]
                Today.time_taken(OfferContainer.offer_labels, self)
                Today.time_taken(OfferContainer.offer_description, self)                
                Today.time_taken(OfferContainer.offer_disclaimer, self)
                break
            except:
                assert driver.switch_to.alert.text == "Vehicle Stock or VIN not found"
                continue

    def use_offer_tab_onepay(self):
        while True: # Offer Tab
            try:
                Today.time_taken(self.edit_button_links, self)
                
                self.order_list = [[5, self.w.OfferTypeID5]]
                Today.time_taken(OfferContainer.offer_labels, self)
                Today.time_taken(OfferContainer.offer_description, self)                
                Today.time_taken(OfferContainer.offer_disclaimer, self)
                break
            except:
                assert driver.switch_to.alert.text == "Vehicle Stock or VIN not found"
                continue