import pyodbc

def get_db_connection():
    connection_string = (
        "DRIVER={SQL Server};"
        "SERVER=your_server;"
        "DATABASE=your_database;"
        "UID=your_user;"
        "PWD=your_password"
    )
    connection = pyodbc.connect(connection_string)
    return connection