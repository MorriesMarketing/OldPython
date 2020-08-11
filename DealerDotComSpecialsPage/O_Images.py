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

class VehiclePhoto:
    def __init__(self, **kwargs):
        self.ClientID = kwargs['ClientID']
        self.DealerID = kwargs['DealerID']
        self.VehiclePhotoID = kwargs['VehiclePhotoID']
        self.VIN = kwargs['VIN']
        self.UrlVdp = kwargs['UrlVdp']
        self.UrlImage = kwargs['UrlImage']
        
    def __repr__(self):
        return f"{self.VehiclePhotoID} {self.VIN} {self.UrlVdp}"