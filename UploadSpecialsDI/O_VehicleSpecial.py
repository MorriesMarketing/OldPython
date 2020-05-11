from O_Days import Today
from O_TabVehicleInfo import TabVehicleInfo
from O_TabAdvancedOptions import TabAdvancedOptions
from O_TabOffer import TabOfferContainer
from O_WebOfferTypes import OfferTypeContainer
from O_Populate import Populate

class VehicleSpecial():
    
    def __init__(self, driver, website, vehicle):
        self.vehicle = vehicle
        self.website = website
        self.driver = driver

    def build_special(self):
        while True:
            step_one = TabVehicleInfo.run()
            if step_one == False:
                break

            TabAdvancedOptions.run()#applies the offer designated to be shown on VRP
            
            OfferTypeContainer.run(input=OfferTypeContainer.GROUP)# Checks off which DIoffertypes are used for catagorizing for display
             
            TabOfferContainer.run(input=TabOfferContainer.GROUP)#applies the CTA's, Offers Shown, Media Block, and Disclaimer
            
            Populate.run()# Populate vehicle offers
            #Possible Addition #broadcast_subscribers #Group up offers and broadcast them to specific sites.
            print('Completed Build Specials Loop Successfully')
            break

    def check_under_10k(self):
        for o in self.vehicle.Offers():
            if o.OfferTypeID == 5 and o.DueAtSigning < 10000:
                Today.time_taken(self.build_onepay)

    def build_onepay(self):
        while True:
            step_one = TabVehicleInfo.run()
            if step_one == False:
                break

            OfferTypeContainer.run(input=OfferTypeContainer.ONEPAY)# Checks off which DIoffertypes are used for catagorizing for display
             
            TabOfferContainer.run(input=OfferTypeContainer.ONEPAY)#applies the CTA's, Offers Shown, Media Block, and Disclaimer
            
            Populate.run()# Populate vehicle offers
            #Possible Addition #broadcast_subscribers #Group up offers and broadcast them to specific sites.
            print('Completed Build OnePay Loop Successfully')
            break

    def run(self):
        Today.time_taken(self.build_special)
        Today.time_taken(self.check_under_10k)

