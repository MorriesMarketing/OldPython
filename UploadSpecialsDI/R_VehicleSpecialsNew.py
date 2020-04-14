from I_SqlServer import *
from I_Selenium import *
from I_SqlLight import *
from O_Days import *
from O_DIOfferTypes import *
from O_DIWebsites import *
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

    def build_special():
        pass

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

                    if check_match(v) == False:
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
                        build_special()
                    elif v.Brand != w.Brand:
                        print(f'CHECK BLOCK 5 TRUE: Vehicle Brand: {v.Brand} \nWebsite Brand: {w.Brand}')
                        continue
                    else:
                        print(f'ELSE STATMENT ACTIVE: Running Specials on {w.Domain}')
                        build_special()

                    Website.navigate_to(w.Domain,f'{w.DI_INVENTORY_VIN}{v.VIN}')
                    try:
                        driver.find_element_by_xpath('//*[@id="edit-vehicle-form"]/div[4]/div/div[2]/div[2]/a')
                        try:
                            driver.find_element(By.LINK_TEXT, "Mark as Internet Special").click()
                        except:
                            print('Already Marked Special')
                            driver.find_element(By.CSS_SELECTOR, ".toggle-internet-special > strong")
                    except:
                        print("Couldn't Find Element")
                        sleep(1)
            else:
                pass
        driver.quit()
                    
    Today.time_taken(run, vehicles, websites, Website, driver)

def main():
    VehicleSpecialsUsed.run()

if __name__ == "__main__":
    main()
