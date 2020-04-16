from I_SqlServer import *
from O_Vehicles import *
from O_Offers import *


class DigitalMarketing():

    @staticmethod
    def create_vehicles_from_VehicleSpecialsNew():
        #step 1: creating a list of vehicles and grouping by stocknumber 
        data_table = SqlServer.PRD_OfferSpecialsUpload_ReadData()
        data = Database.convert_table_to_dict(data_table)
        vehicles = Database.create_grouped_objects(data, Vehicle, 'StockNumber')

        #Step 2 creating the list of offers
        data_table = SqlServer.PRD_OfferSpecialsUpload_ReadData()
        data = Database.convert_table_to_dict(data_table)
        offers = Database.create_objects(data, Offer)

        # combine offer objects into vehicle objects
        for v in vehicles:
            for o in offers:
                if v.VehicleID == o.VehicleID:
                    v.Offers.append(o)
        
        return vehicles
