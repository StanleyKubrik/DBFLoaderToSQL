import sqlalchemy
import keyring
import pandas as pd


def connector() -> sqlalchemy.engine:
    driver = 'ODBC Driver 17 for SQL Server'
    server = 'powerbivm1.dpst.kola'
    port = 1433
    database = 'petrykivka_test'
    username = 'sa'
    password = keyring.get_password('SQL', username)
    print(f'Connecting to SQL DB {database}...')
    try:
        engine = sqlalchemy.create_engine(f'mssql+pyodbc://{username}:{password}@{server}:{port}/{database}'
                                          f'?driver={driver}')
        engine.connect()
    except sqlalchemy.exc.InterfaceError as e:
        print(f"Can't connection to DB {database}: " + str(e))
    else:
        print(f'Connected to SQL DB {database}!')
        return engine


def get_table_fields_name(table_name: str, db_name='') -> pd.read_sql_query:
    try:
        fields_name = pd.read_sql_query("SELECT COLUMN_NAME "
                                        "FROM INFORMATION_SCHEMA.COLUMNS "
                                        f"WHERE TABLE_NAME = N'{table_name}'",
                                        connector())
        if fields_name.empty:
            raise NameError('EmptyDataFrame')
        return fields_name
    except NameError as ne:
        return f'ERROR: {ne}'
