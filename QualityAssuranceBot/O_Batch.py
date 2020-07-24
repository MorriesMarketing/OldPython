

class Batch():
    def __init__(self, **kwargs):
        self.ClientID = kwargs['ClientID']
        self.MaxBatchID = kwargs['MaxBatchID']
        self.ExportJobEndDT = kwargs['ExportJobEndDT']
        self.JobYear = kwargs['JobYear']
        self.JobMonth = kwargs['JobMonth']
        self.JobDay = kwargs['JobDay']
        self.JobHour = kwargs['JobHour']
        self.LocalTime = kwargs['LocalTime']
        self.CurrentYear = kwargs['CurrentYear']
        self.CurrentMonth = kwargs['CurrentMonth']
        self.CurrentDay = kwargs['CurrentDay']
        self.CurrentHour = kwargs['CurrentHour']
        
        def __repr__(self):
            return f"{self.ClientID} {self.MaxBatchID}"
        


