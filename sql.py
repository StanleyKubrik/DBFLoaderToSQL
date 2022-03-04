import sqlalchemy
from sqlalchemy import insert
import keyring
import pandas as pd


def connector():
    driver = 'ODBC Driver 17 for SQL Server'
    server = 'powerbivm1.dpst.kola'
    port = 1433
    database = 'petrykivka_test'
    username = 'sa'
    password = keyring.get_password('SQL', username)
    print(f'Connecting to SQL DB {database}...')
    try:
        engine = sqlalchemy.create_engine(f'mssql+pyodbc://{username}:{password}@{server}'
                                          f':{port}/{database}'
                                          f'?driver={driver}')
        engine.connect()
    except sqlalchemy.exc.InterfaceError as e:
        print(f"Can't connection to DB {database}: " + str(e))
    else:
        print(f'Connected to SQL DB {database}!')
        return engine


def get_table_fields_name(self, table_name: str, db_name='') -> pd.read_sql_query:
    try:
        pd_query = pd.read_sql_query("SELECT COLUMN_NAME "
                                     "FROM INFORMATION_SCHEMA.COLUMNS "
                                     f"WHERE TABLE_NAME = N'{table_name}'",
                                     self)
        if pd_query.empty:
            raise NameError('EmptyDataFrame')
        return pd_query.values.tolist()
    except NameError as ne:
        return f'ERROR: {ne}'
