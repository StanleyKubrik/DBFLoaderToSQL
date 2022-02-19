from simpledbf import Dbf5
import pandas as pd


def create_csv_from_dbf(dbf_file_list: list):
    for dbf_file in dbf_file_list:
        try:
            dbf = Dbf5(dbf_file, codec='Windows-1251')
            csv_name = str(dbf_file).upper().replace('.DBF', '.CSV')
            dbf.to_csv(csv_name, header=True)
            print(csv_name + ' created!')
        except FileNotFoundError:
            print(f'DBF-file {dbf_file} not found in current directory!')


def take_dbf_files(all_file: tuple) -> list:
    dbf_files_list = []
    for i in all_file:
        if '.dbf'.lower() in i.split('/')[-1].lower():
            dbf_files_list.append(i.split('/')[-1])
    return dbf_files_list
