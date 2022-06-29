import pyodbc

from app.settings import AppSettings


def get_connection_string() -> str:
    return f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={AppSettings.DB_HOST}/{AppSettings.DB_PORT}\
            ;DATABASE={AppSettings.DB_NAME};UID={AppSettings.DB_USER};PWD={AppSettings.DB_PASS}'


def get_db():
    connection_string = get_connection_string()
    connection = pyodbc.connect(connection_string)

    return connection.cursor()
