from U_VehicleSpecialObject import VehicleSpecialObject
from O_Days import Today
from O_Selenium import SeleniumDrivers
from time import sleep


class Populate(VehicleSpecialObject):
    
    def populate_special(self):
        while True:
            try:
                sleep(1)
                element = self.driver.find_element_by_id("title")
                SeleniumDrivers.move_to_element(driver=self.driver,element=element)
                self.driver.find_element_by_id("publish").click()
                break
            except:
                print('Failed')
                sleep(.1)

    def run(self):
        Today.time_taken(self.populate_special)
