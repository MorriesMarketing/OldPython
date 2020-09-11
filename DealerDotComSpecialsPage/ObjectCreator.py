from I_SqlServer import *
from I_SqlLight import *
from O_Batch import *
from O_Clients import *
from O_Dealers import * 
from O_Vehicles import *
from O_Images import *
from O_Offers import *
from O_OrderGroups import *
from O_OfferTypes import *


class ObjectCreator():
    #Project DealerDotComSpecialsPage

    def __init__(self):
        self.images = ObjectCreator.create_list_of_objects(DatabaseTable=SqlServer.PRD_ClientVehicles_Photos(), Object=Image, Seperator='VIN')
        self.client_order = ObjectCreator.create_list_of_objects(DatabaseTable=SqlServer.PRD_VehicleOffers_ClientRank(), Object=ClientGroup, Seperator='VehicleID')
        self.dealer_order = ObjectCreator.create_list_of_objects(DatabaseTable=SqlServer.PRD_VehicleOffers_DealerRank(), Object=DealerGroup, Seperator='VehicleID')
        self.batches = ObjectCreator.create_list_of_objects(DatabaseTable=SqlServer.PRD_Batch_RefreshCheck(), Object=Batch, Seperator='ClientID')
        self.clients = ObjectCreator.create_list_of_objects(DatabaseTable=SqlServer.PRD_Client_ReadData(), Object=Client, Seperator='ClientID')
        self.dealers = ObjectCreator.create_list_of_objects(DatabaseTable=SqlLight.DeskTop_Websites_ReadData(), Object=Dealer, Seperator='DealerID')
        self.vehicle_photos = ObjectCreator.create_list_of_objects(DatabaseTable=SqlLight.DeskTop_VehiclePhotos_ReadData(), Object=VehiclePhoto, Seperator=None)
        self.offertypes = ObjectCreator.create_list_of_objects(DatabaseTable=SqlServer.PRD_OfferType_ReadData(), Object=OfferType, Seperator=None)
        self.vehicles = ObjectCreator.create_list_of_objects(DatabaseTable=SqlServer.PRD_PythonOffers_ReadData(), Object=Vehicle, Seperator='VIN')
        self.offers = ObjectCreator.create_list_of_objects(DatabaseTable=SqlServer.PRD_PythonOffers_ReadData(), Object=Offer, Seperator=None)
        
    @staticmethod
    def create_list_of_objects(DatabaseTable,Object,Seperator):
        print(f'Creating {DatabaseTable} Objects')
        data_table = DatabaseTable
        data = Database.convert_table_to_dict(data_table)
        if Seperator == None:
            object_list = Database.create_objects(data, Object)
        else:
            object_list = Database.create_grouped_objects(data, Object, Seperator)

        return object_list
    
    def apply_image_object_to_vehicles(self):
        for v in self.vehicles:
            for i in self.images:
                if v.VIN == i.VIN:
                    v.Image = i

    def apply_url_data_to_vehicle_image(self):
        print('Combined Image Object to Vehicle Object')
        for v in self.vehicles:
            for vp in self.vehicle_photos:
                if vp.VIN == v.VIN and vp.ClientID == v.ClientID and vp.DealerID == v.DealerID:
                    if v.Image.UrlVdp == None:
                        v.Image.UrlVdp = vp.UrlVdp
                    if v.Image.PhotoURL == None:
                        v.Image.PhotoURL = vp.UrlImage

    def apply_offers_to_vehicle(self):
        for v in self.vehicles:
            for o in self.offers:
                if v.VehicleID == o.VehicleID and o.OfferTypeID != 8 and o.OfferTypeID != 2:
                    v.Offers.append(o)

    def create_clients_dealers_vehicles_offers(self, TestActive):

        if TestActive == True:
            pass
        else:
            ObjectCreator.apply_image_object_to_vehicles(self)

            ObjectCreator.apply_url_data_to_vehicle_image(self)

            ObjectCreator.apply_offers_to_vehicle(self)

            for d in self.dealers:
                for do in self.dealer_order:
                    if do.DealerID == d.DealerID:
                        for v in self.vehicles:
                            if do.VehicleID == v.VehicleID:
                                d.Vehicles.append(v)
                                if v.Year not in d.Years:
                                    d.Years.append(v.Year)
                                if v.MakeName not in d.Makes:
                                    d.Makes.append(v.MakeName)
                                if [v.ModelName,v.Modelurl] not in d.Models:
                                    d.Models.append([v.ModelName,v.Modelurl])
                for ot in self.offertypes:
                    print(ot)
                    d.OfferTypes.append(ot)
            
                #for v in vehicles:
                #    if v.Year not in d.Years:
                #        d.Years.append(v.Year)
                #    if v.MakeName not in d.Makes:
                #        d.Makes.append(v.MakeName)
                #    if [v.ModelName,v.Modelurl] not in d.Models:
                #        d.Models.append([v.ModelName,v.Modelurl])

                d.Years.sort()
                d.Makes.sort()
                d.Models.sort()

            for c in self.clients:
                for b in self.batches:
                    if c.ClientID == b.ClientID:
                        c.Batch = b
                for d in self.dealers:
                    if c.ClientID == d.ClientID:
                        c.Dealers.append(d)
                    
                for co in self.client_order:
                    if co.ClientID == c.ClientID:
                        for v in self.vehicles:
                            if co.VehicleID == v.VehicleID:
                                c.Vehicles.append(v)
                                if v.Year not in c.Years:
                                    c.Years.append(v.Year)
                                if v.MakeName not in c.Makes:
                                    c.Makes.append(v.MakeName)
                                if [v.ModelName,v.Modelurl] not in c.Models:
                                    c.Models.append([v.ModelName,v.Modelurl])
                c.Years.sort()
                c.Makes.sort()
                c.Models.sort()
            print('Clients Created')
            return self.clients

