


class Dealer():
    def __init__(self, **kwargs):
        self.ClientID = kwargs['ClientID']
        self.DealerID = kwargs['DealerID']
        self.Name = kwargs['Name']
        if '/' in self.Name:
            self.Name = self.Name.replace('/','_')

        
        self.Vehicles = []

    def __repr__(self):
        return f"{self.ClientID} {self.DealerID} {self.Name}"

