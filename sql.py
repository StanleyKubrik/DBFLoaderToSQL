from simpledbf import Dbf5
from config import *
import sqlalchemy
import pandas as pd
import numpy as np
from datetime import datetime

EXCHANGE_CONFIG_PATH = 'settings_Petrykivka.ini'
exchange_cfg = Config(EXCHANGE_CONFIG_PATH)
APP_CONFIG_PATH = 'config.ini'
app_config = Config(APP_CONFIG_PATH)


class SQL:
    # def __init__(self):
    #     self.driver = 'ODBC Driver 17 for SQL Server'
    #     self.server = app_config.get_setting('SQL', 'server')
    #     self.port = app_config.get_setting('SQL', 'port')
    #     self.database = app_config.get_setting('SQL', 'database')
    #     self.username = app_config.get_setting('SQL', 'username')
    #     self.password = app_config.get_setting('SQL', 'password')

    def __init__(self):
        self.engine = None
        self.driver = 'ODBC Driver 17 for SQL Server'
        self.server = app_config.get_setting('SQL', 'server')
        self.port = app_config.get_setting('SQL', 'port')
        self.database = app_config.get_setting('SQL', 'database')
        self.username = app_config.get_setting('SQL', 'username')
        self.password = app_config.get_setting('SQL', 'password')
        # driver = self.driver
        # server = self.server
        # port = self.port
        # database = self.database
        # username = self.username
        # password = self.password
        print(datetime.now().strftime("%H:%M:%S"), '|', f'Connecting to SQL DB {self.database}...')
        try:
            if self.engine is None:
                connection_uri = f'mssql+pyodbc://{self.username}:{self.password}@{self.server}:{self.port}' \
                                 f'/{self.database}?driver={self.driver}'
                self.engine = sqlalchemy.create_engine(connection_uri, fast_executemany=True)
                self.engine.connect()
        except sqlalchemy.exc.InterfaceError as e:
            print(datetime.now().strftime("%H:%M:%S"), '|', f"Can't connection to DB {self.database}: " + str(e))
        else:
            print(datetime.now().strftime("%H:%M:%S"), '|', f'Connected to SQL DB {self.database}!')

    def load_into_sql_table_from_dbf(self, dbf_file_from_path: str):
        """
        Loading data from DBF-file to SQL table.
        :param dbf_file_from_path: path to DBF-file.
        """
        try:
            dbf_file_from = dbf_file_from_path.split('\\')[-1]
            sql_table_to = self.get_sql_table_name_for_dbf(dbf_file_from)
            cfg_field_dict = exchange_cfg.get_dict_from_dbf(dbf_file_from)
            # Init Dbf5 object.
            print(datetime.now().strftime("%H:%M:%S"), '|', f'Init Dbf5 object...')
            dbf = Dbf5(dbf_file_from_path, codec='1251')
            # Create simpledbf DataFrame.
            print(datetime.now().strftime("%H:%M:%S"), '|', f'Create simpledbf DataFrame...')
            dbf_df = dbf.to_dataframe()
            # Converting simpledbf DF to Pandas DF.
            print(datetime.now().strftime("%H:%M:%S"), '|', f'Converting simpledbf DF to Pandas DF...')
            df = pd.DataFrame(dbf_df)
            # Reading SQL table.
            print(datetime.now().strftime("%H:%M:%S"), '|', f'Reading SQL table...')
            sql_table = pd.read_sql_table(sql_table_to, self.engine)
            print(datetime.now().strftime("%H:%M:%S"), '|', f'Start uploading {dbf_file_from}...')

            # Renaming fields in DataFrame(DBF) according to SQL table and delete fields that don't exist in config.
            print(datetime.now().strftime("%H:%M:%S"), '|',
                  "Renaming fields in DataFrame(DBF) according to SQL table and delete fields that don't exist in "
                  "config-file...")
            for col in df.columns:
                if cfg_field_dict.keys().__contains__(col.lower()):
                    df = df.rename(columns={f'{col}': f'{cfg_field_dict.get(col.lower())}'})
                else:
                    df.__delitem__(col)

            # Pad ID fields with spaces to 9 chars.
            # Create a list with ID fields.
            print(datetime.now().strftime("%H:%M:%S"), '|', 'Create a list with ID fields...')
            id_fields = []  # or (field[1] == 'C' and field[2] == 9)
            if dbf_file_from == '1SJOURN.DBF':
                section = 'Journal'
            else:
                section = dbf_file_from.split('.')[0]
            for field in dbf.fields:
                if field[1] == 'C' and field[2] == 9 and exchange_cfg.has_option(section, field[0]):
                    value = cfg_field_dict.get(field[0].lower())
                    id_fields.append(value)

            # Appending spaces to each value in the specified column.
            print(datetime.now().strftime("%H:%M:%S"), '|', 'Appending spaces to each value in the specified column...')
            vfunc = np.vectorize(self.fill_field_with_spaces)  # Map array.
            for col in id_fields:
                df[col] = vfunc(df[col].values)  # Assign mapped array to dataframe.
                # for v in df[col].values:
                #     df = df.replace({v: fill_field_with_spaces(v)})

            print(datetime.now().strftime("%H:%M:%S"), '|', 'Looking for exist keys...')
            # Looking for exist keys.
            dropped_rows = 0
            for row in df.itertuples(name=None):
                if not sql_table.empty:  # Check SQL table for data.
                    if row[1] in sql_table[id_fields[0]].values:
                        df = df.drop(row[0])
                        dropped_rows += 1
            print(datetime.now().strftime("%H:%M:%S"), '|',
                  f'Table "{sql_table_to}" already exist {dropped_rows} keys!')
            # Remember the number of rows before inserting.
            before_insert_rows = pd.read_sql_query(f'SELECT COUNT(*) FROM [{sql_table_to}]', self.engine).values[0]
            # Writing DataFrame to SQL DB.
            print(datetime.now().strftime("%H:%M:%S"), '|', 'Writing DataFrame to SQL DB...')
            df.to_sql(sql_table_to, self.engine, if_exists='append', index=False)
            # Counting rows after inserting.
            after_insert_rows = pd.read_sql_query(f'SELECT COUNT(*) FROM [{sql_table_to}]', self.engine).values[0]
            # Output inserted rows quantity.
            ins_rows: int = after_insert_rows[0] - before_insert_rows[0]
            print(datetime.now().strftime("%H:%M:%S"), '|',
                  f'{ins_rows} rows successfully inserted from DBF "{dbf_file_from}" to table "{sql_table_to}".'
                  f'\n')
        except sqlalchemy.exc.ProgrammingError as pe:
            print(pe)
        except configparser.NoSectionError as nse:
            print(nse)
        except FileNotFoundError as fnf:
            print(fnf)
        # except FileExistsError as fee:
        #     print(f'Configuration file "{config_file}" not found! {fee}')
        except sqlalchemy.exc.IntegrityError as ie:
            print(ie)
        except ValueError as ve:
            print(ve)

    def fill_field_with_spaces(self, field: str) -> str:
        """
        Filling ID fields with spaces according to 1C 7.7 ID format.
        :param field: ID field without spaces.
        :return: ID field with spaces.
        """

        field = field.strip()
        if len(field) > 1 and str(field).endswith('1'):
            return str(field).rjust(7) + '  '
        else:
            return str(field).rjust(6) + '   '

    def get_sql_table_name_for_dbf(self, dbf_file_name: str) -> str:
        """
        Getting SQL table name from configuration file according to received DBF file.
        :param dbf_file_name: name of DBF-file.
        :return: SQL table name according to the configuration file.
        :rtype: str
        """

        section_list = re.findall('\d+', dbf_file_name.split('.')[0])
        section = ''.join(section_list)
        if dbf_file_name == '1SJOURN.DBF':
            return '1SJOURN_test'
        elif dbf_file_name.startswith('DH'):
            return 'DH_' + exchange_cfg.get_setting('Documents', section)
        elif dbf_file_name.startswith('DT'):
            return 'DT_' + exchange_cfg.get_setting('Documents', section)
        elif dbf_file_name.startswith('SC'):
            return exchange_cfg.get_setting('References', section)
        elif dbf_file_name.startswith('RA'):
            return 'RA_' + exchange_cfg.get_setting('Registers', section)
        elif dbf_file_name.startswith('RM'):
            return 'RM_' + exchange_cfg.get_setting('Registers', section)


# def base36encode(number, alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
#     """Converts an integer to a base36 string."""
#     if not isinstance(number, int):
#         raise TypeError('number must be an integer')
#
#     base36 = ''
#     sign = ''
#
#     if number < 0:
#         sign = '-'
#         number = -number
#
#     if 0 <= number < len(alphabet):
#         return sign + alphabet[number]
#
#     while number != 0:
#         number, i = divmod(number, len(alphabet))
#         base36 = alphabet[i] + base36
#
#     return sign + base36
#
#
# def base36decode(number):
#     return int(number, 36)
