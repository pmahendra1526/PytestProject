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

@pytest.fixture
def sql_query(request,sql_connection):
    query=request.param
    print(f"\nExecuting query: {query}")
    sql_df=pd.read_sql_query(query,sql_connection)
    print(sql_df)
    yield sql_df

@pytest.fixture(scope="module")
def sql_connection():
    conn = pyodbc.connect(connection_string)
    print(f"Connection Successfull to SQL Server")
    
    yield conn
    
    conn.close()
    print(f"\nClosed SQL Server connection.")



# Define the test cases with (query, expected_results)
TEST_CASES = [
    # ("SELECT EMPID,EMPNAME FROM EMP1", [(101, 'John Doe'), (102, 'Jane Smith')]),
    # ("SELECT EMPNAME FROM EMP1 WHERE salary > 75000.00", [('Jane Smith',)]),
    ("SELECT COUNT(*) CNT FROM EMP", [(4,)])
]

@pytest.mark.parametrize("sql_query, expected_results", TEST_CASES, indirect=["sql_query"])
def test_sql_queries(sql_query, expected_results):
    print("Starts Execution")
    print(sql_query)
    print(expected_results)
    """Test that the SQL query executed by the fixture returns the expected results."""
    assert sql_query == expected_results