from I_Databases import *

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
            database = Database(SqlQueryConnect, SqlQueryExcecute, Database.FETCHALL, Sql)
            return database.access_table()
     
    @staticmethod
    def VM_OfferTypes_ReadData():
        Sql = Database.SQLITE3
        SqlQueryConnect = f"C:\PythonSqlite\Databases\Database1.db"
        SqlQueryExcecute = f"""
                        SELECT *               
                        FROM OfferTypes
                        """
        
        while True:
            database = Database(SqlQueryConnect, SqlQueryExcecute, Database.FETCHALL, Sql)
            return database.access_table()   
        
    @staticmethod
    def DeskTop_Websites_ReadData():
        Sql = Database.SQLITE3
        SqlQueryConnect = f"F:\SQLiteStudio-3.2.1\SQLiteStudio\Database1.db"
        SqlQueryExcecute = f"""
                        SELECT *               
                        FROM Websites
                        """
        
        while True:
            database = Database(SqlQueryConnect, SqlQueryExcecute, Database.FETCHALL, Sql)
            return database.access_table()

    @staticmethod
    def DeskTop_VehiclePhotos_ReadData():
        Sql = Database.SQLITE3
        SqlQueryConnect = f"F:\SQLiteStudio-3.2.1\SQLiteStudio\Database1.db"
        SqlQueryExcecute = f"""
                        SELECT *               
                        FROM VehiclePhotos
                        """
        
        while True:
            database = Database(SqlQueryConnect, SqlQueryExcecute, Database.FETCHALL, Sql)
            return database.access_table()

    @staticmethod
    def DeskTop_VehiclePhotos_Write(ClientID,DealerID,Domain,VIN,url,image):
        Sql = Database.SQLITE3
        conn = Sql.connect(f"F:\SQLiteStudio-3.2.1\SQLiteStudio\Database1.db")
        database_look = conn.execute(f"""
                SELECT 
                MAX(VehiclePhotoID)
                FROM VehiclePhotos
                    
                """)
        count = database_look.fetchone()
        #count_fix = count[0].replace('[','')
        #count_fix = count_fix.replace(']','')
        #count_fix = count_fix.replace(')','')
        #count_fix = count_fix.replace('(','')
        #count_fix = count_fix.replace(',','')
        #
        print(f'max_database: {count}')
        #print(f'max_database: {count[0]}')
        #print(f'max_database: {count_fix}')

        max_count = count[0] + 1
        conn.close()

        Sql = Database.SQLITE3
        conn = Sql.connect(f"F:\SQLiteStudio-3.2.1\SQLiteStudio\Database1.db")
        conn.cursor()
        conn.execute(f"""
                    INSERT INTO VehiclePhotos 
                    VALUES ('{max_count}','{ClientID}','{DealerID}','{Domain}','{VIN}', '{url}' , '{image}')
                    """)
        conn.commit()
        conn.close()

