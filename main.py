from simpledbf import Dbf5

from gui import GUI
from PyQt5.QtWidgets import QApplication
import sys

from sql import SQL
import os

import pandas as pd


if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # ui = GUI()
    # ui.main_window.show()
    # sys.exit(app.exec_())
    sql = SQL()
    for dbf in os.listdir('DBF/'):
        sql.load_into_sql_table_from_dbf(os.getcwd() + '\\DBF\\' + dbf)
    # sql.load_into_sql_table_from_dbf("C:\\Users\\SUPERMAN\\Desktop\\DBFLoaderToSQL\\DBF\\1SJOURN.DBF")
