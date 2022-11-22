from config import Config
from gui import GUI
from PyQt5.QtWidgets import QApplication
from sql import SQL
import pandas as pd
from simpledbf import Dbf5
import os

if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # ui = GUI()
    # ui.main_window.show()
    # sys.exit(app.exec_())

    sql = SQL()
    dbf_file_from = '1SJOURN.DBF'
    current_path = os.getcwd()
    # for dbf in os.listdir('DBF/'):
    #     sql.load_into_sql_table_from_dbf(os.getcwd() + '\\DBF\\' + dbf)
    dbf = f'{current_path}\\DBF\\{dbf_file_from}'
    sql.load_into_sql_table_from_dbf(dbf)

    # EXCHANGE_CONFIG_PATH = 'settings_Petrykivka.ini'
    # exchange_cfg = Config(EXCHANGE_CONFIG_PATH)
    #
    # dbf_file_from = 'RA7683.DBF'
    # dbf_file_from_path = 'C:\\Users\\User\\Desktop\\DBFLoaderToSQL\\DBF\\RA7683.DBF'
    # cfg_field_dict = exchange_cfg.get_dict_from_dbf(dbf_file_from)
    # # sql_table_to = sql.get_sql_table_name_for_dbf(dbf_file_from)
    # # cfg_field_dict = exchange_cfg.get_dict_from_dbf(dbf_file_from)
    #
    # dbf = Dbf5(dbf_file_from_path, codec='1251')
    # dbf_df = dbf.to_dataframe()
    # df = pd.DataFrame(dbf_df)
    # pd_df = pd.read_table(dbf_file_from_path, encoding='1251')
    # print(pd_df)
