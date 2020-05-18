
class Offer:

    def __init__(self, **kwargs):

        self.VehicleID = kwargs['VehicleID']
        self.Payment = kwargs['Payment']
        self.BasePayment = kwargs['BasePayment']
        self.PaymentNoTax = kwargs['PaymentNoTax']
        self.LeaseSpecial = kwargs['LeaseSpecial']
        self.Lender = kwargs['Lender']
        self.LeaseMi = kwargs['LeaseMi']
        self.Term = kwargs['Term']
        self.DownPayment = kwargs['DownPayment']
        self.DueAtSigning = kwargs['DueAtSigning']
        self.TotalRebate = kwargs['TotalRebate']
        self.UploadOrder = kwargs['UploadOrder']
        self.VehicleRank = kwargs['VehicleRank']
        self.ModelRank = kwargs['ModelRank']
        self.ModelNoRank = kwargs['ModelNoRank']
        self.LeaseOfferMileage = kwargs['LeaseOfferMileage']
        self.OfferTypeID = kwargs['OfferTypeID']
        self.DueAtSigning2 = kwargs['DueAtSigning2']

        self.Disclaimer = kwargs['Disclaimer']
        self.LeaseOffer = kwargs['LeaseOffer']
        self.APR = kwargs['APR']
    
    def __repr__(self):
        return f"OfferTypeID:{self.OfferTypeID} {self.LeaseSpecial} {self.LeaseOffer} "

