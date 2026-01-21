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


# BaseClass is super class or parent class.
@pytest.mark.usefixtures("db_connection")
class BaseClass:
    print("In Base Classs")
    a=10

class TestClass(BaseClass):
    # Parameterized fixture db_connection global defined in 'conftest.py' file.
    def test_database_query(self):
        print("In Test Mothod")
        # print(self.db_connection)
        # conn,db_type = self.BaseClass
        print(f"Connection Value: {conn}; Database: {db_type}")
        if db_type=='oracle':
            df=pd.read_sql_query("SELECT * FROM EMPLOYEES",conn)
        elif db_type=="sql_server":
            df=pd.read_sql_query("SELECT * FROM EMP1",conn)
        print(df)

# def test_one():
#     assert 1==1