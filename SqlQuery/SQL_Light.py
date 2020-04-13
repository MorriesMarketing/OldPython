import sqlite3

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
            