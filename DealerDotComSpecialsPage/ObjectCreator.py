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
from O_Websites import Website_DealerDotCom

class ObjectCreator():

    def __init__():
        pass

    @staticmethod
    def create_clients_dealers_vehicles_offers(TestActive):

        print('Creating Image Objects')
        data_table = SqlServer.PRD_Vehicles_Photos()
        data = Database.convert_table_to_dict(data_table)
        images = Database.create_grouped_objects(data, Image, 'VehicleID')

        print('Creating Vehicle Objects')
        data_table = SqlServer.PRD_PythonOffers_ReadData()
        data = Database.convert_table_to_dict(data_table)
        vehicles = Database.create_grouped_objects(data, Vehicle, 'VehicleID')

        print('Creating Offer Objects')
        data_table = SqlServer.PRD_PythonOffers_ReadData()
        data = Database.convert_table_to_dict(data_table)
        offers = Database.create_objects(data, Offer)

        print('Creating ClientGroup Objects')
        data_table = SqlServer.PRD_VehicleOffers_ClientRank()
        data = Database.convert_table_to_dict(data_table)
        client_order = Database.create_grouped_objects(data, ClientGroup, 'VehicleID')
        
        print('Creating DealerGroup Objects')
        data_table = SqlServer.PRD_VehicleOffers_DealerRank()
        data = Database.convert_table_to_dict(data_table)
        dealer_order = Database.create_grouped_objects(data, DealerGroup, 'VehicleID')
        
        print('Creating Batch Objects')
        data_table = SqlServer.PRD_Batch_RefreshCheck()
        data = Database.convert_table_to_dict(data_table)
        batches = Database.create_grouped_objects(data, Batch, 'ClientID')

        print('Creating Client Objects')
        data_table = SqlServer.PRD_Client_ReadData()
        data = Database.convert_table_to_dict(data_table)
        clients = Database.create_grouped_objects(data, Client, 'ClientID')

        print('Creating Dealer Objects')
        data_table = SqlLight.DeskTop_Websites_ReadData()
        data = Database.convert_table_to_dict(data_table)
        dealers = Database.create_grouped_objects(data, Dealer, 'DealerID')

        print('Creating OfferType Objects')
        data_table = SqlServer.PRD_OfferType_ReadData()
        data = Database.convert_table_to_dict(data_table)
        offertypes = Database.create_objects(data, OfferType)

        for v in vehicles:
            for i in images:
                if v.VehicleID == i.VehicleID:
                    v.Image = i
        
        if TestActive:
            pass
        else:
            for d in dealers:
                if d.ActiveSpecialsPage == 1:
                    website = Website_DealerDotCom()
                    for v in vehicles:
                        if v.Image.UrlVdp == None and v.DealerID == d.DealerID:
                            v.InventoryUrl = f'{d.Domain}{website.Search}{v.Inventory}'
                            acquire_image = False
                            if v.Image.PhotoURL == None:
                                acquire_image = True
                            image_data = website.find_vdp(d.Domain,d.SRP,v.VIN,acquire_image)
                            v.Image.UrlVdp = image_data[1]
                            if acquire_image:
                                v.Image.PhotoURL = image_data[2]
                            print(v.Image)
            website.driver.quit()

        for v in vehicles:
            for o in offers:
                if v.VehicleID == o.VehicleID and o.OfferTypeID != 8 and o.OfferTypeID != 2:
                    v.Offers.append(o)

        for d in dealers:
            for do in dealer_order:
                if do.DealerID == d.DealerID:
                    for v in vehicles:
                        if do.VehicleID == v.VehicleID:
                            d.Vehicles.append(v)
                            if v.Year not in d.Years:
                                d.Years.append(v.Year)
                            if v.MakeName not in d.Makes:
                                d.Makes.append(v.MakeName)
                            if [v.ModelName,v.Modelurl] not in d.Models:
                                d.Models.append([v.ModelName,v.Modelurl])
            for ot in offertypes:
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

        for c in clients:
            for b in batches:
                if c.ClientID == b.ClientID:
                    c.Batch = b
            for d in dealers:
                if c.ClientID == d.ClientID:
                    c.Dealers.append(d)
                    
            for co in client_order:
                if co.ClientID == c.ClientID:
                    for v in vehicles:
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
        return clients

