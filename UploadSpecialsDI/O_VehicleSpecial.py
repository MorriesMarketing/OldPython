from O_Days import Today
from O_TabVehicleInfo import TabVehicleInfo
from O_TabAdvancedOptions import TabAdvancedOptions
from O_TabOffer import TabOfferContainer
from O_WebOfferTypes import OfferTypeContainer
from O_Populate import Populate
from U_VehicleSpecialObject import VehicleSpecialObject

class VehicleSpecial(VehicleSpecialObject):
    
    def build_special(self):
        success_check = None
        while True:
            step_one = TabVehicleInfo(self.driver,self.website,self.vehicle)
            check_step_one = step_one.run()
            if check_step_one == False:
                success_check = False
                break

            step_two = TabAdvancedOptions(self.driver,self.website,self.vehicle)
            check_step_two = step_two.run()#applies the offer designated to be shown on VRP
            if check_step_two == False:
                success_check = False
                break
            
            step_three = OfferTypeContainer(self.driver,self.website,self.vehicle)
            check_step_three = step_three.run(input=OfferTypeContainer.GROUP)# Checks off which DIoffertypes are used for catagorizing for display
            if check_step_three == False:
                success_check = False
                break
             
            step_four = TabOfferContainer(self.driver,self.website,self.vehicle)
            check_step_four = step_four.run(input=TabOfferContainer.GROUP)#applies the CTA's, Offers Shown, Media Block, and Disclaimer
            if check_step_four == False:
                success_check = False
                break
            
            step_six = Populate(self.driver,self.website,self.vehicle)
            step_six.run()# Populate vehicle offers
            #Possible Addition #broadcast_subscribers #Group up offers and broadcast them to specific sites.
            print('Completed Build Specials Loop Successfully')
            success_check = True
            break

    def check_under_10k(self):
        for o in self.vehicle.Offers:
            if o.OfferTypeID == 5 and int(o.DueAtSigning2) < 10000:
                Today.time_taken(self.build_onepay)

    def build_onepay(self):
        while True:
            if self.website.error_check():
                break
            step_one = TabVehicleInfo(self.driver,self.website,self.vehicle)
            check_step_one = step_one.run()
            if check_step_one == False:
                break

            step_three = OfferTypeContainer(self.driver,self.website,self.vehicle)
            check_step_three = step_three.run(input=OfferTypeContainer.ONEPAY)# Checks off which DIoffertypes are used for catagorizing for display
            if check_step_three == False:
                break
             
            step_four = TabOfferContainer(self.driver,self.website,self.vehicle)
            check_step_four = step_four.run(input=TabOfferContainer.ONEPAY)#applies the CTA's, Offers Shown, Media Block, and Disclaimer
            if check_step_four == False:
                break
            
            step_six = Populate(self.driver,self.website,self.vehicle)
            step_six.run()# Populate vehicle offers
            #Possible Addition #broadcast_subscribers #Group up offers and broadcast them to specific sites.
            print('Completed Build OnePay Loop Successfully')
            break

    def run(self):
        Today.time_taken(self.build_special)
        if self.website.Domain == 'https://www.walser.com/':
            Today.time_taken(self.check_under_10k)

