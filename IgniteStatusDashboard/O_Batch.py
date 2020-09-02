

class Batch():
    def __init__(self, **kwargs):
        self.ClientID = kwargs['ClientID']
        self.BatchID = kwargs['BatchID']
        self.VehicleJobStartDT = kwargs['VehicleJobStartDT']
        self.VehicleJobEndDT = kwargs['VehicleJobEndDT']
        self.OfferJobStartDT = kwargs['OfferJobStartDT']
        self.OfferJobEndDT = kwargs['OfferJobEndDT']
        self.ExportJobStartDT = kwargs['ExportJobStartDT']
        self.ExportJobEndDT = kwargs['ExportJobEndDT']

        
        def __repr__(self):
            return f"{self.ClientID} {self.BatchID} {self.ExportJobEndDT}"
        


