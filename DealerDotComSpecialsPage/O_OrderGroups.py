

class ClientGroup():
    def __init__(self, **kwargs):
        self.ClientID = kwargs['ClientID']
        self.DealerID = kwargs['DealerID']
        self.VehicleID = kwargs['VehicleID']
        self.Year = kwargs['Year']
        self.Model = kwargs['Model']
        self.BasePayment = kwargs['BasePayment']
        self.DealerRank = kwargs['DealerRank']
        self.ClientRank = kwargs['ClientRank']


class DealerGroup():
    def __init__(self, **kwargs):
        self.ClientID = kwargs['ClientID']
        self.DealerID = kwargs['DealerID']
        self.VehicleID = kwargs['VehicleID']
        self.Year = kwargs['Year']
        self.Model = kwargs['Model']
        self.BasePayment = kwargs['BasePayment']
        self.DealerRank = kwargs['DealerRank']
        self.ClientRank = kwargs['ClientRank']