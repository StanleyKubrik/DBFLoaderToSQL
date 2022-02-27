import configparser
from sql import *
from dbf import *
from config import *
import pandas as pd
import glob
from simpledbf import Dbf5
import re

DBF_FILE = 'DH5188.DBF'
CONFIG_PATH = 'settings_Petrykivka.ini'


def insert_into_table(from_dbf: str, to_sql: str):
    cfg = Config(CONFIG_PATH)
    field_dict = cfg.get_dict_from_dbf()


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
    print()
