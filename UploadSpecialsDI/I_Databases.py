from O_Days import *
import sqlite3
import pyodbc
# Database Constructor

class Database():
    #Used to access a SQL Database
    FETCHALL = 0
    FETCHMANY = 1
    FETCHONE = 2
    SQLSERVER = pyodbc
    SQLITE3 = sqlite3
# On Init place the database instructions to find and login to database
    def __init__(self,database_path, excecute_string, excecute_flag, sql_flag):
        self.database_path =  database_path  
        self.flag = excecute_flag
        self.excecute_string = excecute_string
        self.sql_flag = sql_flag
# Use to excecute the Query and declare how much of the data you want to access
    def access_table(self):
        print(f'\nAccessing Database: {self.database_path}')
        if self.sql_flag == Database.SQLSERVER:
            conn = pyodbc.connect(self.database_path)
        elif self.sql_flag == Database.SQLITE3:
            conn = sqlite3.connect(self.database_path, detect_types=sqlite3.PARSE_COLNAMES)
        cursor = conn.cursor()
        
        execute = cursor.execute(self.excecute_string)
        if self.flag == Database.FETCHALL:
            return [cursor.description, execute.fetchall()]
        elif self.flag == Database.FETCHMANY:
            return [cursor.description, execute.fetchmany()]
        elif self.flag == Database.FETCHONE:
            return [cursor.description, execute.fetchone()]
        else:
            return cursor

        conn.commit()
        conn.close()
    
    @staticmethod # Combine Headers & Columns to create objects from a Table or View
    def convert_table_to_dict(table):
        dict_values = []
        for value in table[1]:
            new_dict = {}
            for i in range(len(table[0])):
                new_dict[table[0][i][0]] = value[i]
            dict_values.append(new_dict)
        return dict_values

    @staticmethod # Create individual object
    def create_objects(data, class_name):
        objects = []
        for row in data:
            obj = class_name(**row)
            objects.append(obj)
        return objects
    
    @staticmethod # Create list of objects grouped by a column name
    def create_grouped_objects(data, class_name, column_name):
        objects = []
        previous_object = None
        for row in data:
            obj = class_name(**row)
            if previous_object == None:
                objects.append(obj)
            elif obj.__dict__[column_name] != previous_object.__dict__[column_name]:
                objects.append(obj)
            previous_object = obj
        return objects

class DigitalMarketingDatabase(Database):

    def create_vehicles_from_VehicleSpecialsNew():
        #step 1: creating a list of vehicles and grouping by stocknumber 
        data_table = SqlServer.PRD_OfferSpecialsUpload_ReadData()
        data = Database.convert_table_to_dict(data_table)
        vehicles = Database.create_grouped_objects(data, Vehicle, 'StockNumber')

        #Step 2 creating the list of offers
        data_table = SqlServer.PRD_OfferSpecialsUpload_ReadData()
        data = Database.convert_table_to_dict(data_table)
        offers = Database.create_objects(data, Offer)

        # combine offer objects into vehicle objects
        for v in vehicles:
            for o in offers:
                if v.VehicleID == o.VehicleID:
                    v.Offers.append(o)
        
        return vehicles

