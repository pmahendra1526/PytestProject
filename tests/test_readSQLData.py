import pytest
from src.dbConnection import create_connection


driver_name="{ODBC Driver 17 for SQL Server}"
server_name="DESKTOP-59J1BAM\\SQLEXPRESS" # r"DESKTOP-59J1BAM\SQLEXPRESS"
database_name="Mahendra"
create_connection(driver_name,server_name, database_name)