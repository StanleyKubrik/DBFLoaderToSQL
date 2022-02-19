import keyring
import pyodbc


def connector() -> pyodbc.connect:
    driver = '{ODBC Driver 17 for SQL Server}'
    server = 'powerbivm1.dpst.kola'
    database = 'petrykivka_test'
    username = 'sukhonosovn'
    password = keyring.get_password('SQL', username)
    print('Connection to SQL DB...')
    try:
        conn = pyodbc.connect('DRIVER=' + driver
                              + ';SERVER=' + server
                              + ';DATABASE=' + database
                              + ';UID=' + username
                              + ';PWD=' + password)
    except pyodbc.OperationalError as e:
        print("Can't connection to DB: " + str(e))
    else:
        return conn
