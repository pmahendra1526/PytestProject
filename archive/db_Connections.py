# import pandas as pd
# import pytest
# import pyodbc
# import oracledb

# connection_string =(
#     f"DRIVER={"{ODBC Driver 17 for SQL Server}"};"
#     f"SERVER={"DESKTOP-59J1BAM\\SQLEXPRESS"};"
#     f"DATABASE={"Mahendra"};"
#     f"Trusted_Connection=yes;"
#     )

# @pytest.fixture(scope="module")
# def oracle_connection():
#     conn = oracledb.connect(user="SYSTEM",password="roshi",dsn="localhost:1521/XE")
#     print(f"Connection Successfull to Oracle")
    
#     yield conn

#     conn.close()
#     print(f"\nClosed Oracle connection.")

# @pytest.fixture(scope="module")
# def sql_connection():
#     conn = pyodbc.connect(connection_string)
#     print(f"Connection Successfull to SQL Server")
    
#     yield conn
    
#     conn.close()
#     print(f"\nClosed SQL Server connection.")
