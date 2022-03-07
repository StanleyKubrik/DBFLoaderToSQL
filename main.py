import keyring

from sql import *
from config import *
import pandas as pd
from simpledbf import Dbf5
from sqlalchemy import *

DBF_FILE = 'SC5174.DBF'
SQL_TABLE = 'TypeOfServices'
CONFIG_PATH = 'settings_Petrykivka.ini'


def pad_field_with_spaces(field: str) -> str:
    field = field.strip()
    if len(field) > 1 and str(field).endswith('1'):
        return str(field).rjust(7) + '  '
    else:
        return str(field).rjust(6) + '   '


# Need to debugging check for exist key in SQL table.
def insert_into_table(dbf_file_from: str, sql_table_to: str):
    try:
        cfg = Config(CONFIG_PATH)  # Initialization cfg object.
        cfg_field_dict = cfg.get_dict_from_dbf(dbf_file_from)
        conn = connector()  # Initialization connector object.
        dbf = Dbf5(dbf_file_from, codec='1251')  # Initialization Dbf5 object.
        dbf_df = dbf.to_dataframe()  # Create simpledbf DataFrame.
        df = pd.DataFrame(dbf_df)  # Converting simpledbf DF to pandas DF.

        # Renaming fields in DataFrame(DBF) according to SQL table and delete fields that don't exist in config-file.
        for col in df.columns:
            if cfg_field_dict.keys().__contains__(col.lower()):
                df = df.rename(columns={f'{col}': f'{cfg_field_dict.get(col.lower())}'})
            else:
                df.__delitem__(col)

        # Pad ID fields with spaces to 9 chars.
        # Create a list with ID fields.
        id_fields = []
        for field in dbf.fields:
            if field[1] == 'C' and field[2] == 9:
                id_fields.append(field[0])

        # Appending spaces to each value in the specified column.
        for col in df.columns:
            if col in id_fields:  # Check if fields is ID.
                for v in df[col].values:
                    df = df.replace({v: pad_field_with_spaces(v)})

        sql_table = pd.read_sql_table(sql_table_to, conn, columns=id_fields)

        # Writing DataFrame to SQL DB.
        # Check rows count before insert.
        before_ins_rows_count = pd.read_sql_query(f'SELECT COUNT(*) FROM {sql_table_to}', conn).values[0]
        # Inserting DF to SQL.
        for row in df.itertuples(index=False, name=None):
            if row[0] not in sql_table[id_fields[0]].values:
                df_row = pd.DataFrame(row)
                df_row.to_sql(str(row), conn, if_exists='append', index=False, chunksize=500)
            else:
                print(f'Table "{sql_table_to}" already exist key "{row[0]}"!')
        # Check rows count after insert.
        after_ins_rows_count = pd.read_sql_query(f'SELECT COUNT(*) FROM {sql_table_to}', conn).values[0]
        # Calculating and output inserted rows quantity.
        inserted_rows: int = after_ins_rows_count[0] - before_ins_rows_count[0]
        print(f'{inserted_rows} rows successfully inserted from DBF "{dbf_file_from}" to table "{sql_table_to}".')
    except sqlalchemy.exc.ProgrammingError as pe:
        print(pe)
    except configparser.NoSectionError as nse:
        print(nse)
    except FileNotFoundError as fnf:
        print(fnf)
    except FileExistsError as fee:
        print(f'Configuration file {CONFIG_PATH} not found! {fee}')
    except sqlalchemy.exc.IntegrityError as ie:
        print(ie)


if __name__ == '__main__':
    insert_into_table(DBF_FILE, SQL_TABLE)
