# from src.dbConnection import DBConnect
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

# driver_name="{ODBC Driver 17 for SQL Server}"
# server_name="DESKTOP-59J1BAM\\SQLEXPRESS" # r"DESKTOP-59J1BAM\SQLEXPRESS"
# database_name="Mahendra" pyodbc.connect(connection_string)

@pytest.fixture(params=["oracle", "sql_server"])
def db_connection(request):
    db_type = request.param
    print(db_type)
    conn = None
    cursor = None
    try:
        if db_type=="oracle":
            conn=oracledb.connect(user="SYSTEM",password="roshi",dsn="localhost:1521/XE")
            # cursor = conn.cursor()
            print(f"\nConnected to Oracle database.")
        elif db_type=="sql_server":
            conn=pyodbc.connect(connection_string)
            # cursor = conn.cursor()
            print(f"\nConnected to SQL Server database.")
        else:
            raise ValueError(f"Unknown database type: {db_type}")
        
        yield conn,db_type

    finally:
        # Teardown: this code runs after the test finishes
        # if cursor:
        #     cursor.close()
        #     print(f"\nClosed {db_type} cursor.")
        if conn:
            conn.close()
            print(f"\nClosed {db_type} connection.")

def test_database_query(db_connection):
    conn,db_type = db_connection
    print(conn)
    print("In Cursor")
    print(db_type)
    if db_type=='oracle':
         df=pd.read_sql_query("SELECT * FROM EMPLOYEES",conn)
    elif db_type=="sql_server":
         df=pd.read_sql_query("SELECT * FROM EMP1",conn)
    print(df)

    # else:
    #      cursor.execute("SELECT * FROM EMP1")

    # result = cursor.fetchone()
    # assert result is not None
    # print(f"Query result: {result}")

#     result = cursor.fetchone()
#     assert result is not None
#     print(f"Query result: {result}")


#     sql_conn=c.ssms_connection(driver_name,server_name,database_name)
#     oracle_conn=c.oracle_connection()
#     sql_query="SELECT * FROM DBO.EMP1"
#     oracle_query="SELECT * FROM EMPLOYEES"
#     sql_df=c.execute_Query(sql_query,sql_conn)
#     oracle_df=c.execute_Query(oracle_query,oracle_conn)
#     yield
#     sql_conn.close()
#     print("SQL Connection Closed")
#     oracle_conn.close()
#     print("Oracle Connection Closed")

# def test_dataframe_equals(fetch_db_connection):
#     assert sql_df.equals(oracle_df),"Data not matching"



# print(sql_conn,oracle_conn)
# sql_query="SELECT * FROM DBO.EMP1"
# oracle_query="SELECT * FROM EMPLOYEES"

# sql_df=c.execute_Query(sql_query,sql_conn)
# oracle_df=c.execute_Query(oracle_query,oracle_conn)
# print(type(sql_df))

# print(sql_df)
# print(oracle_df)

# print(sql_df.equals(oracle_df))
# diff=sql_df.compare(oracle_df,keep_shape=True)
# print(diff)
# # print(sql_df.merge(oracle_df,on=['EMPID'], how='inner', indicator=True))


