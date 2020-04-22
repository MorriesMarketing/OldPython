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
        #driver.find_element(By.CSS_SELECTOR, ".acf-radio-list > li:nth-child(3)").click() # Click Area Around > Offer Applies To - Stock(one unit)
        driver.find_element(By.ID, "acf-field_56917bb83947f-stock").click()# Click Offer Applies To - Stock(one unit)
        element = driver.find_element(By.ID, "acf-field_56549cefdeb1a")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        Today.time_taken(VehicleSpecialsNew.fix_text_box, driver, v.StockNumber, driver.find_element(By.ID, "acf-field_56549cefdeb1a"))# Send Stock Number to Vehicle Stock Text Box
        driver.find_element(By.ID, "populate_vehicle").click()# Click Populate Stock Number - Image will auto load
    
    @staticmethod
    def populate_title_boxes(v, driver):
        while True:
            try: # Check for if vehicle exists
                x = driver.find_element(By.NAME, "post_title")# add vehicle title to Title Text Box
                element = x
                actions = ActionChains(driver)
                actions.move_to_element(element).perform()
                Today.time_taken(VehicleSpecialsNew.fix_text_box, driver, f'New {v.Year} {v.MakeName} {v.ModelName} {v.Trim}', x)
                driver.find_element(By.ID, "acf-field_5575ca339b200").clear()# clear vehicle title 
                x = driver.find_element(By.ID, "acf-field_5575ca339b200")# replace vehicle title with fixed one
                Today.time_taken(VehicleSpecialsNew.fix_text_box, driver, f'New {v.Year} {v.MakeName} {v.ModelName} {v.Trim}', x)
                driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) b").click()# Click Offer Applies To - Inventory
                Today.time_taken(VehicleSpecialsNew.fix_text_box, driver, v.StockNumber, driver.find_element(By.ID, "acf-diso_vehicle_stock"))# Send Keys to Secondary Stock Number Box 
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
        
    @staticmethod
    def use_advanced_options_tab(v, driver, w):
        while True: # Advanced Options Tab
            Today.time_taken(VehicleSpecialsNew.ao_tab_step1, driver)
            Today.time_taken(VehicleSpecialsNew.ao_tab_step2, v, driver, w)
            break
    
    @staticmethod
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
      
    @staticmethod
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

    def fix_text_box(driver, text, element_path):
        special_symbols = ['"', '/', '<', '>', ';', ':', '=', '-', '\n', '\t']

        for x in special_symbols:
            text = text.replace(x,f'\{x}')
        print(text)
        driver.execute_script('arguments[0].value = "' + text + '";', element_path)

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
            Today.time_taken(VehicleSpecialsNew.use_offer_tab, v, driver, w, ot)#applies the CTA's, Offers Shown, Media Block, and Disclaimer
            Today.time_taken(VehicleSpecialsNew.populate_special, driver)# Populate vehicle offers
            #Possible Addition #broadcast_subscribers #Group up offers and broadcast them to specific sites.
            print('Completed Build Specials Loop Successfully')
            break

  
    def run(vehicles, websites, Website, driver, offertypes):
        for w in websites:
            w.Driver = driver
            driver.maximize_window()
            if w.WebsiteID >= 1:
                # Login Method
                w.DI_SignIn()
                # Delete All Specials 
                Today.time_taken(DIWebsite.delete_all_specials,driver, w)
                
                for v in vehicles:
                    for ot in offertypes:
                        if w.Domain == 'https://www.walsernissan.com/':
                            v.DealerCode = 'NIS'
                        if w.Domain == 'https://www.walsernissancoonrapids.com/':
                            v.DealerCode = 'CRN'
                        if w.Domain == 'https://www.walsernissanwayzata.com/':
                            v.DealerCode = 'WZMNNS'
                        if w.Domain == 'https://www.walser-mazda.com/':
                            v.DealerCode = 'MAZ'
                        if w.Domain == 'https://www.walserpolarmazda.com/':
                            v.DealerCode = 'WBMNMA'    
                        if f'{ot.Make} {ot.DealerCode}' != f'{v.MakeName} {v.DealerCode}':
                            print(f'CHECK BLOCK 1 TRUE: Make & Dealer Code Did Not Match')
                        
                        elif 'N' not in v.StockNumber:
                            print(f'CHECK BLOCK 2 TRUE: "N" Letter not found in Stock Number: {v.StockNumber}')
                        
                        elif len(v.Offers) == 0:
                            print(f'CHECK BLOCK 3 TRUE: No Offers found')
                        
                        elif w.Domain == 'https://www.walser.com/':
                            print(f'CHECK BLOCK 4 TRUE: Running Specials on {w.Domain} for {v.StockNumber}')
                            Today.time_taken(VehicleSpecialsNew.build_special, v, driver, w, ot)
                        elif w.Domain == 'https://www.walserautocampus.com/' and v.State == 'KS':
                            print(f'CHECK BLOCK 4 TRUE: Running Specials on {w.Domain} for {v.StockNumber}')
                            Today.time_taken(VehicleSpecialsNew.build_special, v, driver, w, ot)

                        elif v.Brand != w.Brand:
                            print(f'CHECK BLOCK 5 TRUE: Vehicle Brand: {v.Brand} \nWebsite Brand: {w.Brand}')
                        
                        else:
                            print(f'ELSE STATMENT ACTIVE: Running Specials on {w.Domain} for {v.StockNumber}')
                            Today.time_taken(VehicleSpecialsNew.build_special, v, driver, w, ot)
                sleep(5)
                        
            else:
                pass
        driver.quit()

def main():
    print('Running Right function')   
    Today.time_taken(VehicleSpecialsNew.run, VehicleSpecialsNew.vehicles, VehicleSpecialsNew.websites, VehicleSpecialsNew.Website, VehicleSpecialsNew.driver, VehicleSpecialsNew.offertypes)

if __name__ == "__main__":
    main()
