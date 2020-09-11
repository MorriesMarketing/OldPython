


class Dealer():
    #Project VehicleImageSearch
    def __init__(self, **kwargs):
        self.WebsiteID = kwargs['WebsiteID']
        self.ClientID = kwargs['ClientID']
        self.DealerID = kwargs['DealerID']
        self.DealerName = kwargs['DealerName']
        self.Domain = kwargs['Domain']
        self.SpecialsPage = kwargs['SpecialsPage']
        self.UserName = kwargs['UserName']
        self.Password = kwargs['Password']
        self.GroupSite = kwargs['GroupSite']
        self.DealerInspireSite = kwargs['DealerInspireSite']
        self.DealerDotComSite = kwargs['DealerDotComSite']
        self.CdkSite = kwargs['CdkSite']
        self.ActiveSpecialsPage = kwargs['ActiveSpecialsPage']
        self.MakesToRun = kwargs['MakesToRun']
        self.ModelsToRun = kwargs['ModelsToRun']
        self.OfferTypeIDsActive = kwargs['OfferTypeIDsActive']
        self.OfferTypeIDsActive = list(self.OfferTypeIDsActive.split(','))
        self.OfferTypesOnLoad = kwargs['OfferTypesOnLoad']
        self.OfferTypesOnLoad = list(self.OfferTypesOnLoad.split(','))
        self.Vehicles = []
        self.Html = ''
        self.HtmlVehicles = ''
        self.OfferTypes = []
        self.Years = []
        self.Makes = []
        self.Models = []
        self.Pages = []

    def __repr__(self):
        return f"{self.ClientID} {self.DealerID} {self.DealerName} {self.Domain}"

    

