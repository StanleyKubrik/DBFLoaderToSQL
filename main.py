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
    try:
        cfg = Config(CONFIG_PATH)  # Initialization cfg object.
        cfg_field_dict = cfg.get_dict_from_dbf(dbf_file_from)
        conn = connector()  # Initialization connector object.
        dbf = Dbf5(dbf_file_from, codec='1251')
        dbf_df = dbf.to_dataframe()
        df = pd.DataFrame(dbf_df)

        # Renaming fields in DataFrame(DBF) according to SQL table and delete fields that don't exist in config-file.
        for col in df.columns:
            if cfg_field_dict.keys().__contains__(col.lower()):
                df = df.rename(columns={f'{col}': f'{cfg_field_dict.get(col.lower())}'})
            else:
                df.__delitem__(col)

        # Writing NewDataFrame to SQL DB.
        before_ins_rows_count = pd.read_sql_query(f'SELECT COUNT(*) FROM {sql_table_to}', conn).values[0]
        df.to_sql(sql_table_to, conn, if_exists='append', index=False, chunksize=500)
        after_ins_rows_count = pd.read_sql_query(f'SELECT COUNT(*) FROM {sql_table_to}', conn).values[0]
        inserted_rows: int = after_ins_rows_count - before_ins_rows_count
        print(f'{inserted_rows[0]} rows successfully inserted from DBF "{dbf_file_from}" to table "{sql_table_to}".')
    except sqlalchemy.exc.ProgrammingError as pe:
        print(pe)
    except configparser.NoSectionError as nse:
        print(nse)
    except FileNotFoundError as fnf:
        print(fnf)
    except FileExistsError as fnf:
        print(f'File {CONFIG_PATH}')
    except sqlalchemy.exc.IntegrityError as ie:
        print(ie)


if __name__ == '__main__':
    insert_into_table(DBF_FILE, 'TypeOfServices')
    # dbf = Dbf5(DBF_FILE, codec='1251')
    # dbf_df = dbf.to_dataframe()
    # df = pd.DataFrame(dbf_df)
    # df_list = list(df['ID'])
    # print(df_list)
    # i = 0
    # while i < len(df_list):
    #     if len(df_list[i]) == 1:
    #         df_list[i] = str('     {}   ').format(df_list[i])
    #         i += 1
    # print(df_list)
