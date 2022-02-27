from simpledbf import Dbf5
import pandas as pd
import os


# def create_csv_from_dbf(dbf_file_list: list):
#     for dbf_file in dbf_file_list:
#         try:
#             dbf = Dbf5(dbf_file, codec='Windows-1251')
#             csv_name = str(dbf_file).upper().replace('.DBF', '.CSV')
#             dbf.to_csv(csv_name, header=True)
#             print(csv_name + ' created!')
#         except FileNotFoundError:
#             print(f'DBF-file {dbf_file} not found in current directory!')
