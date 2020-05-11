from O_Days import Today
from O_TabVehicleInfo import TabVehicleInfo
from O_TabAdvancedOptions import TabAdvancedOptions
from O_TabOffer import TabOfferContainer
from O_WebOfferTypes import OfferTypeContainer
from O_Populate import Populate
from U_VehicleSpecialObject import VehicleSpecialObject

class VehicleSpecial(VehicleSpecialObject):
    
    def build_special(self):
        while True:
            step_one = TabVehicleInfo(self.driver,self.website,self.vehicle)
            step_two = TabVehicleInfo.run()
            if step_two == False:
                break

            step_three = TabAdvancedOptions(self.driver,self.website,self.vehicle)
            step_three.run()#applies the offer designated to be shown on VRP
            
            step_four = OfferTypeContainer(self.driver,self.website,self.vehicle)
            step_four.run(input=OfferTypeContainer.GROUP)# Checks off which DIoffertypes are used for catagorizing for display
             
            step_five = TabOfferContainer(self.driver,self.website,self.vehicle)
            step_five.run(input=TabOfferContainer.GROUP)#applies the CTA's, Offers Shown, Media Block, and Disclaimer
            
            step_six = Populate(self.driver,self.website,self.vehicle)
            step_six.run()# Populate vehicle offers
            #Possible Addition #broadcast_subscribers #Group up offers and broadcast them to specific sites.
            print('Completed Build Specials Loop Successfully')
            break

    def check_under_10k(self):
        for o in self.vehicle.Offers():
            if o.OfferTypeID == 5 and o.DueAtSigning < 10000:
                Today.time_taken(self.build_onepay)

    def build_onepay(self):
        while True:
            step_one = TabVehicleInfo(self.driver,self.website,self.vehicle)
            step_two = TabVehicleInfo.run()
            if step_two == False:
                break

            step_four = OfferTypeContainer(self.driver,self.website,self.vehicle)
            step_four.run(input=OfferTypeContainer.ONEPAY)# Checks off which DIoffertypes are used for catagorizing for display
             
            step_five = TabOfferContainer(self.driver,self.website,self.vehicle)
            step_five.run(input=TabOfferContainer.ONEPAY)#applies the CTA's, Offers Shown, Media Block, and Disclaimer
            
            step_six = Populate(self.driver,self.website,self.vehicle)
            step_six.run()# Populate vehicle offers
            #Possible Addition #broadcast_subscribers #Group up offers and broadcast them to specific sites.
            print('Completed Build OnePay Loop Successfully')
            break

    def run(self):
        Today.time_taken(self.build_special)
        Today.time_taken(self.check_under_10k)

