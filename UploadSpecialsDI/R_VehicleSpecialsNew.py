from I_SqlLight import *
from I_DigitalMarketing import *
from O_TabAdvancedOptions import AdvancedOptions
from O_Days import *
from O_DIOfferTypes import *
from O_DIWebsites import *
from O_Selenium import *
from O_WebOfferTypes import *
from O_TabOffer import OfferContainer
from O_VehicleSpecial import VehicleSpecial

class VehicleSpecialsNew():

    def __init__(self):
        # This is to verify that offers new offers are available
        self.refresh_check = SqlServer.PRD_OfferSpecialsUpload_RefreshCheck()
        self.websites = self.gather_websites()
        self.offertypes = self.gather_offer_types()
        self.vehicles = DigitalMarketing.create_vehicles_from_VehicleSpecialsNew()
        self.driver = SeleniumDrivers.CHROME
        # These are to be used later in the run method. These are to be used as objects
        
    def gather_websites():
        #Pull data for Websites to be ran
        data_table = SqlLight.VM_Websites_ReadData()
        data = Database.convert_table_to_dict(data_table)
        websites = Database.create_objects(data, DIWebsite)
        return websites
    
    def gather_offer_types():
        data_table = SqlLight.VM_OfferTypes_ReadData()
        data = Database.convert_table_to_dict(data_table)
        offertypes = Database.create_objects(data, DIOfferType)
        return offertypes


    @staticmethod
    def edit_button_links(v, driver):
        driver.find_element(By.LINK_TEXT, "Offer").click()# Click OFFER Tab 
        text_box1 = driver.find_element(By.ID, "acf-field_569c2e95a3d27")
        Today.time_taken(VehicleSpecialsNew.fix_text_box, driver, "View Vehicle Details", text_box1)#Primary Button Label
        vehicle = f'{v.Year} {v.MakeName} {v.ModelName}'.replace(' ','-')
        x = f'/new-vehicles/#action=im_ajax_call&perform=get_results&search={vehicle}&page=1'
        z = driver.find_element(By.ID, "acf-field_569c2aa7a3d24")#Secondary Button Link
        Today.time_taken(VehicleSpecialsNew.fix_text_box, driver, x, z)
        Today.time_taken(VehicleSpecialsNew.fix_text_box, driver, "View Inventory", driver.find_element(By.ID, "acf-field_569c2bb9a3d26"))#Secondary Link 
    
    @staticmethod
    def offer_labels(v, driver, w, order_list):
        for i in order_list:
            print(i)
            if i[1] == 'True':
                for o in v.Offers:
                    if o.OfferTypeID == i[0]:
                        driver.find_element(By.LINK_TEXT, "Add Line").click()
        count = 0
        for i in order_list:
            print(i)
            if i[1] == 'True':
                for o in v.Offers:
                    print(f'o.OfferTypeID: {o.OfferTypeID}\ni: {i[0]}')
                    if o.OfferTypeID == i[0]:
                        table = driver.find_elements_by_css_selector('.ui-sortable')[6]
                        row = table.find_elements_by_css_selector('.acf-row')[count]
                        tile = row.find_elements_by_css_selector('.acf-field')[0]
                        child1 = tile.find_element_by_css_selector('.acf-input')
                        child2 = child1.find_element_by_css_selector('.acf-input-wrap')
                        Input = child2.find_element_by_css_selector('input')
                        # OFFER
                        driver.execute_script('arguments[0].value = "' + str(o.LeaseOffer) + '";', Input)

                        table = driver.find_elements_by_css_selector('.ui-sortable')[6]
                        row = table.find_elements_by_css_selector('.acf-row')[count]
                        tile = row.find_elements_by_css_selector('.acf-field')[1]
                        child1 = tile.find_element_by_css_selector('.acf-input')
                        child2 = child1.find_element_by_css_selector('.acf-input-wrap')
                        Input = child2.find_element_by_css_selector('input')
                        # SPECIAL
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
                        Today.time_taken(VehicleSpecialsNew.fix_text_box, driver, special, Input)

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

    @staticmethod
    def use_offer_tab(v, driver, w, ot):
        while True: # Offer Tab
            try:
                Today.time_taken(VehicleSpecialsNew.edit_button_links, v, driver)
                
                order_list = [[3, w.OfferTypeID3], [2, w.OfferTypeID2], [1,w.OfferTypeID1], [4, w.OfferTypeID4], [5, w.OfferTypeID5], [6, w.OfferTypeID6], [7, w.OfferTypeID7]]
                Today.time_taken(VehicleSpecialsNew.offer_labels, v, driver, w, order_list)
                Today.time_taken(VehicleSpecialsNew.offer_description, v, driver, w, ot)                
                Today.time_taken(VehicleSpecialsNew.offer_disclaimer, v, driver, w, order_list)
                break
            except:
                assert driver.switch_to.alert.text == "Vehicle Stock or VIN not found"
                continue

    @staticmethod
    def populate_special(driver):
        while True:
            try:
                element = driver.find_element(By.ID, "title")
                actions = ActionChains(driver)
                actions.move_to_element(element).perform()
                driver.find_element(By.ID, "publish").click()
                break
            except:
                print('Failed')
                sleep(.1)

    

    @staticmethod
    def check_under_10k(v, driver, w, ot):
        for o in v.Offers():
            if o.OfferTypeID == 5 and o.DueAtSigning < 10000:
                Today.time_taken(VehicleSpecialsNew.build_onepay, v, driver, w, ot)

    def run(self):

        for w in self.websites:
            for ot in self.offertypes:
                if w.Domain == ot.Domain:
                    w.OfferType = ot

        for w in self.websites:
            
            w.Driver = self.driver
            self.driver.maximize_window()

            if w.WebsiteID >= 1:
                # Login Method
                w.DI_SignIn()
                # Delete All Specials 
                Today.time_taken(w.delete_all_specials,driver, w)
                   
                for v in self.vehicles:
                    for ot in self.offertypes:
                        if w.Domain == ot.Domain and v.MakeName == ot.Make:
                            w.OfferType = ot

                    vehicle_special = VehicleSpecial(driver=self.driver, website=w, offer_type=ot, vehicle=v)

                    if 'N' in v.StockNumber and len(v.Offers) != 0:
                                                        
                        if w.Domain == 'https://www.walser.com/':
                            print(f'CHECK BLOCK 4 TRUE: Running Specials on {w.Domain} for {v.StockNumber}')
                                   
                            Today.time_taken(vehicle_special.build_special)
                            Today.time_taken(VehicleSpecialsNew.check_under_10k, v, driver, w, ot)
                            
                        elif w.Domain == 'https://www.walserautocampus.com/' and v.State == 'KS':
                            print(f'CHECK BLOCK 4 TRUE: Running Specials on {w.Domain} for {v.StockNumber}')
                            Today.time_taken(VehicleSpecialsNew.build_special, v, driver, w, ot)
                            Today.time_taken(VehicleSpecialsNew.check_under_10k, v, driver, w, ot)

                        elif w.Brand == v.Brand:
                            print(f'ELSE STATMENT ACTIVE: Running Specials on {w.Domain} for {v.StockNumber}')
                            Today.time_taken(VehicleSpecialsNew.build_special, v, driver, w, ot)
                            Today.time_taken(VehicleSpecialsNew.check_under_10k, v, driver, w, ot)
                sleep(5)
                        
            else:
                pass
        driver.quit()

def main():
    vehicle_specials = VehicleSpecialsNew()
    Today.time_taken(vehicle_specials.run)

if __name__ == "__main__":
    main()
