from O_Days import Today
from U_JsTextBox import JsTextBox
from U_VehicleSpecialObject import VehicleSpecialObject

class TabVehicleInfo(VehicleSpecialObject):

    
    def reset_post_page(self):# Navigates to Post then Edit page to reset any cached data.
        self.driver.get(f'{self.website.Domain}{self.website.DI_EDIT}')
        self.driver.get(f'{self.website.Domain}{self.website.DI_POST}')
        

   
    def populate_vehicle(self):#Moves to create vehicle by adding Stock# to textbox then clicking the populate button
        #self.driver.find_element(By.CSS_SELECTOR, ".acf-radio-list > li:nth-child(3)").click() # Click Area Around > Offer Applies To - Stock(one unit)
        self.driver.find_element_by_id("acf-field_56917bb83947f-stock").click()# Click Offer Applies To - Stock(one unit)

        element = self.driver.find_element_by_id("acf-field_56549cefdeb1a")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        Today.time_taken(JsTextBox.fix_text_box, self.driver, self.vehicle.StockNumber, self.driver.find_element_by_id("acf-field_56549cefdeb1a"))# Send Stock Number to Vehicle Stock Text Box
        self.driver.find_element_by_id("populate_vehicle").click()# Click Populate Stock Number - Image will auto load

   
    def populate_title_boxes(self):#Edits the title boxes for both the offer and backend
        while True:
            try: # Check for if vehicle exists
                element = self.driver.find_element_by_name("post_title")# add vehicle title to Title Text Box
                actions = ActionChains(self.driver)
                actions.move_to_element(element).perform()
                Today.time_taken(JsTextBox.fix_text_box, self.driver, f'New {self.vehicle.Year} {self.vehicle.MakeName} {self.vehicle.ModelName} {self.vehicle.Trim}', element)

                self.driver.find_element_by_id("acf-field_5575ca339b200").clear()# clear vehicle title 
                element = self.driver.find_element_by_id("acf-field_5575ca339b200")# replace vehicle title with fixed one
                Today.time_taken(JsTextBox.fix_text_box, self.driver, f'New {self.vehicle.Year} {self.vehicle.MakeName} {self.vehicle.ModelName} {self.vehicle.Trim}', element)
                
                self.driver.find_element_by_css_selector("li:nth-child(2) b").click()# Click Offer Applies To - Inventory
                Today.time_taken(JsTextBox.fix_text_box, self.driver, self.vehicle.StockNumber, self.driver.find_element_by_id("acf-diso_vehicle_stock"))# Send Keys to Secondary Stock Number Box 
                break 
            except Exception as e:
                sleep(.1)
                print(f'Failed to find element. \t{e}')

   
    def error_check(self):
        error_occured = False
        try:
            assert self.driver.switch_to.alert.text == "Vehicle Stock or VIN not found"
            error_occured = True
        except:
            error_occured = False
        print(f'\n\tError: {error_occured}\n')
        return error_occured

    def run():
        success_check = True
        Today.time_taken(TabVehicleInfo.reset_post_page)
        Today.time_taken(TabVehicleInfo.populate_vehicle)
        if self.error_check():
            success_check = False
        Today.time_taken(TabVehicleInfo.populate_title_boxes)
        if self.error_check():
            success_check = False
        return success_check