from interface import MainFrame
import wx
from sql import insert_into_sql_table_from_dbf

DBF = 'RA7683.DBF'

if __name__ == '__main__':
    # app = wx.App()
    #
    # frame = MainFrame(None)
    # frame.Show()
    #
    # app.MainLoop()
    insert_into_sql_table_from_dbf(DBF)
