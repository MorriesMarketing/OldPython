


class ComparisonClients():
    def __init__(self,Group1 ,Group2):
        self.ClientID = [Group1.ClientID, Group2.ClientID]
        self.Name = [Group1.Name, Group2.Name]
        self.Location = [Group1.Location, Group2.Location]
        self.Phone = [Group1.Phone, Group2.Phone]
        self.Website = [Group1.Website, Group2.Website]
        self.IsActive = [Group1.IsActive, Group2.IsActive]

        self.Vehicles = []
        self.Batches = []

class ComparisonBatches():
    def __init__(self,Group1 ,Group2):
        self.ClientID = [Group1.ClientID, Group2.ClientID]
        self.MaxBatchID = [Group1.MaxBatchID, Group2.MaxBatchID]
        self.ExportJobEndDT = [Group1.ExportJobEndDT, Group2.ExportJobEndDT]
        self.JobYear = [Group1.JobYear, Group2.JobYear]
        self.JobMonth = [Group1.JobMonth, Group2.JobMonth]
        self.JobDay = [Group1.JobDay, Group2.JobDay]
        self.JobHour = [Group1.JobHour, Group2.JobHour]
        self.LocalTime = [Group1.LocalTime, Group2.LocalTime]
        self.CurrentYear = [Group1.CurrentYear, Group2.CurrentYear]
        self.CurrentMonth = [Group1.CurrentMonth, Group2.CurrentMonth]
        self.CurrentDay = [Group1.CurrentDay, Group2.CurrentDay]
        self.CurrentHour = [Group1.CurrentHour, Group2.CurrentHour]


class ComparisonVehiclesOffers():
    def __init__(self,**kwargs):
        self.ClientID = kwargs['ClientID']
        self.DealerID = kwargs['DealerID']
        self.VehicleID = kwargs['VehicleID']
        self.BatchID = kwargs['BatchID']
        self.StockNumber = kwargs['StockNumber']
        self.VIN = kwargs['VIN']
        self.DealerCode = kwargs['DealerCode']
        self.State = kwargs['State']
        self.County = kwargs['County']
        self.ZipCode = kwargs['ZipCode']

        self.MakeName = kwargs['BrandName']
        self.ModelName = kwargs['Model']
        self.ModelNumber = kwargs['ModelNumber']
        self.Trim = kwargs['Trim']
        self.Year = kwargs['Year']
        self.Invoice = kwargs['Invoice']
        self.SellingPrice = kwargs['SellingPrice']
        self.MSRP = kwargs['MSRP']
        self.DealerPrice = kwargs['DealerPrice']
        self.PriceOption = kwargs['PriceOption']

        self.StockType = kwargs['StockType']
        self.Payment = kwargs['Payment']
        self.BasePayment = kwargs['BasePayment']
        self.PaymentNoTax = kwargs['PaymentNoTax']
        self.Lender = kwargs['Lender']
        self.Mileage = kwargs['Mileage']
        self.Term = kwargs['Term']
        self.DownPayment = kwargs['Downpayment']
        self.DueAtSigning = kwargs['DueAtSigning']
        self.TotalRebate = kwargs['TotalRebate']
        self.OfferTypeID = kwargs['OfferTypeID']
        self.OfferType = kwargs['OfferType']
        self.Disclaimer = kwargs['Disclaimer']
        self.APR = kwargs['APR']
        self.OfferRank = kwargs['OfferRank']
        self.ModelRank = kwargs['ModelRank']
        self.ModelNoRank = kwargs['ModelNoRank']
        self.ClientName = kwargs['ClientName']
        self.RegistrationFee = kwargs['RegistrationFee']
        self.AcquisitionFee = kwargs['AquisitionFee']
        self.InceptionFees = kwargs['InceptionFees']
        self.OtherFees = kwargs['OtherFees']
        self.TotalRebate = kwargs['TotalRebate']
        self.MarkupRate = kwargs['MarkupRate']
        self.BuyRate = kwargs['BuyRate']
        self.SellRate = kwargs['SellRate']
        self.PaidReserve = kwargs['PaidReserve']
        self.AmountFinanced = kwargs['AmountFinanced']
        self.ResidualPercent = kwargs['ResidualPercent']
        self.ResidualDollar = kwargs['ResidualDollar']
        self.MaxAdvance = kwargs['MaxAdvance']
        self.SalesTax = kwargs['SalesTax']
        self.ProgramCode = kwargs['ProgramCode']
        self.HasOEMException = kwargs['HasOEMException']
        self.PriceChange = kwargs['PriceChange']
        self.IsCaptive = kwargs['IsCaptive']
        self.IsSpecial = kwargs['IsSpecial']
        self.IsVisible = kwargs['IsVisible']
        self.VINOffer = f'{self.VIN}{self.OfferTypeID}'



    def __repr__(self):
        return f"{self.ClientID} {self.DealerID} {self.VIN} {self.OfferTypeID}"






