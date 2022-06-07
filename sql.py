from simpledbf import Dbf5
from config import *
import sqlalchemy
import keyring
import pandas as pd
import numpy as np
from datetime import datetime

EXCHANGE_CONFIG_PATH = 'settings_Petrykivka.ini'
exchange_cfg = Config(EXCHANGE_CONFIG_PATH)
APP_CONFIG_PATH = 'config.ini'
app_config = Config(APP_CONFIG_PATH)


class SQL:

    def connector(self):
        driver = 'ODBC Driver 17 for SQL Server'
        server = app_config.get_setting('SQL', 'server')  # or 'powerbivm1.dpst.kola'
        port = app_config.get_setting('SQL', 'port')  # or 1433
        database = app_config.get_setting('SQL', 'database')  # or 'petrykivka_test'
        username = app_config.get_setting('SQL', 'username')  # or 'sa'
        password = app_config.get_setting('SQL', 'password')  # or keyring.get_password('SQL', username)
        print(datetime.now().strftime("%H:%M:%S"), '|', f'Connecting to SQL DB {database}...')
        try:
            connection_uri = f'mssql+pyodbc://{username}:{password}@{server}:{port}/{database}?driver={driver}'
            engine = sqlalchemy.create_engine(connection_uri, fast_executemany=True)
            engine.connect()
        except sqlalchemy.exc.InterfaceError as e:
            print(datetime.now().strftime("%H:%M:%S"), '|', f"Can't connection to DB {database}: " + str(e))
        else:
            print(datetime.now().strftime("%H:%M:%S"), '|', f'Connected to SQL DB {database}!')
            return engine

    def load_into_sql_table_from_dbf(self, dbf_file_from: str):
        """
        Loading data from DBF-file to SQL table.
        :param dbf_file_from: name of uploading DBF-file.
        """
        from interface import MainFrame
        try:
            sql_table_to = self.get_sql_table_name_for_dbf(dbf_file_from)
            cfg_field_dict = exchange_cfg.get_dict_from_dbf(dbf_file_from)
            conn = self.connector()  # Initialization connector object.
            dbf = Dbf5(dbf_file_from, codec='1251')  # Initialization Dbf5 object.
            dbf_df = dbf.to_dataframe()  # Create simpledbf DataFrame.
            df = pd.DataFrame(dbf_df)  # Converting simpledbf DF to pandas DF.
            sql_table = pd.read_sql_table(sql_table_to, conn)  # , columns=id_fields)

            # Renaming fields in DataFrame(DBF) according to SQL table and delete fields that don't exist in config-file.
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
            id_fields = []
            for field in dbf.fields:
                if field[1] == 'C' and field[2] == 9 and exchange_cfg.has_option(dbf_file_from.split('.')[0], field[0]):
                    value = cfg_field_dict.get(field[0].lower())
                    id_fields.append(value)

            # Appending spaces to each value in the specified column.
            print(datetime.now().strftime("%H:%M:%S"), '|', 'Appending spaces to each value in the specified column...')
            vfunc = np.vectorize(self.fill_field_with_spaces)  # Map array.
            for col in id_fields:
                df[col] = vfunc(df[col].values)  # Assign mapped array to dataframe.
                # for v in df[col].values:
                #     df = df.replace({v: fill_field_with_spaces(v)})

            # Check rows count before insert.
            before_ins_rows_count = pd.read_sql_query(f'SELECT COUNT(*) FROM {sql_table_to}', conn).values[0]
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
            # Writing DataFrame to SQL DB.
            print(datetime.now().strftime("%H:%M:%S"), '|', 'Writing DataFrame to SQL DB...')
            df.to_sql(sql_table_to, conn, if_exists='append', index=False)
            # Check rows count after insert.
            after_ins_rows_count = pd.read_sql_query(f'SELECT COUNT(*) FROM {sql_table_to}', conn).values[0]
            # Calculating and output inserted rows quantity.
            inserted_rows: int = after_ins_rows_count[0] - before_ins_rows_count[0]
            print(datetime.now().strftime("%H:%M:%S"), '|',
                  f'{inserted_rows} rows successfully inserted from DBF "{dbf_file_from}" to table "{sql_table_to}".')
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

    def get_sql_table_name_for_dbf(self, dbf_file_name: str):
        """
        Getting SQL table name from configuration file according to received DBF file.
        :param dbf_file_name: name of DBF-file.
        :return: SQL table name according to the configuration file.
        :rtype: str
        """

        section_list = re.findall('\d+', dbf_file_name.split('.')[0])
        section = ''.join(section_list)
        if dbf_file_name.startswith('DH'):
            return 'DH_' + exchange_cfg.get_setting('Documents', section)
        elif dbf_file_name.startswith('DT'):
            return 'DT_' + exchange_cfg.get_setting('Documents', section)
        elif dbf_file_name.startswith('SC'):
            return exchange_cfg.get_setting('References', section)
        elif dbf_file_name.startswith('RA'):
            return 'RA_' + exchange_cfg.get_setting('Registers', section)
        elif dbf_file_name.startswith('RM'):
            return 'RM_' + exchange_cfg.get_setting('Registers', section)

    # def get_table_fields_name(table_name: str, db_name='') -> pd.read_sql_query:
    #     try:
    #         pd_query = pd.read_sql_query("SELECT COLUMN_NAME "
    #                                      "FROM INFORMATION_SCHEMA.COLUMNS "
    #                                      f"WHERE TABLE_NAME = N'{table_name}'",
    #                                      connector())
    #         if pd_query.empty:
    #             raise NameError('EmptyDataFrame')
    #         return pd_query.values.tolist()
    #     except NameError as ne:
    #         return f'ERROR: {ne}'
