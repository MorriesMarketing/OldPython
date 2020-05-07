from I_SqlLight import *
from I_DigitalMarketing import *
from O_TabAdvancedOptions import TabAdvancedOptions
from O_Days import *
from O_DIOfferTypes import *
from O_DIWebsites import *
from O_Selenium import *
from O_WebOfferTypes import *
from O_TabOffer import TabOfferContainer
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

    def run(self):
        self.driver.maximize_window()
        for w in self.websites:
            w.Driver = self.driver
            
            if w.WebsiteID >= 1:
                # Login Method
                w.DI_SignIn()
                # Delete All Specials 
                Today.time_taken(w.delete_all_specials)
                   
                for v in self.vehicles:
                    for ot in self.offertypes:
                        if w.Domain == ot.Domain and v.MakeName == ot.Make:
                            w.OfferType = ot

                    vehicle_special = VehicleSpecial(driver=self.driver, website=w, vehicle=v)

                    if 'N' in v.StockNumber and len(v.Offers) != 0:
                                                        
                        if w.Domain == 'https://www.walser.com/':
                            print(f'CHECK BLOCK 4 TRUE: Running Specials on {w.Domain} for {v.StockNumber}')
                            Today.time_taken(vehicle_special.run)
                            
                        elif w.Domain == 'https://www.walserautocampus.com/' and v.State == 'KS':
                            print(f'CHECK BLOCK 4 TRUE: Running Specials on {w.Domain} for {v.StockNumber}')
                            Today.time_taken(vehicle_special.run)

                        elif w.Brand == v.Brand:
                            print(f'ELSE STATMENT ACTIVE: Running Specials on {w.Domain} for {v.StockNumber}')
                            Today.time_taken(vehicle_special.run)
                    
                sleep(5)
                DIWebsite.reload_cache()
                        
            else:
                pass
        driver.quit()

def main():
    vehicle_specials = VehicleSpecialsNew()
    Today.time_taken(vehicle_specials.run)

if __name__ == "__main__":
    main()