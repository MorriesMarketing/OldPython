import pyodbc
import sqlite3
from  Days import *
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
        if self.sql_flag == Databases.SQLSERVER:
            conn = pyodbc.connect(self.database_path)
        elif self.sql_flag == Databases.SQLITE3:
            conn = sqlite3.connect(self.database_path, detect_types=sqlite3.PARSE_COLNAMES)
        cursor = conn.cursor()
        
        execute = cursor.execute(self.excecute_string)
        if self.flag == Databases.FETCHALL:
            return [cursor.description, execute.fetchall()]
        elif self.flag == Databases.FETCHMANY:
            return [cursor.description, execute.fetchmany()]
        elif self.flag == Databases.FETCHONE:
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
    
    @staticmethod # Create list of individual objects
    def create_unique_objects(data, class_name,column_name):
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

class SqlLight():

    def __init__(self):
        pass
    
    @staticmethod
    def VM_Websites_ReadData():
        Sql = Database.SQLITE3
        SqlQueryConnect = f"C:\PythonSqlite\Databases\Database1.db"
        SqlQueryExcecute = f"""
                        SELECT *               
                        FROM Websites
                        """
        
        while True:
            database = Database(SqlQueryConnect, SqlQueryExcecute, Databases.FETCHALL, Sql)
            return database.access_table()

