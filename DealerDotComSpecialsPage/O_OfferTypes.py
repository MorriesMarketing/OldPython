class OfferType():
    #Project DealerDotComSpecialsPage
    def __init__(self, **kwargs):
        self.OfferTypeID = kwargs['OfferTypeID']
        self.Name = kwargs['Name']
        if self.OfferTypeID == 1:
            self.Description = '$0 Down Payment'
        elif self.OfferTypeID == 3:
            self.Description = '10% MSRP Down'
        else:
            self.Description = kwargs['Description']
        if 'Lease' in self.Name:
            self.DealType = 'Lease'
        elif 'Finance' in self.Name:
            self.DealType = 'Finance'
        else:
            self.DealType = ''

    def __repr__(self):
        return f"{self.OfferTypeID} {self.Name} {self.DealType}"
