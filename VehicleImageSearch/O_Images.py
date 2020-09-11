class Image:

    def __init__(self, **kwargs):
        self.ClientID = kwargs['ClientID']
        self.DealerID = kwargs['DealerID']
        self.VIN = kwargs['VIN']
        self.UrlVdp = None
        self.PhotoURL = kwargs['PhotoURL']
        self.VdpActive = None
        
    def __repr__(self):
        return f"{self.DealerID} {self.VIN} {self.UrlVdp}"

class VehiclePhoto:
    def __init__(self, **kwargs):
        self.ClientID = kwargs['ClientID']
        self.DealerID = kwargs['DealerID']
        self.Domain = kwargs['Domain']
        self.VehiclePhotoID = kwargs['VehiclePhotoID']
        self.VIN = kwargs['VIN']
        self.UrlVdp = kwargs['UrlVdp']
        self.UrlImage = kwargs['UrlImage']
        
    def __repr__(self):
        return f"{self.VehiclePhotoID} {self.VIN} {self.UrlVdp}"