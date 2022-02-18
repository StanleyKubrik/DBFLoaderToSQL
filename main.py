import keyring
import pandas as pd
import pyodbc
from simpledbf import Dbf5


def create_csv_from_dbf(dbf_file: str):
    try:
        dbf = Dbf5(dbf_file + '.dbf', codec='Windows-1251')
        dbf.to_csv(dbf_file + '.csv')
        print('CSV-file from dbf created!')
    except FileNotFoundError:
        print('DBF-file not found in current directory!')


def connect_to_sql() -> pyodbc.connect:
    driver = '{ODBC Driver 17 for SQL Server}'
    server = 'powerbivm1.dpst.kola'
    database = 'petrykivka_test'
    username = 'sukhonosovn'
    password = keyring.get_password('SQL', username)
    print('Connection to SQL DB...')
    try:
        conn = pyodbc.connect('DRIVER=' + driver
                              + ';SERVER=' + server
                              + ';DATABASE=' + database
                              + ';UID=' + username
                              + ';PWD=' + password)
    except pyodbc.OperationalError as e:
        print("Can't connection to DB: " + str(e))
    else:
        return conn


if __name__ == '__main__':
    dbf_name = input('Enter full name of the DBF file (without extension, not case sensitive): ')
    create_csv_from_dbf(dbf_name)
    # df = pd.read_csv()
    # print(df)
