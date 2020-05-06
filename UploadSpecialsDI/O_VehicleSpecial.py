
from O_Days import Today

class VehicleSpecial(Today):
    
    def __init__(self, driver, website, offer_type, vehicle):
        self.vehicle = vehicle
        self.website = website
        self.offer_type = offer_type
        self.driver = driver

    def build_special(self):
        while True:
            self.time_taken(self.reset_post_page, self.vehicle, self.driver, self.website)# Navigates to Post then Edit page to reset any cached data.
            self.time_taken(self.populate_vehicle, v, driver)#Moves to create vehicle by adding Stock# to textbox then clicking the populate button
            if self.error_check():
                break
            self.time_taken(self.populate_title_boxes, v, driver)#Edits the title boxes for both the offer and backend
            if self.error_check():
                break
            ao_run = AdvancedOptions(self.driver, self.website, self.vehicle)
            self.time_taken(ao_run.use_advanced_options_tab)#applies the offer designated to be shown on VRP
            
            ot_run = OfferTypeContainer(v, driver, w, ot)
            self.time_taken(ot_run.select_group_offertypes)# Checks off which DIoffertypes are used for catagorizing for display
            self.time_taken(self.use_offer_tab, v, driver, w, ot)#applies the CTA's, Offers Shown, Media Block, and Disclaimer
            self.time_taken(self.populate_special, driver)# Populate vehicle offers
            #Possible Addition #broadcast_subscribers #Group up offers and broadcast them to specific sites.
            print('Completed Build Specials Loop Successfully')
            break

    def build_onepay(self):
        while True:
            self.time_taken(VehicleSpecialsNew.reset_post_page, v, driver, w)# Navigates to Post then Edit page to reset any cached data.
            self.time_taken(VehicleSpecialsNew.populate_vehicle, v, driver)#Moves to create vehicle by adding Stock# to textbox then clicking the populate button
            if VehicleSpecialsNew.error_check():
                break
            self.time_taken(VehicleSpecialsNew.populate_title_boxes, v, driver)#Edits the title boxes for both the offer and backend
            if VehicleSpecialsNew.error_check():
                break

            ot_run = OfferTypeContainer(v, driver, w, ot)
            self.time_taken(ot_run.select_one_pay_offertypes)# Checks off which DIoffertypes are used for catagorizing for display
            oc_run = OfferContainer( v, driver, w, ot)
            self.time_taken(oc_run.use_offer_tab_onepay)#applies the CTA's, Offers Shown, Media Block, and Disclaimer

            self.time_taken(VehicleSpecialsNew.populate_special, driver)# Populate vehicle offers
            #Possible Addition #broadcast_subscribers #Group up offers and broadcast them to specific sites.
            print('Completed Build OnePay Loop Successfully')
            break


