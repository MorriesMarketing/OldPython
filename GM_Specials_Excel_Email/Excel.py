import win32com.client
from pathlib import Path
#import openpyxl
import datetime
#import xlrd
import time

# Computer
class Excel:

    def __init__(self):
        self.folder = Path('C:/Users/gamer/Documents/')
        self.Walser_Ignite_Specials = self.folder / 'Walser Ignite Specials.xlsm'
        self.xl = win32com.client.DispatchEx('Excel.Application')
        self.refresh = self.refresh_sheet(sheet=f"{self.Walser_Ignite_Specials}")
        

    def refresh_sheet(self,sheet):
        wb = self.xl.Workbooks.Open(sheet)
        ws = wb.Worksheets(1)
        wb.RefreshAll()
        self.xl.CalculateUntilAsyncQueriesDone()

