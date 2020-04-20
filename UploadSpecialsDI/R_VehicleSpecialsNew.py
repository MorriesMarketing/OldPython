from I_SqlLight import *
from I_DigitalMarketing import *
from O_Days import *
from O_DIOfferTypes import *
from O_DIWebsites import *
from O_Selenium import *

class VehicleSpecialsNew():

    SqlServer.PRD_OfferSpecialsUpload_RefreshCheck()
     #Pull data for Websites to be ran
    data_table = SqlLight.VM_Websites_ReadData()
    data = Database.convert_table_to_dict(data_table)
    websites = Database.create_objects(data, DIWebsite)

    data_table = SqlLight.VM_OfferTypes_ReadData()
    data = Database.convert_table_to_dict(data_table)
    offertypes = Database.create_objects(data, DIOfferType)

    
    vehicles = DigitalMarketing.create_vehicles_from_VehicleSpecialsNew()

    #Setup Driver & Website to be ran
    driver = SeleniumDrivers.CHROME
    Website = SeleniumDrivers(driver)

    @staticmethod
    def reset_post_page(v,driver, w):
        driver.get(f'{w.Domain}{DIWebsite.DI_EDIT}')
        driver.get(f'{w.Domain}{DIWebsite.DI_POST}')

    @staticmethod
    def populate_vehicle(v, driver):
        driver.find_element(By.CSS_SELECTOR, ".acf-radio-list > li:nth-child(3)").click() # Click Area Around > Offer Applies To - Stock(one unit)
        driver.find_element(By.ID, "acf-field_56917bb83947f-stock").click()# Click Offer Applies To - Stock(one unit)
        driver.find_element(By.ID, "acf-field_56549cefdeb1a").send_keys(f'{v.StockNumber}')# Send Stock Number to Vehicle Stock Text Box
        driver.find_element(By.ID, "populate_vehicle").click()# Click Populate Stock Number - Image will auto load
    
    @staticmethod
    def populate_title_boxes(v, driver):
        while True:
            try: # Check for if vehicle exists
                x = driver.find_element(By.NAME, "post_title")# add vehicle title to Title Text Box
                element = x
                actions = ActionChains(driver)
                actions.move_to_element(element).perform()
                driver.execute_script(f'arguments[0].value = "New {v.Year} {v.MakeName} {v.ModelName} {v.Trim}";', x)
                driver.find_element(By.ID, "acf-field_5575ca339b200").clear()# clear vehicle title 
                x = driver.find_element(By.ID, "acf-field_5575ca339b200")# replace vehicle title with fixed one
                driver.execute_script(f'arguments[0].value = "New {v.Year} {v.MakeName} {v.ModelName} {v.Trim}";', x)
                driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) b").click()# Click Offer Applies To - Inventory
                driver.find_element(By.ID, "acf-diso_vehicle_stock").send_keys(f'{v.StockNumber}')# Send Keys to Secondary Stock Number Box 
                break 
            except Exception as e:
                sleep(.1)
                print(f'Failed to find element. \t{e}')

    @staticmethod
    def ao_tab_step1(driver):
        driver.find_element(By.LINK_TEXT, "Advanced Options").click()
        driver.find_element(By.LINK_TEXT, "Add Discount").click()
        driver.find_element(By.LINK_TEXT, "Add Discount").click()

    @staticmethod
    def ao_tab_step2_offer_path(driver, Region, count, table, vehicle): 
        if vehicle.Brand == 'FCA' and 'https://www.walsercjd.com/' in driver.current_url or 'https://www.walserpolarmazda.com/' in driver.current_url:
            return f'/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div[2]/div/div[3]/div[1]/div[{Region}]/div/div[36]/div[2]/div/table/tbody/tr[{count}]/td[{table}]/div/div'
        return f'/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div[2]/div/div[3]/div[1]/div[{Region}]/div/div[37]/div[2]/div/table/tbody/tr[{count}]/td[{table}]/div/div'

    @staticmethod
    def ao_tab_step2(v, driver, w):

        offer_input = driver.find_element_by_xpath(VehicleSpecialsNew.ao_tab_step2_offer_path(driver, w.RegionID, 1, 2, v))
        offer_input_css = offer_input.find_element_by_css_selector('input')
        offer_type_input = driver.find_element_by_xpath(VehicleSpecialsNew.ao_tab_step2_offer_path(driver, w.RegionID, 1, 3, v))
        offer_type_input_css = offer_type_input.find_element_by_css_selector('input')
        for o in v.Offers:
            if '10% Down Lease Special' in o.LeaseSpecial or 'OEM' in o.LeaseSpecial:
                driver.execute_script(f'arguments[0].value = "{o.LeaseOffer}";', offer_input_css)
                special = f'\<br\>{o.LeaseSpecial}\<br\>{o.DueAtSigning} Due at Signing'
                driver.execute_script(f'arguments[0].value = "{special}";', offer_type_input_css)
                
        offer_input = driver.find_element_by_xpath(VehicleSpecialsNew.ao_tab_step2_offer_path(driver, w.RegionID, 2, 2, v))
        offer_input_css = offer_input.find_element_by_css_selector('input')
        driver.execute_script('arguments[0].value = "CLICK HERE FOR MORE OFFERS";', offer_input_css)
        

    def use_advanced_options_tab(v, driver, w):
        while True: # Advanced Options Tab
            Today.time_taken(VehicleSpecialsNew.ao_tab_step1, driver)
            Today.time_taken(VehicleSpecialsNew.ao_tab_step2, v, driver, w)
            break
    
    def offer_type_clicks(driver, value_list):
        while True:
            try:
                for i in value_list:
                    print(i)
                    driver.find_element_by_id(i).click()
                    sleep(.1)
                break
            except:
                sleep(.1)   
                
    def select_offertypes(v, driver, w, ot):
        value_list = []
        element = driver.find_element_by_xpath('//*[@id="typediv"]/button/span[2]')
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        print('found element')
        domain = w.Domain
        if w.WebsiteID == 0:
            value_list = [ot.OnePay]
        elif domain == 'https://www.walserautocampus.com/':
            print('campus')
            value_list = [ot.WAC_Brand, ot.WAC_Fixed, ot.WAC3_Fixed, ot.WAC4_Fixed]
        elif domain == 'https://www.walser.com/':
            print('not campus')
            value_list = [ot.WAG_Fixed, ot.WAG_StateCode, ot.WAG_New, ot.WAG_Walser]
        else:
            value_list = [ot.StoreType]
        print(f'List: {value_list}')
        VehicleSpecialsNew.offer_type_clicks(driver, value_list)

    def edit_button_links(v, driver):
        driver.find_element(By.LINK_TEXT, "Offer").click()# Click OFFER Tab 
        driver.find_element(By.ID, "acf-field_569c2e95a3d27").send_keys("View Vehicle Details")#Primary Button Label
        vehicle = f'{v.Year} {v.MakeName} {v.ModelName}'.replace(' ','-')
        x = f'/new-vehicles/#action=im_ajax_call&perform=get_results&search={vehicle}&page=1'
        z = driver.find_element(By.ID, "acf-field_569c2aa7a3d24")#Secondary Button Link
        driver.execute_script(f'arguments[0].value = "{x}";', z)
        driver.find_element(By.ID, "acf-field_569c2bb9a3d26").send_keys("View Inventory")#Secondary Link Label

    def offer_labels():
        count = 0
        
        for offer in vehicle.Offers:
            if 'One Pay' in offer.LeaseSpecial and 'landrover' in website or 'One Pay' in offer.LeaseSpecial and 'mercedes' in website:
                pass
            else:
                self.driver.find_element(By.LINK_TEXT, "Add Line").click()
                table = self.driver.find_elements_by_css_selector('.ui-sortable')[6]
                row = table.find_elements_by_css_selector('.acf-row')[count]
                tile = row.find_elements_by_css_selector('.acf-field')[0]
                child1 = tile.find_element_by_css_selector('.acf-input')
                child2 = child1.find_element_by_css_selector('.acf-input-wrap')
                Input = child2.find_element_by_css_selector('input')
                # OFFER
                self.driver.execute_script('arguments[0].value = "' + str(offer.LeaseOffer) + '";', Input)

                table = self.driver.find_elements_by_css_selector('.ui-sortable')[6]
                row = table.find_elements_by_css_selector('.acf-row')[count]
                tile = row.find_elements_by_css_selector('.acf-field')[1]
                child1 = tile.find_element_by_css_selector('.acf-input')
                child2 = child1.find_element_by_css_selector('.acf-input-wrap')
                Input = child2.find_element_by_css_selector('input')
                # SPECIAL
                special = ''
                special += '\<br\>'
                special += str(offer.LeaseSpecial)
                # if vehicle.MakeName == 'Nissan' and 'Lease Special' in advanced_options.LeaseSpecial:
                if 'APR Finance Special' in offer.LeaseSpecial:
                    special += ''
                else:
                    special += '\<br\>'
                    special += str(offer.DueAtSigning)
                    special += ' Due at Signing'
                self.driver.execute_script('arguments[0].value = "' + special + '";', Input)
                count += 1

    def use_offer_tab(v, driver):
        while True: # Offer Tab
            try:

                VehicleSpecialsNew.edit_button_links(v, driver)
                
                self.offer_labels(vehicle)
                
                self.offer_description(vehicle, Region)
                #self.driver.find_element(By.ID, "acf-field_5577c0782430f").send_keys("Offer Disclaimer")
                
                self.offer_disclaimer(vehicle)
                break
            except:
                assert driver.switch_to.alert.text == "Vehicle Stock or VIN not found"
                continue

    def populate_special():
        while True:
            try:
                element = driver.find_element(By.ID, "title")
                actions = ActionChains(self.driver)
                actions.move_to_element(element).perform()
                driver.find_element(By.ID, "publish").click()
                break
            except:
                print('Failed')
                sleep(.1)

    def error_check():
        error_occured = False
        try:
            assert driver.switch_to.alert.text == "Vehicle Stock or VIN not found"
            error_occured = True
        except:
            error_occured = False
        print(f'\n\tError: {error_occured}\n')
        return error_occured

    def build_special(v, driver, w, ot):
        while True:
            Today.time_taken(VehicleSpecialsNew.reset_post_page, v, driver, w)# Navigates to Post then Edit page to reset any cached data.
            Today.time_taken(VehicleSpecialsNew.populate_vehicle, v, driver)#Moves to create vehicle by adding Stock# to textbox then clicking the populate button
            if VehicleSpecialsNew.error_check():
                break
            Today.time_taken(VehicleSpecialsNew.populate_title_boxes, v, driver)#Edits the title boxes for both the offer and backend
            if VehicleSpecialsNew.error_check():
                break
            Today.time_taken(VehicleSpecialsNew.use_advanced_options_tab, v, driver, w)#applies the offer designated to be shown on VRP
            Today.time_taken(VehicleSpecialsNew.select_offertypes, v, driver, w, ot)# Checks off which DIoffertypes are used for catagorizing for display
            Today.time_taken(VehicleSpecialsNew.use_offer_tab, v, driver)#applies the CTA's, Offers Shown, Media Block, and Disclaimer
            #Today.time_taken(populate_special)# Populate vehicle offers
            #Possible Addition #broadcast_subscribers #Group up offers and broadcast them to specific sites.
            print('Completed Build Specials Loop Successfully')

  
    def run(vehicles, websites, Website, driver, offertypes):
        for w in websites:
            if w.WebsiteID >= 1:
            
                w.Driver = driver
                # Login Method
                w.DI_SignIn()
                # Delete All Specials 
                #Today.time_taken(DIWebsite.delete_all_specials,None)

                for v in vehicles:
                    for ot in offertypes:
                        print(f'OFFER TYPE: {ot.Make} {ot.DealerCode}\nVEHICLE: {v.MakeName} {v.DealerCode}\n')
                        if f'{ot.Make} {ot.DealerCode}' != f'{v.MakeName} {v.DealerCode}':
                            print(f'CHECK BLOCK 1 TRUE: Make & Dealer Code Did Not Match')
                        
                        elif 'N' not in v.StockNumber:
                            print(f'CHECK BLOCK 2 TRUE: "N" Letter not found in Stock Number: {v.StockNumber}')
                        
                        elif len(v.Offers) == 0:
                            print(f'CHECK BLOCK 3 TRUE: No Offers found')
                        
                        elif w.Domain == 'https://www.walser.com/' or w.Domain == 'https://www.walserautocampus.com/':
                            print(f'CHECK BLOCK 4 TRUE: Running Specials on {w.Domain} for {v.StockNumber}')
                            Today.time_taken(VehicleSpecialsNew.build_special, v, driver, w, ot)

                        elif v.Brand != w.Brand:
                            print(f'CHECK BLOCK 5 TRUE: Vehicle Brand: {v.Brand} \nWebsite Brand: {w.Brand}')
                        
                        else:
                            if w.Domain == 'https://www.walsernissan.com/':
                                ot.DealerCode = 'NIS'
                            if w.Domain == 'https://www.walsernissancoonrapids.com/':
                                ot.DealerCode = 'CRN'
                            if w.Domain == 'https://www.walsernissanwayzata.com/':
                                ot.DealerCode = 'WZMNNS'
                            if w.Domain == 'https://www.walser-mazda.com/':
                                ot.DealerCode = 'MAZ'
                            if w.Domain == 'https://www.walserpolarmazda.com/':
                                ot.DealerCode = 'WBMNMA'
                            print(f'ELSE STATMENT ACTIVE: Running Specials on {w.Domain} for {v.StockNumber}')
                            Today.time_taken(VehicleSpecialsNew.build_special, v, driver, ot)
                        
            else:
                pass
        driver.quit()
    #print('Running Wrong function')               
    #Today.time_taken(run, vehicles, websites, Website, driver)

def main():
    print('Running Right function')   
    Today.time_taken(VehicleSpecialsNew.run, VehicleSpecialsNew.vehicles, VehicleSpecialsNew.websites, VehicleSpecialsNew.Website, VehicleSpecialsNew.driver, VehicleSpecialsNew.offertypes)

if __name__ == "__main__":
    main()
