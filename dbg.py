import sys
import wx
import wx.html2 as webview

#----------------------------------------------------------------------

class NotificationPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.mBrowser = wx.html2.WebView.New(self)
        self.mBrowser.LoadURL("http://www.baidu.com")
        sizer.Add(self.mBrowser ,1 , wx.EXPAND)
        self.SetSizer(sizer)

#----------------------------------------------------------------------


def main():
    app = wx.App()
    frm = wx.Frame(None, title="html2.WebView sample", size=(700,500))
    frm.CreateStatusBar()
    pnl = NotificationPanel(frm)
    frm.Show()
    app.MainLoop()


#----------------------------------------------------------------------

if __name__ == '__main__':
    main()