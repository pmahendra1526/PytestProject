import pandas as pd
import pytest
# from src.db_Connections import oracle_connection,sql_connection

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

# Calling fixure sql_query & oracle_query which returns dataframe object
# Tests Eexecution - Columns Count
def test_dfs_columns_count(sql_query,oracle_query):
    assert len(sql_query.columns)==len(oracle_query.columns),"Number of columns not matching"

# Tests Eexecution - Records Count
def test_dfs_records_count(sql_query,oracle_query):
    assert len(sql_query)==len(oracle_query), "Records count not matching"

# Tests Eexecution - quals returns True or False..
def test_dfs_equals(sql_query,oracle_query):
    assert sql_query.equals(oracle_query),"Dataframes are not equal"
    
# Tests Eexecution - Compare Dataframes. compare will work only if both index and columns are identical
def test_dfs_compare(sql_query,oracle_query):
    assert sql_query.compare(oracle_query),"Dataframes are not equal"

# Global ixtures with params=["oracle", "sql_server"] to execute for both oracle and sql server.
def test_database_query(db_connection):
    conn,db_type = db_connection
    print(conn)
    print(db_type)
    if db_type=='oracle':
         df=pd.read_sql_query("SELECT * FROM EMPLOYEES",conn)
    elif db_type=="sql_server":
         df=pd.read_sql_query("SELECT * FROM EMP1",conn)
    print(df)

