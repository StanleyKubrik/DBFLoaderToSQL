import configparser
from sql import *
from dbf import *
from config import *
import pandas as pd
import glob
from simpledbf import Dbf5
from sqlalchemy import *

DBF_FILE = 'SC5174.DBF'
CONFIG_PATH = 'settings_Petrykivka.ini'


def insert_into_table(dbf_file_from: str, sql_table_to: str):
    # cfg = Config(CONFIG_PATH)
    # cfg_field_dict = cfg.get_dict_from_dbf(dbf_file_from)
    # sql_fields = get_table_fields_name(sql_table_to)
    # query_text = f'INSERT INTO {sql_table_to} ('
    # for field in sql_fields:
    #     if field[0] in cfg_field_dict.values():
    #         query_text += f'\n {field[0]},'
    # # for value in cfg_field_dict.values():
    # query_text += ') VALUES ('
    # query_text = query_text.replace(',)', ')\n')
    conn = connector()
    insert_table = table(sql_table_to)
    dbf = Dbf5(DBF_FILE, codec='1251')
    dbf_df = dbf.to_dataframe()
    df = pd.DataFrame(dbf_df)
    before_ins_rows_count = pd.read_sql_query(f'SELECT COUNT(*) FROM {sql_table_to}', conn)[0]
    # conn.execute(insert(insert_table), df.to_records(index=False)[0])
    conn.execute(insert(insert_table), "('1', '0', '0000000001', 'электроэнергия', 2, NULL, '0', 0)")
    after_ins_rows_count = pd.read_sql_query(f'SELECT COUNT(*) FROM {sql_table_to}', conn)[0]
    print(before_ins_rows_count)
    print(after_ins_rows_count)
    # print(df.to_records(index=False)[0])


if __name__ == '__main__':
    insert_into_table(DBF_FILE, 'TypeOfServices')

