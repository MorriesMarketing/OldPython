from I_Databases import *


class SqlServer(Database):
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
            database = Database(SqlQueryConnect, SqlQueryExcecute, Database.FETCHONE, Sql)
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
            database = Database(SqlQueryConnect, SqlQueryExcecute, Database.FETCHALL, Sql)
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
            database = Database(SqlQueryConnect, SqlQueryExcecute, Database.FETCHALL, Sql)
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
            database = Database(SqlQueryConnect, SqlQueryExcecute, Database.FETCHALL, Sql)
            return database.access_table()    


