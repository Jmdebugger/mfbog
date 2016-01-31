#!/usr/bin/python
# -*- coding:utf-8 -*-
import wx
import ui
import glob
import sys


class Main(wx.App):
    def __init__(self, redirect=False, filename=None, useBestVisual=False, clearSigInt=True):
        super(Main, self).__init__(redirect, filename, useBestVisual, clearSigInt)


if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main = Main()
    customsize = (wx.DisplaySize()[0]*0.7 ,wx.DisplaySize()[1]*0.9)
    frame = ui.MainFrame(None, wx.ID_ANY, glob.SOFTWARE_NAME, size = customsize)
    main.MainLoop()
