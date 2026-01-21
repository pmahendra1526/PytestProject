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


# Global fixtures (oracle and sql connections) with Teardown setup.
# oracle_connection & sql_connection used as parameter in tests functions sql_query & oracle_query 
@pytest.fixture(scope="module")
def oracle_connection():
    conn = oracledb.connect(user="SYSTEM",password="roshi",dsn="localhost:1521/XE")
    print(f"Connection Successfull to Oracle")
    
    yield conn

    conn.close()
    print(f"\nClosed Oracle connection.")

@pytest.fixture(scope="module")
def ssms_connection():
    conn = pyodbc.connect(connection_string)
    print(f"Connection Successfull to SQL Server")
    
    yield conn
    
    conn.close()
    print(f"\nClosed SQL Server connection.")

# Pytest with parameters to execute same test for 2 parameters
@pytest.fixture(params=["oracle", "sql_server"])
def db_connection(request):
    print("In db Connection fixture")
    db_type = request.param
    print(db_type)
    conn = None
    cursor = None
    try:
        if db_type=="oracle":
            conn=oracledb.connect(user="SYSTEM",password="roshi",dsn="localhost:1521/XE")
            cursor = conn.cursor()
            print(f"\nConnected to Oracle database.")
        elif db_type=="sql_server":
            conn=pyodbc.connect(connection_string)
            cursor = conn.cursor()
            print(f"\nConnected to SQL Server database.")
        else:
            raise ValueError(f"Unknown database type: {db_type}")
        
        yield conn,db_type

    finally:
        pass
        if conn:
            conn.close()
            print(f"\nClosed {db_type} connection.")

# @pytest.fixture
# def sql_query(request, db_connection):
#     """Fixture to execute a SQL query passed as a parameter."""
#     query = request.param # The SQL query string from the parametrize marker
#     print(f"\nExecuting query: {query}")
#     # Use your database connection to execute the query
#     # For example, using a mock connection here
#     cursor = db_connection.cursor()
#     cursor.execute(query)
#     results = cursor.fetchall()
#     yield results
#     # Teardown logic (e.g., closing cursor, rolling back session)
#     cursor.close()