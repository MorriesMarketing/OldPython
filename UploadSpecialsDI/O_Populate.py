from U_VehicleSpecialObject import VehicleSpecialObject
from O_Days import Today

class Populate(VehicleSpecialObject):
    
    def populate_special(self):
        while True:
            try:
                element = self.driver.find_element(By.ID, "title")
                actions = ActionChains(self.driver)
                actions.move_to_element(element).perform()
                self.driver.find_element(By.ID, "publish").click()
                break
            except:
                print('Failed')
                sleep(.1)

    def run(self):
        Today.time_taken(self.populate_special)
