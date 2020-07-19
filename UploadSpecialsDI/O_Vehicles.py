
class Vehicle:

    def __init__(self, **kwargs):
        self.VehicleID = kwargs['VehicleID']
        ##self.MarketScanID = kwargs['MarketScanID']
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

        if kwargs['Brand'] == 'Chrysler' or kwargs['Brand'] == 'Jeep' or kwargs['Brand'] == 'Dodge' or kwargs['Brand'] == 'Ram' :
            self.Brand = 'FCA'
        elif kwargs['Brand'] == 'Gmc' or kwargs['Brand'] == 'Buick':
            self.Brand = 'GM'
        else:
            self.Brand = kwargs['Brand']

        self.ModelName = kwargs['Model']
        self.ModelNumber = kwargs['ModelNumber']
        self.Trim = kwargs['Trim']
        self.Title = kwargs['Title']
        self.Year = kwargs['Year']
        self.Mileage = kwargs['Mileage']
        self.Invoice = kwargs['Invoice']
        self.SellingPrice = kwargs['SellingPrice']
        self.MSRP = kwargs['MSRP']
        self.Image = None
        self.YearMakeModelGroup = f'{self.Year} {self.MakeName} {self.ModelName}'
        self.YearMakeGroup = f'{self.Year} {self.MakeName}'
        self.MakeModelGroup = f'{self.MakeName} {self.ModelName}'
        self.YearMakeModelTrimGroup = f'{self.Year} {self.MakeName} {self.ModelName} {self.Trim}'
        
        self.Offers = []

    def create_vehicle_html(self,htmloffers):
        html = """<div>
			<div style="width:100%;height:200px;">
			    <img id="{self.Year}-{self.Make}-{self.Model}-{self.Trim}" src="{self.PhotoURL}" alt="{self.Year}-{self.Make}-{self.Model}-{self.Trim}" style="float:left;width:100%;height:100%;object-fit:cover;">
			</div>

			<div class="vehicle-title">{self.Year} {self.Make} {self.Model} {self.Trim}</div>
            </br></br>
            {htmloffers}
            <div class="buttonz">
				<button type="button" class="btn btn-primary">View Vehicle</button>
				<!--<button type="button" class="btn btn-primary">View Inventory</button>--> 
				<button type="button" class="btn btn-primary">Claim Offer</button>
			</div>
		</div>"""
        return html

    def __repr__(self):
        return f"{self.StockNumber} {self.YearMakeModelGroup}"

class VehicleAged:

    def __init__(self, **kwargs):
        self.DealerCode = kwargs['DealerCode']
        self.StockNumber = kwargs['StockNumber']
        self.VIN = kwargs['VIN']
        
        

    def __repr__(self):
        return f"{self.StockNumber}"
    