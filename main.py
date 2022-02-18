import keyring
import pandas as pd
import pyodbc
from simpledbf import Dbf5
from tkinter import filedialog


def create_csv_from_dbf(dbf_file_list: list):
    for dbf_file in dbf_file_list:
        try:
            dbf = Dbf5(dbf_file, codec='Windows-1251')
            csv_name = str(dbf_file).upper().replace('.DBF', '.CSV')
            dbf.to_csv(csv_name, header=True)
            print(csv_name + ' created!')
        except FileNotFoundError:
            print(f'DBF-file {dbf_file} not found in current directory!')


def connector() -> pyodbc.connect:
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
    # files_name = filedialog.askopenfilenames()
    # dbf_files_list = []
    # for i in files_name:
    #     if '.dbf'.lower() in i.split('/')[-1].lower():
    #         dbf_files_list.append(i.split('/')[-1])
    # create_csv_from_dbf(dbf_files_list)
    # df = pd.read_csv('DH5188.CSV', encoding='Windows-1251')
    dbf = Dbf5('DH5188.DBF', codec='Windows-1251')
    print(dbf.to_dataframe())
