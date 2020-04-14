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

    def refresh_post_page(v,driver):
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

    def build_special(v, driver):
        refresh_post_page(v,driver)
        populate_vehicle(v, driver)
        populate_title_boxes(v, driver)


    def check_match(v):
        value = None
        for ot in offertypes:
            print(f'OFFER TYPE: {ot.Make} {ot.DealerCode} \nVEHICLE: {v.MakeName} {v.DealerCode}')
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
                Today.time_taken(DIWebsite.delete_all_specials,None)

                for v in vehicles:
                    value = check_match(v)
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
                        build_special(v, driver)
                    elif v.Brand != w.Brand:
                        print(f'CHECK BLOCK 5 TRUE: Vehicle Brand: {v.Brand} \nWebsite Brand: {w.Brand}')
                        continue
                    else:
                        print(f'ELSE STATMENT ACTIVE: Running Specials on {w.Domain}')
                        build_special(v, driver)

            else:
                pass
        driver.quit()
                    
    Today.time_taken(run, vehicles, websites, Website, driver)

def main():
    VehicleSpecialsUsed.run()

if __name__ == "__main__":
    main()
