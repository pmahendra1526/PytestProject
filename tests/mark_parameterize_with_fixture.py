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

# oracle_config={user="SYSTEM",password="roshi",dsn="localhost:1521/XE"}

@pytest.fixture
def oracle_connection():
    try:
        connection = oracledb.connect(user="SYSTEM",password="roshi",dsn="localhost:1521/XE")
        print(f"Connection Successfull to Oracle database")
        cursor = connection.cursor()
        yield cursor
    except Exception as e:
        print(f"Connection failed: {e}")
        return None
    # finally:
    #     cursor.close()
    #     connection.close()
    
@pytest.fixture
def ssms_connection():
    try:
        connection_string =(
            f"DRIVER={"{ODBC Driver 17 for SQL Server}"};"
            f"SERVER={"DESKTOP-59J1BAM\\SQLEXPRESS"};"
            f"DATABASE={"Mahendra"};"
            f"Trusted_Connection=yes;"
            )
        conn = pyodbc.connect(connection_string)
        print(f"Connection Successfull to SQL Server'")
        cursor = conn.cursor()
        return cursor
    except Exception as e:
        print(f"Connection failed: {e}")
        return None
    # finally:
    #     cursor.close()
    #     conn.close()

@pytest.mark.parametrize("sql_query, expected_results",\
                         [("SELECT COUNT(*) CNT FROM EMP1","SELECT COUNT(*) CNT FROM EMPLOYEES"), \
                          ("SELECT MIN(SALARY) CNT FROM EMP1","SELECT MIN(SALARY) CNT FROM EMPLOYEES"), \
                          ("SELECT MAX(SALARY) CNT FROM EMP1","SELECT MAX(SALARY) CNT FROM EMPLOYEES")])

def test_sceanario(ssms_connection,oracle_connection,sql_query,expected_results):
    print(ssms_connection,oracle_connection)
    sql_query=ssms_connection.execute(sql_query).fetchone()
    expected_results=oracle_connection.execute(expected_results).fetchone()
    print(sql_query[0],expected_results[0])
    assert sql_query[0] == expected_results[0]

# def test_sceanario(ssms_connection,oracle_connection,sql_query,expected_results):
#     print(ssms_connection,oracle_connection)
#     sql_query=ssms_connection.execute(sql_query).fetchone()
#     expected_results=oracle_connection.execute(expected_results).fetchone()
#     print(sql_query[0],expected_results[0])
#     assert sql_query[0] == expected_results[0]

# Dynamic code to pass table name
# def fetch_table_data(connection, table_name):
#     """Helper function to fetch all data from a table as a list of dictionaries."""
#     print("In fetch_table_data")
#     print(connection,table_name)
#     # with connection.cursor() as cursor:
#     connection.execute(f"SELECT * FROM {table_name}") # Order by primary key for consistent comparison
#     columns = [desc[0] for desc in connection.description]
#     data = [dict(zip(columns, row)) for row in connection.fetchall()]
#     print(data)
#     return data
# def test_compare_table_contents(ssms_connection, oracle_connection):
#     """Test to compare the contents of a single table in two databases."""
#     # table_name = 'your_table_name' # Replace with your actual table name
#     print("In test_compare_table_contents")
#     print(ssms_connection,oracle_connection)
#     data1 = fetch_table_data(ssms_connection, "EMP1")
#     print("before data1")
#     data2 = fetch_table_data(oracle_connection, "EMPLOYEES")
#     print("after data1")
#     # Use pytest's powerful assertion introspection
#     assert data1 == data2, f"Data in table does not match between databases"