class SqlServer():
    def __init__(self):
        pass
    
    @staticmethod
    def PRD_OfferSpecialsUpload_RefreshCheck():
        Sql = Database.SQLSERVER
        SqlQueryConnect = """
        Driver={SQL Server};
        Server=dealermarketing.database.windows.net;
        Database=PRD_DigitalMarketing;
        UID=ApplicationRead;
        PWD=TheW@lserW@y;
        """
        SqlQueryExcecute = """
        SELECT CONVERT(VARCHAR(10), CreatedDT, 111) [CreatedDate]
        FROM OfferSpecialsUpload
        """
        
        while True:
            database = Database(SqlQueryConnect, SqlQueryExcecute, Databases.FETCHONE, Sql)
            cursor = database.access_table()
            print(cursor)
            today = Today()
            sql_date = cursor[1][0]
            if today.today_date_format == sql_date:
                print('SUCCESS')
                print(f'today: {today.today_date_format} sql:{sql_date}')
                break
            else:
                print('FAILED')
                print(f'today: {today.today_date_format} sql:{sql_date}')
                print('Going to sleep for 60 sec.')
                sleeping = 0
                while sleeping <60:
                    sleep(1)
                    print('slept ' + str(sleeping) + '/60')
                    sleeping += 1

    @staticmethod
    def PRD_OfferSpecialsUpload_ReadData():
        Sql = Database.SQLSERVER
        SqlQueryConnect = """
            Driver={SQL Server};
            Server=dealermarketing.database.windows.net;
            Database=PRD_DigitalMarketing;
            UID=ApplicationRead;
            PWD=TheW@lserW@y;
            """
        SqlQueryExcecute = """
            select 
            CONVERT(VARCHAR(10), CreatedDT, 111) [CreatedDate], BatchID, 
            
            /* Dealer Info */
            State, DealerCode, 
            /* Vehicle Info */
            StockNumber, Title,  
            /* Payment Info */
            '$' + replace(convert(varchar,cast(floor(Payment) as money),1), '.00', '') as Payment, 
            '$' + replace(convert(varchar,cast(floor(BasePayment) as money),1), '.00', '') as BasePayment, 
            '$' + replace(convert(varchar,cast(floor(PaymentNoTax) as money),1), '.00', '') as PaymentNoTax, 
            LeaseSpecial, Lender, 
            /* Offer Info */
            format([LeaseMileage],'N0') [LeaseMi], 
            Term, 
            '$' + replace(convert(varchar,cast(floor(Downpayment) as money),1), '.00', '') as DownPayment, 
            '$' + replace(convert(varchar,cast(floor(DueAtSigning) as money),1), '.00', '') as DueAtSigning, 
            '$' + replace(convert(varchar,cast(floor(TotalRebate) as money),1), '.00', '') as TotalRebate, 
            '$' + replace(convert(varchar,cast(floor(MSRP) as money),1), '.00', '') as MSRP, 
            '$' + replace(convert(varchar,cast(floor(Invoice) as money),1), '.00', '') as Invoice, 
            '$' + replace(convert(varchar,cast(floor(DealerPrice) as money),1), '.00', '') as DealerPrice, 
            '$' + replace(convert(varchar,cast(floor(SellingPrice) as money),1), '.00', '') as SellingPrice, 
            Disclaimer, 
            UploadOrder, VehicleRank, ModelRank, ModelNoRank, 
            /* Vehicle Info 2*/
            VIN, StockType, Year, BrandName [Brand], Model, ModelNumber, Trim, OptionCode, Mileage, 
            /* Offers */
            LeaseOfferMileage, 
            '$' + replace(convert(varchar,cast(floor(AmountFinanced) as money),1), '.00', '') as AmountFinanced, 
            '$' + replace(convert(varchar,cast(floor(MaxAdvance) as money),1), '.00', '') as MaxAdvance, 
            '$' + replace(convert(varchar,cast(floor(PaidReserve) as money),1), '.00', '') as PaidReserve, 
            /* Fees */
            '$' + replace(convert(varchar,cast(floor(RegistrationFee) as money),1), '.00', '') as RegistrationFee, 
            '$' + replace(convert(varchar,cast(floor(AquisitionFee) as money),1), '.00', '') as AquisitionFee, 
            '$' + replace(convert(varchar,cast(floor(InceptionFees) as money),1), '.00', '') as InceptionFees, 
            '$' + replace(convert(varchar,cast(floor(OtherFees) as money),1), '.00', '') as OtherFees, 
            /* Rates */
            APR, BuyRate, SellRate,
            '$' + replace(convert(varchar,cast(floor(SalesTax) as money),1), '.00', '') as SalesTax, 
            SalesTaxRate, 
            '$' + replace(convert(varchar,cast(floor(SecurityDeposit) as money),1), '.00', '') as SecurityDeposit, 
            cast( cast(ResidualPercent AS DECIMAL(18,0)) as varchar(100)) + ' %' as [ResidualPercent], 
            '$' + replace(convert(varchar,cast(floor(ResidualDollar) as money),1), '.00', '') as ResidualDollar,  
            ProgramCode, Description, 
            LeaseOffer, 
            StartDate, EndDate, EndDay, EndMonth, EndYear, 
            DeathDate, DeathDay, DeathMonth, DeathYear, 
            
            IsCaptive, IsSpecial, 
            HasOEMException [OEMException], PriceChange, MarkupRate, 
            VehicleID, MarketScanID, DealerID, BrandID, OfferID, OfferTypeID, PriceOptionID

            from OfferSpecialsUpload
            order by VehicleRank desc, UploadOrder asc
            """
        while True:
            database = Database(SqlQueryConnect, SqlQueryExcecute, Databases.FETCHALL, Sql)
            return database.access_table()
    
    @staticmethod
    def PRD_OfferSpecialsBlog_ReadData():
        Sql = Database.SQLSERVER
        SqlQueryConnect = """
            Driver={SQL Server};
            Server=dealermarketing.database.windows.net;
            Database=PRD_DigitalMarketing;
            UID=ApplicationRead;
            PWD=TheW@lserW@y;
            """
        SqlQueryExcecute = """
            select 
            CONVERT(VARCHAR(10), CreatedDT, 111) [CreatedDate], BatchID, 
            
            /* Dealer Info */
            State, DealerCode, 
            /* Vehicle Info */
            StockNumber, Title,  
            /* Payment Info */
            '$' + replace(convert(varchar,cast(floor(Payment) as money),1), '.00', '') as Payment, 
            '$' + replace(convert(varchar,cast(floor(BasePayment) as money),1), '.00', '') as BasePayment, 
            '$' + replace(convert(varchar,cast(floor(PaymentNoTax) as money),1), '.00', '') as PaymentNoTax, 
            LeaseSpecial, Lender, 
            /* Offer Info */
            format([LeaseMileage],'N0') [LeaseMi], 
            Term, 
            '$' + replace(convert(varchar,cast(floor(Downpayment) as money),1), '.00', '') as DownPayment, 
            '$' + replace(convert(varchar,cast(floor(DueAtSigning) as money),1), '.00', '') as DueAtSigning, 
            '$' + replace(convert(varchar,cast(floor(TotalRebate) as money),1), '.00', '') as TotalRebate, 
            '$' + replace(convert(varchar,cast(floor(MSRP) as money),1), '.00', '') as MSRP, 
            '$' + replace(convert(varchar,cast(floor(Invoice) as money),1), '.00', '') as Invoice, 
            '$' + replace(convert(varchar,cast(floor(DealerPrice) as money),1), '.00', '') as DealerPrice, 
            '$' + replace(convert(varchar,cast(floor(SellingPrice) as money),1), '.00', '') as SellingPrice, 
            Disclaimer, 
            UploadOrder, VehicleRank, ModelRank, ModelNoRank, 
            /* Vehicle Info 2*/
            VIN, StockType, Year, BrandName [Brand], Model, ModelNumber, Trim, OptionCode, Mileage, 
            /* Offers */
            LeaseOfferMileage, 
            '$' + replace(convert(varchar,cast(floor(AmountFinanced) as money),1), '.00', '') as AmountFinanced, 
            '$' + replace(convert(varchar,cast(floor(MaxAdvance) as money),1), '.00', '') as MaxAdvance, 
            '$' + replace(convert(varchar,cast(floor(PaidReserve) as money),1), '.00', '') as PaidReserve, 
            /* Fees */
            '$' + replace(convert(varchar,cast(floor(RegistrationFee) as money),1), '.00', '') as RegistrationFee, 
            '$' + replace(convert(varchar,cast(floor(AquisitionFee) as money),1), '.00', '') as AquisitionFee, 
            '$' + replace(convert(varchar,cast(floor(InceptionFees) as money),1), '.00', '') as InceptionFees, 
            '$' + replace(convert(varchar,cast(floor(OtherFees) as money),1), '.00', '') as OtherFees, 
            /* Rates */
            APR, BuyRate, SellRate,
            '$' + replace(convert(varchar,cast(floor(SalesTax) as money),1), '.00', '') as SalesTax, 
            SalesTaxRate, 
            '$' + replace(convert(varchar,cast(floor(SecurityDeposit) as money),1), '.00', '') as SecurityDeposit, 
            cast( cast(ResidualPercent AS DECIMAL(18,0)) as varchar(100)) + ' %' as [ResidualPercent], 
            '$' + replace(convert(varchar,cast(floor(ResidualDollar) as money),1), '.00', '') as ResidualDollar,  
            ProgramCode, Description, 
            LeaseOffer, 
            StartDate, EndDate, EndDay, EndMonth, EndYear, 
            DeathDate, DeathDay, DeathMonth, DeathYear, 
            
            IsCaptive, IsSpecial, 
            HasOEMException [OEMException], PriceChange, MarkupRate, 
            VehicleID, MarketScanID, DealerID, BrandID, OfferID, OfferTypeID, PriceOptionID

            from OfferSpecialsUpload
            order by Brand asc, Model asc, Year desc, VehicleRank asc, UploadOrder asc
            """
        while True:
            database = Database(SqlQueryConnect, SqlQueryExcecute, Databases.FETCHALL, Sql)
            return database.access_table()

    @staticmethod
    def PRD_ExternalVehicles_AgedUsed_ReadData():
        Sql = Database.SQLSERVER
        SqlQueryConnect = """
            Driver={SQL Server};
            Server=dealermarketing.database.windows.net;
            Database=PRD_DigitalMarketing;
            UID=ApplicationRead;
            PWD=TheW@lserW@y;
            """
        SqlQueryExcecute = """
            select ClientID, DealerCode, Type, StockNumber, VIN, Age

            from ExternalVehicle

            where ClientID = 1 and Age > 59 and Type = 'Used'
            """
        while True:
            database = Database(SqlQueryConnect, SqlQueryExcecute, Databases.FETCHALL, Sql)
            return database.access_table()        