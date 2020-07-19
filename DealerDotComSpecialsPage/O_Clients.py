
# Called using SqlServer.PRD_Client_ReadData()
class Client():
    def __init__(self, **kwargs):
        self.ClientID = kwargs['ClientID']
        self.Name = kwargs['Name']
        self.Location = kwargs['Location']
        self.Phone = kwargs['Phone']
        self.Website = kwargs['Website']
        self.IsActive = kwargs['IsActive']
        self.Batch = None

        self.Dealers = []
        self.Vehicles = []
        self.Html = ''
        self.HtmlVehicles = ''


    def __repr__(self):
        return f"{self.ClientID} {self.Name}"

    

