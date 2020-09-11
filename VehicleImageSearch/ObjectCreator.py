from I_SqlServer import *
from I_SqlLight import *
from O_Dealers import * 
from O_Vehicles import *
from O_Images import *
#from C_VehicleImageSearch import VehicleImageSearch
from Soup import *
from O_Pages import *

class ObjectCreator():
    #Project VehicleImageSearch
    def __init__(self, TestActive):
        self.images = ObjectCreator.create_list_of_objects(DatabaseTable=SqlServer.PRD_ClientVehicles_Photos(), Object=Image, Seperator='VIN')
        self.vehicles = ObjectCreator.create_list_of_objects(DatabaseTable=SqlServer.PRD_ClientVehicles_ReadData(), Object=Vehicle, Seperator='VIN')
        self.dealers = ObjectCreator.create_list_of_objects(DatabaseTable=SqlLight.DeskTop_Websites_ReadData(), Object=Dealer, Seperator=None)
        #self.website = VehicleImageSearch()
        self.vehicle_photos = ObjectCreator.create_list_of_objects(DatabaseTable=SqlLight.DeskTop_VehiclePhotos_ReadData(), Object=VehiclePhoto, Seperator=None)
        self.TestActive = TestActive

    #def create_objects(self):

        #print('Creating Image Objects')
        #data_table = SqlServer.PRD_ClientVehicles_Photos()
        #data = Database.convert_table_to_dict(data_table)
        #self.images = Database.create_grouped_objects(data, Image, 'VIN')
        #
        #print('Creating Vehicle Objects')
        #data_table = SqlServer.PRD_ClientVehicles_ReadData()
        #data = Database.convert_table_to_dict(data_table)
        #self.vehicles = Database.create_grouped_objects(data, Vehicle, 'VIN')
        #
        #print('Creating Dealer Objects')
        #data_table = SqlLight.DeskTop_Websites_ReadData()
        #data = Database.convert_table_to_dict(data_table)
        #self.dealers = Database.create_grouped_objects(data, Dealer, 'WebsiteID')
        #
        #print('Creating Photo Objects')
        #data_table = SqlLight.DeskTop_VehiclePhotos_ReadData()
        #data = Database.convert_table_to_dict(data_table)
        #self.vehicle_photos = Database.create_objects(data, VehiclePhoto)

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


    def gather_vdp_website_list(self):
            
        for d in self.dealers:
            if d.ActiveSpecialsPage == True:
                if d.DealerInspireSite == True:
                    flag = Soup.DEALER_INSPIRE_XML
                elif d.DealerDotComSite == True:
                    flag = Soup.DEALER_DOT_COM_XML
                elif d.CdkSite == True:
                    flag = Soup.CDK_XML

                soup = Soup(Domain=d.Domain,Flag=flag)
                list_of_vdp_urls = soup.scrape_xml_page(Domain=d.Domain,Page=soup.sitemap_xml)
                remaining_list_of_vdp_urls = soup.trim_list_of_pre_existing_values(self.vehicle_photos,list_of_vdp_urls)

                for page in remaining_list_of_vdp_urls:

                    returned_dict = soup.scrap_image_and_vin(f'{d.Domain}{page}')
                    inventory_page = Page()
                    inventory_page.Domain = d.Domain
                    inventory_page.VdpUrl = page
                    inventory_page.VdpImage = returned_dict['ImageUrl']
                    try:
                        vin = returned_dict['VIN'].upper()
                    except:
                        vin = returned_dict['VIN']
                    inventory_page.VIN = vin
                    if inventory_page.VIN != None:
                        d.Pages.append(inventory_page)
                        print(inventory_page)
                    if inventory_page.VIN != None and inventory_page.VdpUrl != None and inventory_page.VdpImage != None:
                        SqlLight.DeskTop_VehiclePhotos_Write(d.ClientID,d.DealerID,d.Domain,inventory_page.VIN,inventory_page.VdpUrl,inventory_page.VdpImage)
               
    def combine_objects(self):
        for i in self.images:
            for v in self.vehicles:
                if v.VIN == i.VIN and i.ClientID == v.ClientID:
                    v.Image = i

        for v in self.vehicles:
            for vp in self.vehicle_photos:
                if vp.VIN == v.VIN and vp.ClientID == v.ClientID:
                    if v.Image.UrlVdp == None:
                        v.Image.UrlVdp = vp.UrlVdp
                    if v.Image.PhotoURL == None:
                        v.Image.PhotoURL = vp.UrlImage

        if self.TestActive:
            pass
        else:
            for d in self.dealers:
                if d.ActiveSpecialsPage == True:
                    
                    for v in self.vehicles:
                        if v.Image.UrlVdp == None:
                                
                            for p in d.Pages:
                                if v.VIN == p.VIN:
                                    if v.Image.UrlVdp == None:
                                        v.Image.UrlVdp = p.VdpUrl
                                    if v.Image.PhotoURL == None:
                                        v.Image.PhotoURL = p.VdpImage
                            if v.Image.UrlVdp != None and v.Image.PhotoURL != None:
                                SqlLight.DeskTop_VehiclePhotos_Write(v.ClientID,v.DealerID,d.Domain,v.VIN,v.Image.UrlVdp,v.Image.PhotoURL)


