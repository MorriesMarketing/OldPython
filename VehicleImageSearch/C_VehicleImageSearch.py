
from O_Days import *
from O_Selenium import *

class VehicleImageSearch():

    def __init__(self):
        self.driver = Selenium.CHROME
        self.driver.maximize_window()

    def searchDIsite():
        pass
    def searchDealerDotCom():
        vehicles = self.driver.find_elements_by_tag_name('a')

    def get_elements(self,tag_name, attribute):
        sleep(2)
        elements = self.driver.find_elements_by_tag_name(tag_name)
        list_of_found_elements = []
        counter = 2
        for e in elements:
            try:
                element = e.get_attribute(attribute)
                list_of_found_elements.append(element)
            except:
                try:
                    if counter != 0:
                        sleep(1)
                        counter -= 1
                        element = e.get_attribute(attribute)
                        list_of_found_elements.append(element)
                    else:
                        break
                except:
                    print(f'unable to get element {e}')
        return list_of_found_elements

    def search_vehicle_page(self, Dealer, Vehicle):
        for srp in Dealer.SRP:
            if srp == '':
                pass
            else:
                print(srp)
                self.driver.get(f'{Dealer.Domain}')
                self.driver.refresh()
                page = self.driver.get(f'{Dealer.Domain}{srp}{Vehicle.VIN}')

                vehicle_image = None
                list_of_found_elements = VehicleImageSearch.get_elements(self,tag_name='img', attribute='src')
                for image in list_of_found_elements:
                    if Dealer.DealerDotComSite == 1:
                        for url in Dealer.FirstImageSelector:
                            if image != None:
                                if image.startswith(url):
                                    print(f'URL: {url}\n\t {image}')
                                    vehicle_image = image
                                    break
                    if Dealer.DealerInspireSite == 1:
                        if image != None:
                            if Vehicle.VIN in image:
                                vehicle_image = image
                                break

                current_vdp_url = None
                list_of_found_elements = VehicleImageSearch.get_elements(self,tag_name='a', attribute='href')
                            
                for vehicle in list_of_found_elements:
                    if vehicle != None:
                        if Dealer.DealerDotComSite == 1:
                            if f'{Dealer.Domain}used/' in vehicle or f'{Dealer.Domain}new/' in vehicle:
                                current_vdp_url = vehicle
                                break
                        if Dealer.DealerInspireSite == 1:
                            if '/inventory/' in vehicle:
                                current_vdp_url = vehicle
                                break

                if current_vdp_url == None and vehicle_image == None:
                    self.driver.refresh()
                    break
            
        print(f'\nFINAL: \n{current_vdp_url}\n\t{vehicle_image}')
        return [current_vdp_url,vehicle_image]


