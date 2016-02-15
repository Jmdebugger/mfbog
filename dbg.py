#!/usr/bin/python
# -*- coding:utf-8 -*-
import wx
class ProxyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)

        box = wx.StaticBox(self, -1, u"代理IP设置")
        bsizer = wx.StaticBoxSizer(box, wx.VERTICAL)

        t2 = wx.StaticText(self, -1, "Controls placed \"inside\" the box are really its siblings")
        t1 = wx.StaticText(self, -1, "Controls placed \"inside\" the box are really its siblings")
        bsizer.Add(t1, 1, wx.TOP|wx.LEFT)
        bsizer.Add(t2, 1, wx.TOP|wx.LEFT)


        border = wx.BoxSizer()
        border.Add(bsizer, 1, wx.EXPAND|wx.ALL)
        self.SetSizer(border)


class MyFrame(wx.Frame):
    def __init__(self, parent):
        super(MyFrame, self).__init__(parent, title="ListCtrl with Icons")

        # Attributes
        self._list = ProxyPanel(self)

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None)
        self.frame.Show()
        return True

if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
