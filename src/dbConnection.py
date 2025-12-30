import pyodbc
import oracledb
import getpass
import pandas as pd

class DBConnect:

    connection_string =(
        f"DRIVER={"{ODBC Driver 17 for SQL Server}"};"
        f"SERVER={"DESKTOP-59J1BAM\\SQLEXPRESS"};"
        f"DATABASE={"Mahendra"};"
        f"Trusted_Connection=yes;"
        )

    def oracle_connection(self):
        try:
            connection = oracledb.connect(user="SYSTEM",password="roshi",dsn="localhost:1521/XE")
            print(f"Connection Successfull to Oracle database")
            return connection
        except Exception as e:
            print(f"Connection failed: {e}")
            return None

    def ssms_connection(self,connection_string):
        try:
            # connection_string = (
            #     f"DRIVER={driver_name};"
            #     f"SERVER={server_name};"
            #     f"DATABASE={database_name};"
            #     f"Trusted_Connection=yes;"
            #     # r'UID=your_username;'
            #     # r'PWD=your_password;'
            #     )
            conn = pyodbc.connect(connection_string)
            print(f"Connection Successfull to server '{server_name}' and database '{database_name}'")
            return conn
        except Exception as e:
            print(f"Connection failed: {e}")
            return None

    def execute_Query(self,query,conn):
        try:
            df=pd.read_sql_query(query,conn)
            return df
        except Exception as e:
            print(f"Connection failed: {e}")
        

# driver_name="{ODBC Driver 17 for SQL Server}"
# server_name="DESKTOP-59J1BAM\\SQLEXPRESS" # r"DESKTOP-59J1BAM\SQLEXPRESS"
# database_name="Mahendra"
# c=DBConnect()
# c.ssms_connection(driver_name,server_name,database_name)
# c.oracle_connection()