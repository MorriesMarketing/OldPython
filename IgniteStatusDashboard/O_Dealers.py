


class Dealer():
    def __init__(self, **kwargs):
        self.ClientID = kwargs['ClientID']
        self.DealerID = kwargs['DealerID']
        self.DealerCode = kwargs['DealerCode']
        self.Name = kwargs['Name']
        self.Address = kwargs['Address']
        self.City = kwargs['City']
        self.StateID = kwargs['StateID']
        self.ZipCode = kwargs['ZipCode']
        self.County = kwargs['County']
        self.MSAccountID = kwargs['MSAccountID']
        self.VAutoFilename = kwargs['VAutoFilename']
        self.HomeNetFilename = kwargs['HomeNetFilename']
        self.ExportFilename = kwargs['ExportFilename']
        self.IsActive = kwargs['IsActive']
        self.CreatedDT = kwargs['CreatedDT']

        self.StockTypes = []


    def __repr__(self):
        return f"{self.ClientID} {self.DealerID} {self.DealerName} {self.Domain}"

    

