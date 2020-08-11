
class Vehicle:

    def __init__(self, **kwargs):
        self.ClientID = kwargs['ClientID']
        self.DealerID = kwargs['DealerID']
        self.VehicleID = kwargs['VehicleID']
        #self.MarketScanID = kwargs['MarketScanID']
        self.StockNumber = kwargs['StockNumber']
        self.VIN = kwargs['VIN']
        self.DealerCode = kwargs['DealerCode']
        self.State = kwargs['State']
        self.MakeName = kwargs['BrandName']
        self.ModelName = kwargs['Model']
        self.ModelNumber = kwargs['ModelNumber']
        self.Trim = kwargs['Trim']
        #self.Title = kwargs['Title']
        self.Year = kwargs['Year']
        self.Invoice = kwargs['Invoice']
        self.SellingPrice = kwargs['SellingPrice']
        self.MSRP = kwargs['MSRP']
        self.StockType = kwargs['StockType']

        self.YearMake = f'{self.Year} {self.MakeName}'
        self.YearMakeModel = f'{self.Year} {self.MakeName} {self.ModelName}'
        self.YearMakeModelTrim = f'{self.Year} {self.MakeName} {self.ModelName} {self.Trim}'
        self.MakeModel = f'{self.MakeName} {self.ModelName}'

        self.YearMakeurl = self.YearMake.replace(' ','-')
        self.YearMakeModelurl = self.YearMakeModel.replace(' ','-')
        self.YearMakeModelTrimurl = self.YearMakeModelTrim.replace(' ','-')
        self.MakeModelurl = self.MakeModel.replace(' ','-')
        self.Modelurl = self.ModelName.replace(' ','-')
        
        self.Inventory = self.YearMakeModel.replace(' ','+')
        self.InventoryUrl = ''

        self.Image = None

        self.Offers = []
        self.Html = ''
        self.HtmlOffers = ''


    def __repr__(self):
        return f"{self.ClientID} {self.DealerID} {self.VehicleID} {self.YearMakeModel}"

class VehicleAged:

    def __init__(self, **kwargs):
        self.DealerCode = kwargs['DealerCode']
        self.StockNumber = kwargs['StockNumber']
        self.VIN = kwargs['VIN']
        
        

    def __repr__(self):
        return f"{self.StockNumber}"
    