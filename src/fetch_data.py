import pytest
import pyodbc
import pandas as pd
# ssms_connection ia a global fixture defined in conftest.py file.
@pytest.fixture(scope="module")
def sql_query(ssms_connection): 
    sql_df=pd.read_sql_query("SELECT * FROM EMP1",ssms_connection)
    # print(sql_df)
    return sql_df

# oracle_connection is a global fixture defined in conftest.py file.
@pytest.fixture(scope="module")
def oracle_query(oracle_connection):
    oracle_df=pd.read_sql_query("SELECT * FROM EMPLOYEES",oracle_connection)
    # print(oracle_df)
    return oracle_df