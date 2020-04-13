from I_SqlServer import *
from I_Selenium import *
from I_SqlLight import *
from O_Days import *
from O_DIWebsite import *
from O_Vehicles import *

class VehicleSpecialsNew():


     #Pull data for Websites to be ran
    data_table = SqlLight.VM_Websites_ReadData()
    data = Database.convert_table_to_dict(data_table)
    websites = Database.create_objects(data, DiWebsite)
    #Pull data for Vehicle to be ran
    data_table = SqlServer.PRD_ExternalVehicles_AgedUsed_ReadData()
    data = Database.convert_table_to_dict(data_table)
    vehicles = Database.create_objects(data, VehicleAged)
    #Setup Driver & Website to be ran
    driver = SeleniumDrivers.CHROME
    Website = SeleniumDrivers(driver)

    def run(vehicles, websites, Website, driver):
        for w in websites:
            if w.WebsiteID >= 1:
            
                w.Driver = driver
                w.DI_SignIn()
                #Website.navigate_to(w.Domain, f'{w.DI_INVENTORY_PAGE}')
                #Test Piece
                Today.time_taken(Website.navigate_to, w.Domain, f'{w.DI_INVENTORY_PAGE}')
                sleep(.1)
                driver.find_element(By.ID, "im_user_signature").send_keys("Matthew Muhlenkort")
                sleep(.1)
                driver.find_element(By.ID, "im_user_signature").send_keys(Keys.ENTER)
                for v in vehicles:
                
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
