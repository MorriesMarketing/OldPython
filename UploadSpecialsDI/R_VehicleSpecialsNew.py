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

    def reset_post_page(v,driver, w):
        driver.get(f'{w.Domain}{DIWebsite.DI_EDIT}')
        driver.get(f'{w.Domain}{DIWebsite.DI_POST}')

    def populate_vehicle(v, driver):
        driver.find_element(By.CSS_SELECTOR, ".acf-radio-list > li:nth-child(3)").click() # Click Area Around > Offer Applies To - Stock(one unit)
        driver.find_element(By.ID, "acf-field_56917bb83947f-stock").click()# Click Offer Applies To - Stock(one unit)
        driver.find_element(By.ID, "acf-field_56549cefdeb1a").send_keys(f'{v.StockNumber}')# Send Stock Number to Vehicle Stock Text Box
        driver.find_element(By.ID, "populate_vehicle").click()# Click Populate Stock Number - Image will auto load
    
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

    def ao_tab_step1(driver):
        driver.find_element(By.LINK_TEXT, "Advanced Options").click()
        driver.find_element(By.LINK_TEXT, "Add Discount").click()
        driver.find_element(By.LINK_TEXT, "Add Discount").click()

    def offer_path(driver, region, count, table, vehicle): 
        if vehicle.Brand == 'FCA' and 'https://www.walsercjd.com/' in driver.current_url or 'https://www.walserpolarmazda.com/' in driver.current_url:
            return f'/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div[2]/div/div[3]/div[1]/div[{Region}]/div/div[36]/div[2]/div/table/tbody/tr[{count}]/td[{table}]/div/div'
        return f'/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div[2]/div/div[3]/div[1]/div[{Region}]/div/div[37]/div[2]/div/table/tbody/tr[{count}]/td[{table}]/div/div'

    def ao_tab_step2(v, driver, w):

        offer_input = driver.find_element_by_xpath(VehicleSpecialsNew.offer_path(driver, w.RegionID, 1, 2, v))
        offer_input_css = offer_input.find_element_by_css_selector('input')
        offer_type_input = driver.find_element_by_xpath(self.offer_path(driver, w.RegionID, 1, 3, v))
        offer_type_input_css = offer_type_input.find_element_by_css_selector('input')
        for o in v.Offers:
            if '10% Down Lease Special' in o.LeaseSpecial or 'OEM' in o.LeaseSpecial:
                driver.execute_script(f'arguments[0].value = "{o.LeaseOffer}";', offer_input_css)
                special = f'\<br\>{o.LeaseSpecial}\<br\>{o.DueAtSigning} Due at Signing'
                driver.execute_script(f'arguments[0].value = "{special}";', offer_type_input_css)
                
        offer_input = driver.find_element_by_xpath(self.offer_path(driver, w.RegionID, 2, 2, v))
        offer_input_css = offer_input.find_element_by_css_selector('input')
        driver.execute_script('arguments[0].value = "CLICK HERE FOR MORE OFFERS";', offer_input_css)
        pass

    def use_advanced_options_tab(v, driver, w):
        while True: # Advanced Options Tab
            try:
                Today.time_taken(VehicleSpecialsNew.ao_tab_step1, driver)
                Today.time_taken(VehicleSpecialsNew.ao_tab_step2, v, driver, w)
                value_list = []
                element = driver.find_element_by_xpath('//*[@id="typediv"]/button/span[2]')
                actions = ActionChains(self.driver)
                actions.move_to_element(element).perform()
                print('found element')
                domain = website
                if domain == 'https://www.walserautocampus.com/':
                    print('campus')
                    value_list = [
                    f'{dictionary[f"{vehicle.DealerCode} {vehicle.MakeName}"]["OfferType WAC"]}',
                    'in-type-94', 'in-type-95', 'in-type-58' ]
                    print(value_list)
                    self.offer_type_clicks(value_list)
                    break
                elif domain == 'https://www.walser.com/':
                    print('not campus')
                    value_list = [ 
                        f'in-type-33',
                        f'{dictionary[f"{vehicle.DealerCode} {vehicle.MakeName}"]["OfferType StateCode"]}',
                        f'{dictionary[f"{vehicle.DealerCode} {vehicle.MakeName}"]["OfferType New"]}',
                        f'{dictionary[f"{vehicle.DealerCode} {vehicle.MakeName}"]["OfferType Walser"]}'
                        ]
                    print(value_list)
                    self.offer_type_clicks(value_list)
                    break
                else:
                    if domain == 'https://www.walsernissan.com/':
                        v.DealerCode = 'NIS'
                    if domain == 'https://www.walsernissancoonrapids.com/':
                        v.DealerCode = 'CRN'
                    if domain == 'https://www.walsernissanwayzata.com/':
                        v.DealerCode = 'WZMNNS'
                    if domain == 'https://www.walser-mazda.com/':
                        v.DealerCode = 'MAZ'
                    if domain == 'https://www.walserpolarmazda.com/':
                        v.DealerCode = 'WBMNMA'
                    print(f"{vehicle.DealerCode} {vehicle.MakeName}")
                    value_list = [
                        
                        f'{dictionary[f"{vehicle.DealerCode} {vehicle.MakeName}"]["OfferType Store"]}'
                    ]
                    print(value_list)
                    self.offer_type_clicks(value_list)
                    break
            except:
                assert driver.switch_to.alert.text == "Vehicle Stock or VIN not found"
                continue 

    def use_offer_tab(v, driver):
        while True: # Offer Tab
            try:
                driver.find_element(By.LINK_TEXT, "Offer").click()# Click OFFER Tab 
                driver.find_element(By.ID, "acf-field_569c2e95a3d27").send_keys("View Vehicle Details")# Primary Button Label
                v = f'{vehicle.Year} {vehicle.MakeName} {vehicle.ModelName}'.replace(' ','-')
                x = f'/new-vehicles/#action=im_ajax_call&perform=get_results&search={v}&page=1'
                z = driver.find_element(By.ID, "acf-field_569c2aa7a3d24")#Secondary Button Link
                driver.execute_script(f'arguments[0].value = "{x}";', z)
                driver.find_element(By.ID, "acf-field_569c2bb9a3d26").send_keys("View Inventory")#Secondary Link Label
                
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

    def build_special(v, driver, w):
        Today.time_taken(VehicleSpecialsNew.reset_post_page, v, driver, w)
        Today.time_taken(VehicleSpecialsNew.populate_vehicle, v, driver)
        Today.time_taken(VehicleSpecialsNew.populate_title_boxes, v, driver)
        Today.time_taken(VehicleSpecialsNew.use_advanced_options_tab, v, driver, w)
        Today.time_taken(VehicleSpecialsNew.use_offer_tab, v, driver)
        #Today.time_taken(populate_special)

    def check_match(v,offertypes):
        print('Running Check Match')
        has_match = None
        for ot in offertypes:
            print(f'OFFER TYPE: {ot.Make} {ot.DealerCode}\nVEHICLE: {v.MakeName} {v.DealerCode}\n')
            if f'{ot.Make} {ot.DealerCode}' == f'{v.MakeName} {v.DealerCode}':
                has_match = True
                break
            else:
                has_match = False
                
        return has_match

    def run(vehicles, websites, Website, driver):
        for w in websites:
            if w.WebsiteID >= 1:
            
                w.Driver = driver
                # Login Method
                w.DI_SignIn()
                # Delete All Specials 
                #Today.time_taken(DIWebsite.delete_all_specials,None)

                for v in vehicles:
                    is_match = VehicleSpecialsNew.check_match(v,VehicleSpecialsNew.offertypes)
                    if not is_match:
                        print(f'CHECK BLOCK 1 TRUE: Unable to find matching Make & Dealer Code')
                        
                    elif 'N' not in v.StockNumber:
                        print(f'CHECK BLOCK 2 TRUE: "N" Letter not found in Stock Number: {v.StockNumber}')
                        
                    elif len(v.Offers) == 0:
                        print(f'CHECK BLOCK 3 TRUE: No Offers found')
                        
                    elif w.Domain == 'https://www.walser.com/' or w.Domain == 'https://www.walserautocampus.com/':
                        print(f'CHECK BLOCK 4 TRUE: Running Specials on {w.Domain}')
                        Today.time_taken(VehicleSpecialsNew.build_special, v, driver, w)
                    elif v.Brand != w.Brand:
                        print(f'CHECK BLOCK 5 TRUE: Vehicle Brand: {v.Brand} \nWebsite Brand: {w.Brand}')
                        
                    else:
                        print(f'ELSE STATMENT ACTIVE: Running Specials on {w.Domain}')
                        Today.time_taken(VehicleSpecialsNew.build_special, v, driver)

            else:
                pass
        driver.quit()
    #print('Running Wrong function')               
    #Today.time_taken(run, vehicles, websites, Website, driver)

def main():
    print('Running Right function')   
    Today.time_taken(VehicleSpecialsNew.run, VehicleSpecialsNew.vehicles, VehicleSpecialsNew.websites, VehicleSpecialsNew.Website, VehicleSpecialsNew.driver)

if __name__ == "__main__":
    main()
