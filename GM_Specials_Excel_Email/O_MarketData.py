

class MarketData():
    def __init__(self, **kwargs):
        self.MAKE = None#A - 0
        self.YEAR = None#B - 1
        self.MODEL = None#C - 2
        self.BUILD = None#D - 3
        self.TRIM = None#E - 4
        self.STATUS = None#F - 5
        self.MSRP = None#G - 6
        self.VIN = None#H - 7
        self.VON = None#I - 8
        self.ALLOCATION_DATE = None#J - 9
        self.TRANSIT_DATE = None#K - 10
        self.GROUND_DATE = None#L - 11
        self.SOLD_DATE = None#M - 12
        self.LAST_STATUS_CHANGE = None#N - 13
        self.OPTIONS = None#O - 14
        self.EXT_COLOR = None#P - 15
        self.INT_COLOR = None#Q - 16
        self.DAYS_IN_STOCK = None#R - 17
        self.DEALER_TITLE = None#S - 18
        self.DISTANCE = None#T - 19
        self.BVS = None#U - 20

    def __repr__(self):
        return f"{self.YEAR} {self.MAKE} {self.MODEL} {self.VIN} {self.BUILD}"
