
class Vehicle:

    def __init__(self, **kwargs):
        self.VehicleID = kwargs['VehicleID']
        self.MarketScanID = kwargs['MarketScanID']
        self.StockNumber = kwargs['StockNumber']
        self.VIN = kwargs['VIN']
        self.DealerCode = kwargs['DealerCode']
        self.State = kwargs['State']
        if kwargs['Brand'] == 'Mini':
            self.MakeName = 'MINI'
        elif kwargs['Brand'] == 'Gmc':
            self.MakeName = 'GMC'
        elif kwargs['Brand'] == 'Bmw':
            self.MakeName = 'BMW'
        else:
            self.MakeName = kwargs['Brand']
        self.ModelName = kwargs['Model']
        self.ModelNumber = kwargs['ModelNumber']
        self.Trim = kwargs['Trim']
        self.Title = kwargs['Title']
        self.Year = kwargs['Year']
        self.Mileage = kwargs['Mileage']
        self.Invoice = kwargs['Invoice']
        self.SellingPrice = kwargs['SellingPrice']
        self.MSRP = kwargs['MSRP']
        self.Image = ''
        self.StockType = ''
        self.UrlPicture = ''
        self.UrlVdp = ''
        self.YearMakeModelGroup = f'{self.Year} {self.MakeName} {self.ModelName}'
        self.YearMakeGroup = f'{self.Year} {self.MakeName}'
        self.MakeModelGroup = f'{self.MakeName} {self.ModelName}'
        self.YearMakeModelTrimGroup = f'{self.Year} {self.MakeName} {self.ModelName} {self.Trim}'
        
        self.Offers = []

    def __repr__(self):
        return f"{self.StockNumber} {self.YearMakeModelGroup}"


class VehicleAged:

    def __init__(self, **kwargs):
        self.DealerCode = kwargs['DealerCode']
        self.StockNumber = kwargs['StockNumber']
        self.VIN = kwargs['VIN']
        
        

    def __repr__(self):
        return f"{self.StockNumber}"
    