# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from sql import SQL


###########################################################################
## Class MainFrame
###########################################################################

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
        gbSizer_main = wx.GridBagSizer(5, 5)
        gbSizer_main.SetFlexibleDirection(wx.BOTH)
        gbSizer_main.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_ALL)

        self.lbl_choose_dbf = wx.StaticText(self.first_page, wx.ID_ANY, u"Choose DBF file:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.lbl_choose_dbf.Wrap(-1)

        self.lbl_choose_dbf.SetFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        gbSizer_main.Add(self.lbl_choose_dbf, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.EXPAND | wx.LEFT | wx.TOP, 8)

        self.filepicker_file_select = wx.FilePickerCtrl(self.first_page, wx.ID_ANY, wx.EmptyString,
                                                        u"Select a DBF file", u"DBF files (*.dbf)|*.dbf",
                                                        wx.DefaultPosition, wx.DefaultSize,
                                                        wx.FLP_DEFAULT_STYLE | wx.FLP_FILE_MUST_EXIST | wx.FLP_OPEN)
        self.filepicker_file_select.SetFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        gbSizer_main.Add(self.filepicker_file_select, wx.GBPosition(0, 1), wx.GBSpan(1, 4),
                         wx.EXPAND | wx.RIGHT | wx.TOP, 5)

        self.txt_console = wx.TextCtrl(self.first_page, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TE_MULTILINE | wx.TE_READONLY)
        gbSizer_main.Add(self.txt_console, wx.GBPosition(2, 0), wx.GBSpan(1, 5), wx.ALL | wx.EXPAND, 5)

        self.uploadButton = wx.ToggleButton(self.first_page, wx.ID_ANY, u"Upload", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.uploadButton.SetFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        gbSizer_main.Add(self.uploadButton, wx.GBPosition(1, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.closeButton = wx.ToggleButton(self.first_page, wx.ID_ANY, u"Close", wx.Point(-1, -1), wx.DefaultSize, 0)
        self.closeButton.SetFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        gbSizer_main.Add(self.closeButton, wx.GBPosition(1, 4), wx.GBSpan(1, 1), wx.ALL, 5)

        gbSizer_main.AddGrowableCol(1)
        gbSizer_main.AddGrowableRow(2)

        self.first_page.SetSizer(gbSizer_main)
        self.first_page.Layout()
        gbSizer_main.Fit(self.first_page)
        self.m_notebook3.AddPage(self.first_page, u"Main", True)
        self.second_page = wx.Panel(self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        gbSizer_configuration = wx.GridBagSizer(0, 0)
        gbSizer_configuration.SetFlexibleDirection(wx.BOTH)
        gbSizer_configuration.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.lbl_configuration_server = wx.StaticText(self.second_page, wx.ID_ANY, u"Server:", wx.DefaultPosition,
                                                      wx.DefaultSize, 0)
        self.lbl_configuration_server.Wrap(-1)

        self.lbl_configuration_server.SetFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        gbSizer_configuration.Add(self.lbl_configuration_server, wx.GBPosition(0, 0), wx.GBSpan(1, 1),
                                  wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.EXPAND, 5)

        self.txt_server = wx.TextCtrl(self.second_page, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(250, -1),
                                      0)
        gbSizer_configuration.Add(self.txt_server, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        self.lbl_configuration_port = wx.StaticText(self.second_page, wx.ID_ANY, u"Port:", wx.DefaultPosition,
                                                    wx.DefaultSize, 0)
        self.lbl_configuration_port.Wrap(-1)

        self.lbl_configuration_port.SetFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        gbSizer_configuration.Add(self.lbl_configuration_port, wx.GBPosition(0, 2), wx.GBSpan(1, 1),
                                  wx.EXPAND | wx.LEFT | wx.TOP, 8)

        self.txt_port = wx.TextCtrl(self.second_page, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(50, -1), 0)
        gbSizer_configuration.Add(self.txt_port, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.lbl_configuration_database = wx.StaticText(self.second_page, wx.ID_ANY, u"Database:", wx.DefaultPosition,
                                                        wx.DefaultSize, 0)
        self.lbl_configuration_database.Wrap(-1)

        self.lbl_configuration_database.SetFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        gbSizer_configuration.Add(self.lbl_configuration_database, wx.GBPosition(1, 0), wx.GBSpan(1, 1),
                                  wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.EXPAND, 5)

        self.txt_database = wx.TextCtrl(self.second_page, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(150, -1), 0)
        gbSizer_configuration.Add(self.txt_database, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.lbl_configuration_username = wx.StaticText(self.second_page, wx.ID_ANY, u"Username:", wx.DefaultPosition,
                                                        wx.DefaultSize, 0)
        self.lbl_configuration_username.Wrap(-1)

        self.lbl_configuration_username.SetFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        gbSizer_configuration.Add(self.lbl_configuration_username, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.txt_username = wx.TextCtrl(self.second_page, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(150, -1), 0)
        gbSizer_configuration.Add(self.txt_username, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.lbl_configuration_password = wx.StaticText(self.second_page, wx.ID_ANY, u"Password:", wx.DefaultPosition,
                                                        wx.DefaultSize, 0)
        self.lbl_configuration_password.Wrap(-1)

        self.lbl_configuration_password.SetFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        gbSizer_configuration.Add(self.lbl_configuration_password, wx.GBPosition(3, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.txt_password = wx.TextCtrl(self.second_page, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(150, -1), wx.TE_PASSWORD)
        gbSizer_configuration.Add(self.txt_password, wx.GBPosition(3, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.second_page.SetSizer(gbSizer_configuration)
        self.second_page.Layout()
        gbSizer_configuration.Fit(self.second_page)
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
        try:
            dbf_file = self.filepicker_file_select.GetPath()
            if not dbf_file:
                raise FileExistsError
            SQL().load_into_sql_table_from_dbf(dbf_file.split('\\')[-1])
        except FileExistsError:
            print('ERROR: Please choose DBF-file!')
            self.outInConsole('ERROR: Please choose DBF-file!')

    def onClose(self, event):
        event.Skip()
        self.Destroy()

    def outInConsole(self, message):
        self.txt_console.AppendText(message + '\n')