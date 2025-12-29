import pytest
import pandas as pd
from src.dbConnection import create_connection

driver_name="{ODBC Driver 17 for SQL Server}"
server_name="DESKTOP-59J1BAM\\SQLEXPRESS" # r"DESKTOP-59J1BAM\SQLEXPRESS"
database_name="Mahendra"
conn=create_connection(driver_name,server_name, database_name)

sql_query = "SELECT * FROM EMP"
df=pd.read_sql_query(sql_query,conn)
print(df)
df1=pd.read_sql_query("SELECT * FROM EMPLOYEES",conn)
print(df1)