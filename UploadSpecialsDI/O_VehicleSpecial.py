from O_Days import Today
from O_TabVehicleInfo import TabVehicleInfo
from O_TabAdvancedOptions import TabAdvancedOptions
from O_TabOffer import TabOfferContainer

class VehicleSpecial():
    
    def __init__(self, driver, website, offer_type, vehicle):
        self.vehicle = vehicle
        self.website = website
        self.offer_type = offer_type
        self.driver = driver

    def build_special(self):
        while True:
            step_one = TabVehicleInfo.run()
            if step_one == False:
                break

            
            Today.time_taken(TabAdvancedOptions.run())#applies the offer designated to be shown on VRP
            
            step_three = OfferTypeContainer(v, driver, w, ot)
            Today.time_taken(step_three.select_group_offertypes)# Checks off which DIoffertypes are used for catagorizing for display
            
            Today.time_taken(self.use_offer_tab, v, driver, w, ot)#applies the CTA's, Offers Shown, Media Block, and Disclaimer
            
            Today.time_taken(self.populate_special, driver)# Populate vehicle offers
            #Possible Addition #broadcast_subscribers #Group up offers and broadcast them to specific sites.
            print('Completed Build Specials Loop Successfully')
            break

    def build_onepay(self):
        while True:
            Today.time_taken(VehicleSpecialsNew.reset_post_page, v, driver, w)# Navigates to Post then Edit page to reset any cached data.
            Today.time_taken(VehicleSpecialsNew.populate_vehicle, v, driver)#Moves to create vehicle by adding Stock# to textbox then clicking the populate button
            if VehicleSpecialsNew.error_check():
                break
            Today.time_taken(VehicleSpecialsNew.populate_title_boxes, v, driver)#Edits the title boxes for both the offer and backend
            if VehicleSpecialsNew.error_check():
                break

            ot_run = OfferTypeContainer(v, driver, w, ot)
            Today.time_taken(ot_run.select_one_pay_offertypes)# Checks off which DIoffertypes are used for catagorizing for display
            oc_run = OfferContainer( v, driver, w, ot)
            Today.time_taken(oc_run.use_offer_tab_onepay)#applies the CTA's, Offers Shown, Media Block, and Disclaimer

            Today.time_taken(VehicleSpecialsNew.populate_special, driver)# Populate vehicle offers
            #Possible Addition #broadcast_subscribers #Group up offers and broadcast them to specific sites.
            print('Completed Build OnePay Loop Successfully')
            break


