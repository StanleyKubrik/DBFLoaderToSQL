from gui import GUI
from PyQt5.QtWidgets import QApplication
import sys
from sql import SQL

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = GUI()
    ui.main_window.show()
    sys.exit(app.exec_())

    # sql = SQL()
    # # for dbf in os.listdir('DBF/'):
    # #     sql.load_into_sql_table_from_dbf(os.getcwd() + '\\DBF\\' + dbf)
    # dbf = 'C:\\Users\\User\\Desktop\\DBFLoaderToSQL\\DBF\\RA7683.DBF'
    # sql.load_into_sql_table_from_dbf(dbf)
