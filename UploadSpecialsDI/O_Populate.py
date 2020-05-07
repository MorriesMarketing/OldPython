from O_VehicleSpecial import VehicleSpecial
from O_Days import Today

class Populate(VehicleSpecial):
    
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

    def run():
        Today.time_taken(Populate.populate_special)
