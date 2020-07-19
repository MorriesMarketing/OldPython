
class Offer:

    def __init__(self, **kwargs):
        self.ClientID = kwargs['ClientID']
        self.DealerID = kwargs['DealerID']
        self.VehicleID = kwargs['VehicleID']
        self.VIN = kwargs['VIN']
        self.Payment = kwargs['Payment']
        self.BasePayment = kwargs['BasePayment']
        self.PaymentNoTax = kwargs['PaymentNoTax']
        #self.LeaseSpecial = kwargs['LeaseSpecial']
        self.Lender = kwargs['Lender']
        self.Mileage = kwargs['Mileage']
        self.Term = kwargs['Term']
        self.DownPayment = kwargs['Downpayment']
        self.DueAtSigning = kwargs['DueAtSigning']
        self.TotalRebate = kwargs['TotalRebate']
        #self.UploadOrder = kwargs['UploadOrder']
        #self.VehicleRank = kwargs['VehicleRank']
        #self.ModelRank = kwargs['ModelRank']
        #self.ModelNoRank = kwargs['ModelNoRank']
        #self.LeaseOfferMileage = kwargs['LeaseOfferMileage']
        self.OfferTypeID = kwargs['OfferTypeID']
        self.OfferType = kwargs['OfferType']
        #self.DueAtSigning2 = kwargs['DueAtSigning2']

        self.Disclaimer = kwargs['Disclaimer']
        #self.LeaseOffer = kwargs['LeaseOffer']
        self.APR = round(kwargs['APR'], 1)
        self.OfferTypeurl = self.OfferType.replace(' ','-')


        self.Html = ''
    
    def __repr__(self):
        return f"OfferTypeID:{self.ClientID} {self.DealerID} {self.VehicleID} {self.OfferTypeID} {self.OfferType} {self.Payment} "

