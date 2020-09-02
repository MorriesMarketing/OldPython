class StockType():
    def __init__(self, **kwargs):
        self.ClientID = kwargs['ClientID']
        self.DealerID = kwargs['DealerID']
        self.StockType = kwargs['StockType']


    def __repr__(self):
        return f"{self.ClientID} {self.DealerID} {self.StockType}"