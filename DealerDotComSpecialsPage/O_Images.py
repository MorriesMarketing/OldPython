class Image:

    def __init__(self, **kwargs):
        self.ClientID = kwargs['ClientID']
        self.DealerID = kwargs['DealerID']
        self.VehicleID = kwargs['VehicleID']
        self.UrlVdp = None
        self.PhotoURL = kwargs['PhotoURL']
        self.VdpActive = None
        
    def __repr__(self):
        return f"{self.ClientID} {self.DealerID} {self.VehicleID} {self.UrlVdp}"

