#!/usr/bin/python
# -*- coding:utf-8 -*-
import wx

class MfTreeCtrl(wx.TreeCtrl):
    def __init__(self, *args, **kwargs):
        super(MfTreeCtrl, self).__init__(*args, **kwargs)



class MainFrame(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(MainFrame, self).__init__(*args, **kwargs)
        self.Centre()


if __name__ == "__main__":
    mainFrame = MainFrame()

