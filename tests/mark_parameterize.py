import pandas as pd
import pytest
import pyodbc
import oracledb
from src.dbConnection import DBConnect

connection_string =(
    f"DRIVER={"{ODBC Driver 17 for SQL Server}"};"
    f"SERVER={"DESKTOP-59J1BAM\\SQLEXPRESS"};"
    f"DATABASE={"Mahendra"};"
    f"Trusted_Connection=yes;"
    )

c=DBConnect()
sql_conn,sql_cursor=c.ssms_connection(connection_string)
oracle_conn,oracle_cursor=c.oracle_connection()

@pytest.mark.parametrize("sql_query, expected_results",\
                         [("SELECT COUNT(*) CNT FROM EMP1","SELECT COUNT(*) CNT FROM EMPLOYEES"), \
                          ("SELECT MIN(SALARY) CNT FROM EMP1","SELECT MIN(SALARY) CNT FROM EMPLOYEES"), \
                          ("SELECT MAX(SALARY) CNT FROM EMP1","SELECT MAX(SALARY) CNT FROM EMPLOYEES")])

def test_sceanario(sql_query,expected_results):
    sql_cursor.execute(sql_query)
    oracle_cursor.execute(expected_results)
    sql_query=sql_cursor.fetchall()
    expected_results=oracle_cursor.fetchall()
    print(sql_query,expected_results)
    print(sql_query[0][0],expected_results[0][0])
    print("length",len(sql_query))
    assert sql_query[0][0] == expected_results[0][0]

