import wx
import wx.xrc
from sql import insert_into_sql_table_from_dbf


class MainFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"DBF Loader To SQL v 1.0", pos=wx.DefaultPosition,
                          size=wx.Size(700, 400), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL,
                    False, wx.EmptyString))
        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        main_box_sizer = wx.BoxSizer(wx.VERTICAL)

        self.m_notebook3 = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_notebook3.SetFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        self.first_page = wx.Panel(self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        gbSizer2 = wx.GridBagSizer(5, 5)
        gbSizer2.SetFlexibleDirection(wx.BOTH)
        gbSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_ALL)

        self.main_label1 = wx.StaticText(self.first_page, wx.ID_ANY, u"Choose DBF file:", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.main_label1.Wrap(-1)

        self.main_label1.SetFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        gbSizer2.Add(self.main_label1, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 5)

        self.main_file_select = wx.FilePickerCtrl(self.first_page, wx.ID_ANY, wx.EmptyString, u"Select a DBF file",
                                                  u"DBF files (*.dbf)|*.dbf", wx.DefaultPosition, wx.DefaultSize,
                                                  wx.FLP_DEFAULT_STYLE | wx.FLP_FILE_MUST_EXIST | wx.FLP_OPEN)
        self.main_file_select.SetFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        gbSizer2.Add(self.main_file_select, wx.GBPosition(0, 1), wx.GBSpan(1, 4), wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl1 = wx.TextCtrl(self.first_page, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TE_MULTILINE | wx.TE_READONLY)
        gbSizer2.Add(self.m_textCtrl1, wx.GBPosition(2, 0), wx.GBSpan(1, 5), wx.ALL | wx.EXPAND, 5)

        self.uploadButton = wx.ToggleButton(self.first_page, wx.ID_ANY, u"Upload", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.uploadButton.SetFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        gbSizer2.Add(self.uploadButton, wx.GBPosition(1, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.closeButton = wx.ToggleButton(self.first_page, wx.ID_ANY, u"Close", wx.Point(-1, -1), wx.DefaultSize, 0)
        self.closeButton.SetFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        gbSizer2.Add(self.closeButton, wx.GBPosition(1, 4), wx.GBSpan(1, 1), wx.ALL, 5)

        gbSizer2.AddGrowableCol(1)
        gbSizer2.AddGrowableRow(2)

        self.first_page.SetSizer(gbSizer2)
        self.first_page.Layout()
        gbSizer2.Fit(self.first_page)
        self.m_notebook3.AddPage(self.first_page, u"Main", True)
        self.second_page = wx.Panel(self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_notebook3.AddPage(self.second_page, u"Configuration", False)

        main_box_sizer.Add(self.m_notebook3, 1, wx.EXPAND, 5)

        self.SetSizer(main_box_sizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.uploadButton.Bind(wx.EVT_TOGGLEBUTTON, self.onUpload)
        self.closeButton.Bind(wx.EVT_TOGGLEBUTTON, self.onClose)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def onUpload(self, event):
        event.Skip()
        dbf_file = self.main_file_select.GetPath()
        insert_into_sql_table_from_dbf(dbf_file.split('\\')[-1])

    def onClose(self, event):
        event.Skip()
        self.Destroy()

    # def outInConsole(self, message):
        
