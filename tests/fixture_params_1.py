import pandas as pd
import pytest
import pyodbc
import oracledb

connection_string =(
    f"DRIVER={"{ODBC Driver 17 for SQL Server}"};"
    f"SERVER={"DESKTOP-59J1BAM\\SQLEXPRESS"};"
    f"DATABASE={"Mahendra"};"
    f"Trusted_Connection=yes;"
    )
print(connection_string)

# Parameterized fixture db_connection global defined in 'conftest.py' file.
def test_database_query(db_connection):
    conn,db_type = db_connection
    print(f"Connection Value: {conn}; Database: {db_type}")
    if db_type=='oracle':
         df=pd.read_sql_query("SELECT * FROM EMPLOYEES",conn)
    elif db_type=="sql_server":
         df=pd.read_sql_query("SELECT * FROM EMP1",conn)
    print(df)

def test_one():
    assert 1==1