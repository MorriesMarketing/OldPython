


class Dealer():
    def __init__(self, **kwargs):
        self.ClientID = kwargs['ClientID']
        self.DealerID = kwargs['DealerID']
        self.DealerName = kwargs['DealerName']
        self.Domain = kwargs['Domain']
        self.SpecialsPage = kwargs['SpecialsPage']
        self.SRP = kwargs['SRP1']
        if self.SRP == None:
            pass
        elif ',' in self.SRP:
            self.SRP = list(self.SRP.split(','))
        else:
            self.SRP = list(self.SRP)
        self.FirstSearchQueryItem = kwargs['FirstSearchQueryItem']
        self.FirstImageSelector = kwargs['FirstImageSelector']
        self.FirstImageSelector = list(self.FirstImageSelector.split(','))
        self.FirstImageSelector2 = kwargs['FirstImageSelector2']
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

    def __repr__(self):
        return f"{self.ClientID} {self.DealerID} {self.DealerName} {self.Domain}"

    

