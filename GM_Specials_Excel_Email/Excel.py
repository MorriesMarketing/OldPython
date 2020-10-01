#import sys
# insert at 1, 0 is the script path (or '' in REPL)
#sys.path.insert(1, 'C:/Users/gamer/source/repos/MMuhlenkort/PythonWalser/ClassLibrary')

import win32com.client
from pathlib import Path
import datetime
from O_Days import *
from O_Paths import *
from O_Files import *
import os
#import openpyxl
from O_MarketData import *

# Computer
path = Path()
class Excel():

    def __init__(self):
        
        self.Walser_Ignite_Specials = f'{path.desktop_path}/Walser Ignite Specials.xlsm'
        self.xl = win32com.client.DispatchEx('Excel.Application')
        self.refresh = self.refresh_sheet(sheet=f"{self.Walser_Ignite_Specials}")

    def refresh_sheet(self,sheet):
        print(f'Refreshing Excel Sheet:{sheet}')
        wb = self.xl.Workbooks.Open(sheet)
        ws = wb.Worksheets(1)
        wb.RefreshAll()
        print(f"Batch: {int(ws.Range('A18'))}")
        self.xl.CalculateUntilAsyncQueriesDone()
        print(f'Completed Refresh of Excel Sheet: {sheet}')
        print(f"Batch: {int(ws.Range('A18'))}")
        wb.Save()
        self.xl.DisplayAlerts = False
        self.xl.Quit()
    
    @staticmethod
    def split_filename_to_identify_date(filename):
        filename_strings = filename.split('_')
        date_strings = filename_strings[2].split('-')
        day_split = date_strings[2].split('.')
        date = {
            'Year': int(date_strings[0]),
            'Month': int(date_strings[1]),
            'Day': int(day_split[0])
            }
        return date

    def gather_files(self,Directory):
        list_of_valid_files = []
        for filename in os.listdir(Directory):
            today = Today()
            if 'csv#' in filename:
                filename_date = self.split_filename_to_identify_date(filename)
                file_date_valid = today.date_x_days_ago(Minus_Days=7,Year=filename_date['Year'],Month=filename_date['Month'],Day=filename_date['Day'])
                file = File()
                file.Directory = Directory
                file.FileName = filename
                if 'MarketData' in file.FileName and file_date_valid:
                    print(os.path.join(file.Directory, file.FileName))
                    valid_filenames.append(file)
                else:
                    print(filename)

        return list_of_valid_files

    def gather_market_data_files(self):
        list_of_valid_files = []
        folder_1 = self.gather_files(Directory=path.inventory_path_1)
        for f in folder_1:
            list_of_valid_files.append(f)
        folder_2 = self.gather_files(Directory=path.inventory_path_2)
        for f in folder_2:
            list_of_valid_files.append(f)
        folder_3 = self.gather_files(Directory=path.inventory_path_3)
        for f in folder_3:
            list_of_valid_files.append(f)
        folder_4 = self.gather_files(Directory=path.inventory_path_4)
        for f in folder_4:
            list_of_valid_files.append(f)

        return list_of_valid_files

    def create_list_of_vehicles(self):

        list_of_valid_files = self.gather_market_data_files()
        MarketData_Vehicles = []

        for f in list_of_valid_files:
            wb = openpyxl.load_workbook(f.File, data_only=True)
            columns = wb[f'{f.FileName}']
            row_end = len(columns['A'])
            prev_VIN = ''
            for row in columns[f'A1:U{row_end}']:
                values = []
                for cell in row:
                    values.append(cell.value)
                if values[7] != prev_VIN and values[7] != 'VIN':
                    market_data = MarketData()
                    market_data.MAKE = values[0]
                    market_data.YEAR = values[1]
                    market_data.MODEL = values[2]
                    market_data.BUILD = values[3]
                    market_data.TRIM = values[4]
                    market_data.STATUS = values[5]
                    market_data.MSRP = values[6]
                    market_data.VIN = values[7]
                    market_data.VON = values[8]
                    market_data.ALLOCATION_DATE = values[9]
                    market_data.TRANSIT_DATE = values[10]
                    market_data.GROUND_DATE = values[11]
                    market_data.SOLD_DATE = values[12]
                    market_data.LAST_STATUS_CHANGE = values[13]
                    market_data.OPTIONS = values[14]
                    market_data.EXT_COLOR = values[15]
                    market_data.INT_COLOR = values[16]
                    market_data.DAYS_IN_STOCK = values[17]
                    market_data.DEALER_TITLE = values[18]
                    market_data.DISTANCE = values[19]
                    market_data.BVS = values[20]

                    prev_VIN = market_data.VIN

                    MarketData_Vehicles.append(market_data)
        for m in MarketData_Vehicles:
            print(m)