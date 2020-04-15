from I_Databases import *
from I_SqlLight import *
from I_SqlServer import *
from O_Days import *
from O_DIOfferTypes import *
from O_DIWebsites import *
from O_Offers import *
from O_Selenium import *
from O_Vehicles import *

class VehicleSpecialsNew():

    SqlServer.PRD_OfferSpecialsUpload_RefreshCheck()
     #Pull data for Websites to be ran
    data_table = SqlLight.VM_Websites_ReadData()
    data = Database.convert_table_to_dict(data_table)
    websites = Database.create_objects(data, DIWebsite)

    data_table = SqlLight.VM_OfferTypes_ReadData()
    data = Database.convert_table_to_dict(data_table)
    offertypes = Database.create_objects(data, DIOfferType)

    #Pull data for Vehicle to be ran
    data_table = SqlServer.PRD_OfferSpecialsUpload_ReadData()
    data = Database.convert_table_to_dict(data_table)
    vehicles = Database.create_objects(data, Vehicle)

    #Setup Driver & Website to be ran
    driver = SeleniumDrivers.CHROME
    Website = SeleniumDrivers(driver)

    def reset_post_page(v,driver):
        driver.get(f'{self.Domain}{DIWebsite.DI_EDIT}')
        driver.get(f'{self.Domain}{DIWebsite.DI_POST}')

    def populate_vehicle(v, driver):
        driver.find_element(By.CSS_SELECTOR, ".acf-radio-list > li:nth-child(3)").click() # Click Area Around > Offer Applies To - Stock(one unit)
        driver.find_element(By.ID, "acf-field_56917bb83947f-stock").click()# Click Offer Applies To - Stock(one unit)
        driver.find_element(By.ID, "acf-field_56549cefdeb1a").send_keys(f'{v.StockNumber}')# Send Stock Number to Vehicle Stock Text Box
        driver.find_element(By.ID, "populate_vehicle").click()# Click Populate Stock Number - Image will auto load
    
    def populate_title_boxes(v, driver):
        while True:
            driver.find_element(By.CSS_SELECTOR, ".acf-radio-list > li:nth-child(3)").click() # Click Area Around > Offer Applies To - Stock(one unit)
            driver.find_element(By.ID, "acf-field_56917bb83947f-stock").click()# Click Offer Applies To - Stock(one unit)
            driver.find_element(By.ID, "acf-field_56549cefdeb1a").send_keys(f'{vehicle.StockNumber}')# Send Stock Number to Vehicle Stock Text Box
            driver.find_element(By.ID, "populate_vehicle").click()# Click Populate Stock Number - Image will auto load
            try: # Check for if vehicle exists
                x = driver.find_element(By.NAME, "post_title")# add vehicle title to Title Text Box
                element = x
                actions = ActionChains(driver)
                actions.move_to_element(element).perform()
                driver.execute_script(f'arguments[0].value = "New {vehicle.Year} {vehicle.MakeName} {vehicle.ModelName} {vehicle.Trim}";', x)
                driver.find_element(By.ID, "acf-field_5575ca339b200").clear()# clear vehicle title 
                x = self.driver.find_element(By.ID, "acf-field_5575ca339b200")# replace vehicle title with fixed one
                driver.execute_script(f'arguments[0].value = "New {vehicle.Year} {vehicle.MakeName} {vehicle.ModelName} {vehicle.Trim}";', x)
                driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) b").click()# Click Offer Applies To - Inventory
                driver.find_element(By.ID, "acf-diso_vehicle_stock").send_keys(f'{vehicle.StockNumber}')# Send Keys to Secondary Stock Number Box 
                break 
            except:
                try:
                    driver.switch_to_alert().accept()
                    continue
                except:
                    assert driver.switch_to.alert.text == "Vehicle Stock or VIN not found"
                continue

    def use_advanced_options_tab(v, driver):
        while True: # Advanced Options Tab
            try:
                driver.find_element(By.LINK_TEXT, "Advanced Options").click()
                driver.find_element(By.LINK_TEXT, "Add Discount").click()
                driver.find_element(By.LINK_TEXT, "Add Discount").click()
                offer_input = driver.find_element_by_xpath(self.offer_path(Region, 1, 2, vehicle))
                offer_input_css = offer_input.find_element_by_css_selector('input')
                offer_type_input = driver.find_element_by_xpath(self.offer_path(Region, 1, 3, vehicle))
                offer_type_input_css = offer_type_input.find_element_by_css_selector('input')
                for advanced_options in vehicle.Offers:
                    if '10% Down Lease Special' in advanced_options.LeaseSpecial or 'OEM' in advanced_options.LeaseSpecial:
                        driver.execute_script(f'arguments[0].value = "{advanced_options.LeaseOffer}";', offer_input_css)
                        special = f'\<br\>{advanced_options.LeaseSpecial}\<br\>{advanced_options.DueAtSigning} Due at Signing'
                        driver.execute_script(f'arguments[0].value = "{special}";', offer_type_input_css)
                
                offer_input = driver.find_element_by_xpath(self.offer_path(Region, 2, 2, vehicle))
                offer_input_css = offer_input.find_element_by_css_selector('input')
                driver.execute_script('arguments[0].value = "CLICK HERE FOR MORE OFFERS";', offer_input_css)
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

    def build_special(v, driver):
        Today.time_taken(reset_post_page, v, driver)
        Today.time_taken(populate_vehicle, v, driver)
        Today.time_taken(populate_title_boxes, v, driver)
        Today.time_taken(use_advanced_options_tab, v, driver)
        Today.time_taken(use_offer_tab, v, driver)
        #Today.time_taken(populate_special)

    def check_match(v,offertypes):
        print('Running Check Match')
        value = None
        for ot in offertypes:
            print(f'\nOFFER TYPE: {ot.Make} {ot.DealerCode} \nVEHICLE: {v.MakeName} {v.DealerCode}\n')
            sleep(1)
            if f'{ot.Make} {ot.DealerCode}' == f'{v.MakeName} {v.DealerCode}':
                value = True
            else:
                value = False
        return value

    def run(vehicles, websites, Website, driver):
        for w in websites:
            if w.WebsiteID >= 1:
            
                w.Driver = driver
                # Login Method
                w.DI_SignIn()
                # Delete All Specials 
                #Today.time_taken(DIWebsite.delete_all_specials,None)

                for v in vehicles:
                    value = VehicleSpecialsNew.check_match(v,VehicleSpecialsNew.offertypes)
                    if value == False:
                        print(f'CHECK BLOCK 1 TRUE: Unable to find matching Make & Dealer Code')
                        continue
                    elif 'N' not in v.StockNumber:
                        print(f'CHECK BLOCK 2 TRUE: "N" Letter not found in Stock Number: {v.StockNumber}')
                        continue
                    elif len(v.Offers) == 0:
                        print(f'CHECK BLOCK 3 TRUE: No Offers found')
                        continue
                    elif w.Domain == 'https://www.walser.com/' or w.Domain == 'https://www.walserautocampus.com/':
                        print(f'CHECK BLOCK 4 TRUE: Running Specials on {w.Domain}')
                        Today.time_taken(build_special, v, driver)
                    elif v.Brand != w.Brand:
                        print(f'CHECK BLOCK 5 TRUE: Vehicle Brand: {v.Brand} \nWebsite Brand: {w.Brand}')
                        continue
                    else:
                        print(f'ELSE STATMENT ACTIVE: Running Specials on {w.Domain}')
                        Today.time_taken(build_special, v, driver)

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
