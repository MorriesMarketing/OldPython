


class Dealer():
    def __init__(self, **kwargs):
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
        self.OfferTypesOnLoad = kwargs['OfferTypesOnLoad']
        self.Vehicles = []
        self.Html = ''
        self.HtmlVehicles = ''

    def __repr__(self):
        return f"{self.ClientID} {self.DealerID} {self.DealerName} {self.Domain}"

    

