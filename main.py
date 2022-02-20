from tkinter import filedialog
from connect_to_sql import connector
from dbf_to_csv import *

if __name__ == '__main__':
    files_name = filedialog.askopenfilenames()
    # create_csv_from_dbf(take_dbf_files(files_name))
    # df = pd.read_csv('DH5188.CSV', encoding='Windows-1251')
    # dbf = Dbf5('DH5188.DBF', codec='Windows-1251')
    # print(dbf.to_dataframe())
