from I_SqlServer import *
from I_SqlLight import *
from O_Dealers import * 
from O_Vehicles import *
from O_Images import *
from C_VehicleImageSearch import VehicleImageSearch

class ObjectCreator():

    def __init__(self, TestActive):
        self.images = None
        self.vehicles = None
        self.dealers = None
        self.website = VehicleImageSearch()
        self.vehicle_photos = None
        self.TestActive = TestActive

    def create_objects(self):

        print('Creating Image Objects')
        data_table = SqlServer.PRD_Vehicles_Photos()
        data = Database.convert_table_to_dict(data_table)
        self.images = Database.create_grouped_objects(data, Image, 'VIN')

        print('Creating Vehicle Objects')
        data_table = SqlServer.PRD_PythonOffers_ReadData()
        data = Database.convert_table_to_dict(data_table)
        self.vehicles = Database.create_grouped_objects(data, Vehicle, 'VIN')

        print('Creating Dealer Objects')
        data_table = SqlLight.DeskTop_Websites_ReadData()
        data = Database.convert_table_to_dict(data_table)
        self.dealers = Database.create_grouped_objects(data, Dealer, 'DealerID')
        
        print('Creating Photo Objects')
        data_table = SqlLight.DeskTop_VehiclePhotos_ReadData()
        data = Database.convert_table_to_dict(data_table)
        self.vehicle_photos = Database.create_objects(data, VehiclePhoto)

    def combine_objects(self):
        for v in self.vehicles:
            for i in self.images:
                if v.VIN == i.VIN:
                    v.Image = i

        for v in self.vehicles:
            for vp in self.vehicle_photos:
                if vp.VIN == v.VIN and vp.ClientID == v.ClientID and vp.DealerID == v.DealerID:
                    if v.Image.UrlVdp == None:
                        v.Image.UrlVdp = vp.UrlVdp
                    if v.Image.PhotoURL == None:
                        v.Image.PhotoURL = vp.UrlImage
        
        if self.TestActive:
            pass
        else:
            for d in self.dealers:
                if d.ActiveSpecialsPage == 1 and d.GroupSite == 0:
                    #self.website = VehicleImageSearch()
                    for v in self.vehicles:
                        if v.DealerID == d.DealerID and v.StockType == 'New':
                            if v.Image.PhotoURL == None or v.Image.UrlVdp == None:
                                image_data = self.website.search_vehicle_page(d,v)
                                if v.Image.UrlVdp == None:
                                    v.Image.UrlVdp = image_data[0]
                                if v.Image.PhotoURL == None:
                                    v.Image.PhotoURL = image_data[1]
                                print(v.Image)
                                if v.Image.UrlVdp != None and v.Image.PhotoURL != None:
                                    SqlLight.DeskTop_VehiclePhotos_Write(v.ClientID,v.DealerID,v.VIN,v.Image.UrlVdp,v.Image.PhotoURL)
            self.website.driver.quit()


