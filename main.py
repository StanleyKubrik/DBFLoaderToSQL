import keyring
import pandas as pd
import pyodbc
import sqlalchemy as salc


# dbf = Dbf5('DH5188.DBF', codec='Windows-1251')
# dbf.to_csv('DH5188.csv')
# print(df)

# def connect_to_sql() -> pyodbc.connect:
#     driver = '{ODBC Driver 17 for SQL Server}'
#     server = 'powerbivm1.dpst.kola'
#     database = 'petrykivka_test'
#     username = 'sukhonosovn'
#     password = keyring.get_password('SQL', username)
#     print('Connection to SQL DB...')
#     try:
#         conn = pyodbc.connect('DRIVER=' + driver
#                               + ';SERVER=' + server
#                               + ';DATABASE=' + database
#                               + ';UID=' + username
#                               + ';PWD=' + password)
#     except pyodbc.OperationalError as e:
#         print("Can't connection to DB: " + str(e))
#     else:
#         return conn
#
#
# if __name__ == '__main__':
#     df = pd.read_sql_query('SELECT * FROM gender', connect_to_sql())
#     print(df)
#
# driver = '{ODBC Driver 17 for SQL Server}'
# server = 'powerbivm1.dpst.kola'
# database = 'petrykivka_test'
# username = 'sukhonosovn'
# password = keyring.get_password('SQL', username)
#
# connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
# connection_url = salc.engine.URL.create('mysql+pyodbc', query={'odbc_connect': connection_string})
#
# engine = salc.create_engine(connection_url)
# engine.connect()

username = 'sukhonosovn'
password = keyring.get_password('SQL', username)
connection = pyodbc.connect(f'DSN=SQL;UID={username};PWD={password}')
cursor = connection.cursor()
genders = cursor.execute('SELECT * FROM gender')
for i in genders:
    print(i)

# engine = salc.engine.create_engine(
#     f"mssql+pyodbc://{username}:{password}@powerbivm1.dpst.kola:1433/petrykivka_test"
#     "?driver=ODBC+Driver+17+for+SQL+Server"
#     # "&authentication=ActiveDirectoryIntegrated"
# )
# engine.connect()
