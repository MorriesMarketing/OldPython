from I_Databases import *


class SqlServer(Database):
    def __init__(self):
        pass
    
    #This method is used for calling all of the Todays BatchID's. If no BatchID is found to match todays date no value will return
    @staticmethod
    def PRD_Batch_RefreshCheck():
        Sql = Database.SQLSERVER
        SqlQueryConnect = """
        Driver={SQL Server};
        Server=dealermarketing.database.windows.net;
        Database=PRD_DigitalMarketing;
        UID=ApplicationRead;
        PWD=TheW@lserW@y;
        """
        SqlQueryExcecute = """
        SELECT 
	        ClientID, 
	        MAX(BatchID) as MaxBatchID,
	        ExportJobEndDT, 
	        DATEPART ( Year , ExportJobEndDT ) as JobYear,
	        DATEPART ( Month , ExportJobEndDT ) as JobMonth,
	        DATEPART ( Day , ExportJobEndDT ) as JobDay,
	        DATEPART ( hour , ExportJobEndDT ) as JobHour,
	        Dateadd(hh, Datediff(hh, Getutcdate(), Getdate())-5, CURRENT_TIMESTAMP) AS LocalTime,
	        DATEPART ( Year , Dateadd(hh, Datediff(hh, Getutcdate(), Getdate())-5, CURRENT_TIMESTAMP) ) as CurrentYear,
	        DATEPART ( Month , Dateadd(hh, Datediff(hh, Getutcdate(), Getdate())-5, CURRENT_TIMESTAMP) ) as CurrentMonth,
	        DATEPART ( Day , Dateadd(hh, Datediff(hh, Getutcdate(), Getdate())-5, CURRENT_TIMESTAMP) ) as CurrentDay,
	        DATEPART ( hour , Dateadd(hh, Datediff(hh, Getutcdate(), Getdate())-5, CURRENT_TIMESTAMP) ) as CurrentHour

        FROM 
	        Batch B1
        WHERE 
	        ExportJobEndDT IS NOT NULL
	        AND BatchID = (
	        SELECT 
		        MAX(BatchID) 
	        FROM 
		        Batch B2 
	        WHERE
                ClientID != 5
		        AND B2.ClientID = B1.ClientID 
		        AND ExportJobEndDT IS NOT NULL
		        AND CONVERT(Date, ExportJobEndDT) = CONVERT(Date, Dateadd(hh, Datediff(hh, Getutcdate(), Getdate()-.2), CURRENT_TIMESTAMP))
		        )
        GROUP BY 
	        ClientID, 
	        ExportJobEndDT
        ORDER BY 
	        ClientID
        """
        
        while True:
            database = Database(SqlQueryConnect, SqlQueryExcecute, Database.FETCHALL, Sql)
            return database.access_table()
            
    #Calls for the list of vehicles to be prepared for the Vehicle object list
    @staticmethod
    def PRD_PythonOffers_ReadData():
        Sql = Database.SQLSERVER
        SqlQueryConnect = """
            Driver={SQL Server};
            Server=dealermarketing.database.windows.net;
            Database=PRD_DigitalMarketing;
            UID=ApplicationRead;
            PWD=TheW@lserW@y;
            """
        SqlQueryExcecute = """
            SELECT 
                * 
            FROM 
                PythonOffers
            WHERE
                ClientID != 5
            ORDER BY 
                ClientID,
	            DealerID,
	            VehicleID,
	
	            (CASE OfferTypeID 
		            WHEN 3 THEN 1 
		            WHEN 2 THEN 2 
		            WHEN 1 THEN 3 
		            WHEN 4 THEN 4 
		            WHEN 5 THEN 5 
		            WHEN 6 THEN 6 
		            WHEN 7 THEN 7 
		            WHEN 8 THEN 8

		            ELSE 100 END)
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

    # This is used to control the order in which the vehicles are used.
    # This method organizes the vehicles by Client and then Ranks by lowest to highest payment based on OfferTypeID 3 (10% MSRP)
    # Is used in the Dealer Inspire OfferUploads process
    def PRD_VehicleOffers_ClientRank():
        Sql = Database.SQLSERVER
        SqlQueryConnect = """
            Driver={SQL Server};
            Server=dealermarketing.database.windows.net;
            Database=PRD_DigitalMarketing;
            UID=ApplicationRead;
            PWD=TheW@lserW@y;
            """
        SqlQueryExcecute = """
            SELECT 
                ClientID, 
                DealerID, 
                VehicleID,
				Year,
                Model, 
                BasePayment,
                Rank() OVER (PARTITION BY DealerID ORDER BY BasePayment) DealerRank,
                Rank() OVER (PARTITION BY ClientID ORDER BY BasePayment) ClientRank
            FROM 
                VehicleOffers
            WHERE 
                ModelRank = 1
	            AND OfferRank = 1
	            AND OfferTypeID = 3
                AND ClientID != 5 
            GROUP BY 
                ClientID, 
                DealerID, 
                VehicleID,
				Year,
                Model, 
                BasePayment
            ORDER BY 
                ClientID, 
                ClientRank
            """
        while True:
            database = Database(SqlQueryConnect, SqlQueryExcecute, Database.FETCHALL, Sql)
            return database.access_table()

    # This is used to control the order in which the vehicles are used.
    # This method organizes the vehicles by Client then Dealer and then Ranks by lowest to highest payment based on OfferTypeID 3 (10% MSRP)
    # This would be used for creating dealer specific specials pages
    def PRD_VehicleOffers_DealerRank():
        Sql = Database.SQLSERVER
        SqlQueryConnect = """
            Driver={SQL Server};
            Server=dealermarketing.database.windows.net;
            Database=PRD_DigitalMarketing;
            UID=ApplicationRead;
            PWD=TheW@lserW@y;
            """
        SqlQueryExcecute = """
            SELECT 
                ClientID, 
                DealerID, 
                VehicleID,
                Year, 
                Model, 
                BasePayment, 
                Rank() OVER (PARTITION BY DealerID ORDER BY BasePayment) DealerRank,
                Rank() OVER (PARTITION BY ClientID ORDER BY BasePayment) ClientRank
            FROM 
                VehicleOffers
            WHERE 
                ModelRank = 1
	            AND OfferRank = 1
	            AND OfferTypeID = 3
                AND ClientID != 5
            GROUP BY 
                ClientID, 
                DealerID, 
                VehicleID, 
                Year, 
                Model, 
                BasePayment
            ORDER BY 
                ClientID, 
                DealerID, 
                DealerRank
            """
        while True:
            database = Database(SqlQueryConnect, SqlQueryExcecute, Database.FETCHALL, Sql)
            return database.access_table()
    
    # This is used to control the order in which the vehicles are used.
    # This method organizes the vehicles by Client then Year then Model and then Ranks by lowest to highest payment based on OfferTypeID 3 (10% MSRP)
    # This would be used for creating groupings for blogs where similar models are displayed on the same page
    def PRD_VehicleOffers_Year_Model_ClientRank():
        Sql = Database.SQLSERVER
        SqlQueryConnect = """
            Driver={SQL Server};
            Server=dealermarketing.database.windows.net;
            Database=PRD_DigitalMarketing;
            UID=ApplicationRead;
            PWD=TheW@lserW@y;
            """
        SqlQueryExcecute = """
            SELECT 
                ClientID, 
                DealerID, 
                VehicleID,
				Year,
                Model, 
                BasePayment, 
                Rank() OVER (PARTITION BY DealerID ORDER BY BasePayment) DealerRank,
                Rank() OVER (PARTITION BY ClientID ORDER BY BasePayment) ClientRank
            FROM 
                VehicleOffers
            WHERE 
                ModelRank = 1
	            AND OfferRank = 1
	            AND OfferTypeID = 3
                AND ClientID != 5
            GROUP BY 
                ClientID, 
                DealerID,
				Year,
                Model, 
                VehicleID, 
                BasePayment
            ORDER BY 
                ClientID, 
                Year,
				Model,
                ClientRank
            """
        while True:
            database = Database(SqlQueryConnect, SqlQueryExcecute, Database.FETCHALL, Sql)
            return database.access_table()

    # This method is used to see if a photo is available for a VehicleID. 
    # Seperate process is used to identify this occurence and check dealers website to obtain photo.
    def PRD_Vehicles_Photos():
        Sql = Database.SQLSERVER
        SqlQueryConnect = """
            Driver={SQL Server};
            Server=dealermarketing.database.windows.net;
            Database=PRD_DigitalMarketing;
            UID=ApplicationRead;
            PWD=TheW@lserW@y;
            """
        SqlQueryExcecute = """
            SELECT 
                ClientID,
	            DealerID,
	            VehicleID,
	            PhotoURL          
            FROM 
                ClientVehicles
            WHERE
                ClientID != 5

            """
        while True:
            database = Database(SqlQueryConnect, SqlQueryExcecute, Database.FETCHALL, Sql)
            return database.access_table()

    @staticmethod
    def PRD_Client_ReadData():
        Sql = Database.SQLSERVER
        SqlQueryConnect = """
            Driver={SQL Server};
            Server=dealermarketing.database.windows.net;
            Database=PRD_DigitalMarketing;
            UID=ApplicationRead;
            PWD=TheW@lserW@y;
            """
        SqlQueryExcecute = """
            SELECT 
                * 
            FROM 
                Client
            WHERE 
                ClientID != 5
            """
        while True:
            database = Database(SqlQueryConnect, SqlQueryExcecute, Database.FETCHALL, Sql)
            return database.access_table()