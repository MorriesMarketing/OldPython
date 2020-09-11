
# Called using SqlServer.PRD_Client_ReadData()
class Client():
    def __init__(self, **kwargs):
        self.ClientID = kwargs['ClientID']
        self.Name = kwargs['Name']
        self.Location = kwargs['Location']
        self.Phone = kwargs['Phone']
        self.Website = kwargs['Website']
        self.IsActive = kwargs['IsActive']
        self.CreatedDT = kwargs['CreatedDT']
        self.WebID = kwargs['WebID']
        self.Batch = None

        self.Dealers = []

    def __repr__(self):
        return f"{self.ClientID} {self.Name}"

    

