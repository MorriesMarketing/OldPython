class Page():
    def __init__(self):
        self.Domain = None
        self.VdpUrl = None
        self.VdpImage = None
        self.VIN = None

    def __repr__(self):
        return f"{self.Domain}\t{self.VIN}\n{self.VdpImage}\n "