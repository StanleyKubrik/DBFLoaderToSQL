from gui import GUI
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = GUI()
    ui.main_window.show()
    sys.exit(app.exec_())

    # sql = SQL()
    # for dbf in os.listdir('DBF/'):
    #     sql.load_into_sql_table_from_dbf(os.getcwd() + '\\DBF\\' + dbf)
    # sql.load_into_sql_table_from_dbf('C:\\Users\\SUPERMAN\\Desktop\\DBFLoaderToSQL\\DBF\\1SJOURN.DBF')
    # table = pd.read_sql_table('1SJOURN_test', sql.engine)
    # vfunc = np.vectorize(sql.from_36_to_time)
    # table['TIME'] = vfunc(table['TIME'].values)
    # table.to_sql('1SJOURN_test', sql.engine, if_exists='replace', index=False)
