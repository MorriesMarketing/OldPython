

class Ignite_Settings():
    def __init__(self, **kwargs):
        #ID Numbers
        self.ClientID = kwargs['ClientID']
        self.DealerID = kwargs['DealerID']
        self.BatchID = kwargs['BatchID']
        self.VehicleID = kwargs['VehicleID']
        self.OfferID = kwargs['OfferID']
        self.OfferTypeID = kwargs['OfferTypeID']
        #Client & Dealer Info
        self.ClientName = kwargs['ClientName']
        self.State = kwargs['State']
        #Rank Info
        self.OfferRank = kwargs['OfferRank']
        self.ModelRank = kwargs['ModelRank']
        self.ModelNoRank = kwargs['ModelNoRank']
        #Vehicle Info
        self.BrandName = kwargs['BrandName']
        self.Year = kwargs['Year']
        self.Model = kwargs['Model']
        self.ModelNumber = kwargs['ModelNumber']
        self.StockType = kwargs['StockType']
        self.StockNumber = kwargs['StockNumber']
        self.VIN = kwargs['VIN']
        #Offer Info
        self.OfferType = kwargs['OfferType']
        self.Lender = kwargs['Lender']
        self.IsCaptive = kwargs['IsCaptive']
        self.IsSpecial = kwargs['IsSpecial']
        self.IsVisible = kwargs['IsVisible']
        
        self.Vehicles = []

        def __repr__(self):
            return f"Client:{self.ClientID} {self.ClientName} {self.DealerID} "