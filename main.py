import configparser
from sql import *
from dbf_to_csv import *
from config import *
import pandas as pd
import glob
from simpledbf import Dbf5
import re

if __name__ == '__main__':
    # try:
    #     path = 'DH5188.DBF'
    #     ini_file = 'settings_Petrykivka.ini'
    #     config = Config(ini_file)
    #     dbf = Dbf5(path)
    #     config_column = [config.get_setting(path.split('.')[0], column) for column in dbf.columns]
    #     print(config_column)
    # except FileNotFoundError:
    #     print('DBF-file not found!')
    # except configparser.NoOptionError:
    #     print('Specified field not found in config file!')
    # path = 'DH5188.DBF'
    # dbf = Dbf5(path, codec='1251')
    # df = dbf.to_dataframe()
    # print(len(df))
    df = pd.read_sql_query('INSERT INTO gender'
                           '('
                           'ID'
                           ',DESCR'
                           # ',ID_c'
                           ')'
                           "VALUES('5KF      ', N'Средний')",
                           connector())
    print(df)
