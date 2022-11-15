from gui import GUI
from PyQt5.QtWidgets import QApplication
import sys
from sql import SQL
from config import Config
import pandas as pd
from simpledbf import Dbf5

if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # ui = GUI()
    # ui.main_window.show()
    # sys.exit(app.exec_())

    # sql = SQL()
    # # for dbf in os.listdir('DBF/'):
    # #     sql.load_into_sql_table_from_dbf(os.getcwd() + '\\DBF\\' + dbf)
    # dbf = 'C:\\Users\\User\\Desktop\\DBFLoaderToSQL\\DBF\\RA7683.DBF'
    # sql.load_into_sql_table_from_dbf(dbf)

    EXCHANGE_CONFIG_PATH = 'settings_Petrykivka.ini'
    exchange_cfg = Config(EXCHANGE_CONFIG_PATH)

    dbf_file_from = 'RA7683.DBF'
    dbf_file_from_path = 'C:\\Users\\SUPERMAN\\Desktop\\DBFLoaderToSQL\\DBF\\RA7683.DBF'
    cfg_field_dict = exchange_cfg.get_dict_from_dbf(dbf_file_from)
    # sql_table_to = sql.get_sql_table_name_for_dbf(dbf_file_from)
    # cfg_field_dict = exchange_cfg.get_dict_from_dbf(dbf_file_from)
    # dbf = Dbf5(dbf_file_from_path, codec='1251')
    pd_table = pd.read_table(dbf_file_from_path, encoding='1251')
    for row in pd_table.values[1]:
        print(row)
    # for col in pd_table.columns:
    #     if cfg_field_dict.keys().__contains__(col.lower()):
    #         pd_table = pd_table.rename(columns={f'{col}': f'{cfg_field_dict.get(col.lower())}'})
    #     else:
    #         pd_table.__delitem__(col)
    # pd_table.to_csv('second.csv')
    # dbf_df = dbf.to_dataframe()
    # df = pd.DataFrame(dbf_df)
