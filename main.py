from simpledbf import Dbf5
import pandas as pd
import pyodbc

# dbf = Dbf5('DH5188.DBF', codec='Windows-1251')
# dbf.to_csv('DH5188.csv')
# print(df)

driver = '{ODBC Driver 18 for SQL Server}'
server = 'powerbivm1.dpst.kola'
database = 'petrykivka_test'
username = 'sukhonosovn'
password = 'Fe%f8Pyz'

conn = pyodbc.connect(driver=driver,
                      server=server,
                      database=database,
                      uid=username,
                      pwd=password)
cursor = conn.cursor()
cursor.execute('SELECT * FROM gender')

# df = pd.read_sql_query('SELECT * FROM gender', conn)
