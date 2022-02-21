from tkinter import filedialog
from connect_to_sql import connector
from dbf_to_csv import *
from config import *

if __name__ == '__main__':
    # files_name = filedialog.askopenfilenames()
    config = Config('settings_Petrykivka.ini')
    print(config.get_setting('DH5188', 'IDDOC'))
