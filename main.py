from interface import MainFrame
import wx


if __name__ == '__main__':
    app = wx.App()

    frame = MainFrame(None)
    frame.Show()

    app.MainLoop()
