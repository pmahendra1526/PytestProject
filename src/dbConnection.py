import pyodbc

def create_connection(driver_name,server_name, database_name):
    try:
        connection_string = (
            f"DRIVER={driver_name};"
            f"SERVER={server_name};"
            f"DATABASE={database_name};"
            f"Trusted_Connection=yes;"
            # r'UID=your_username;'
            # r'PWD=your_password;'
            )
        conn = pyodbc.connect(connection_string)
        print("Connection Successfull with Windows Authentication!")
        return conn
    except Exception as e:
        print(f"Connection failed: {e}")
        return None

# driver_name="{ODBC Driver 17 for SQL Server}"
# server_name="DESKTOP-59J1BAM\\SQLEXPRESS" # r"DESKTOP-59J1BAM\SQLEXPRESS"
# database_name="Mahendra"
# create_connection(driver_name,server_name, database_name)
