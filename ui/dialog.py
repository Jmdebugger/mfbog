#!/usr/bin/python
# -*- coding:utf-8 -*-
import wx
from ctrl import PhonePanel
from ctrl import AppPanel


class BossDialog(wx.Dialog):
    def __init__(self, parent, id, title):
        super(BossDialog, self).__init__(parent, id, title, wx.DefaultPosition, wx.Size(300, 200))
        wx.StaticText(self, -1, u'账号', (20, 20))
        self.tcTid = wx.TextCtrl(self, -1, "", (70, 20), wx.Size(150, 20))
        wx.StaticText(self, -1, u'备注', (20, 60))
        self.tcName = wx.TextCtrl(self, -1, "", (70, 60), wx.Size(150, 20))
        self.btnYes = wx.Button(self, wx.ID_OK, u"确定", (100, 120))
        self.btnNo = wx.Button(self, wx.ID_CANCEL, u"取消", (200, 120))
        self.Bind(wx.EVT_BUTTON, self.onOK, self.btnYes)

    def checkTid(self, tid):
        return True

    def onOK(self, event):
        if self.checkTid(self.tcTid.GetValue):
            self.EndModal(wx.ID_OK)
        else:
            wx.MessageBox(u"请输入正确的账号！", u"错误")


class PhoneManagerDialog(wx.Dialog):
    def __init__(self, parent, id, title, tid):
        super(PhoneManagerDialog, self).__init__(parent, id, title, wx.DefaultPosition, wx.Size(900, 700))
        self.tid = tid
        hBoxSizer = wx.BoxSizer(wx.HORIZONTAL)
        vBoxSizer = wx.BoxSizer(wx.VERTICAL)
        self.appPanel = AppPanel(self, tid)
        self.phonePanel = PhonePanel(self, tid)
        rightPanel = wx.Panel(self)

        wx.StaticText(rightPanel, -1, u'代理IP设置', pos=(5, 5))
        cbb = wx.ComboBox(rightPanel, -1, value='192.168.1.1', choices=['192.168.1.2'],
                          style=wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER, pos=(5, 25) )
        wx.StaticText(rightPanel, -1, u'用户名', pos = (5, 60))
        self.tcUserName = wx.TextCtrl(rightPanel, -1, "", pos = (70, 60), size = wx.Size(150, 20))
        wx.StaticText(rightPanel, -1, u'密码', (5, 80))
        self.tcPassword = wx.TextCtrl(rightPanel, -1, "", pos = (70, 80), size =wx.Size(150, 20))
        wx.StaticLine(rightPanel ,pos = (0, 120) ,size = wx.Size(300 ,1))

        self.btnYes = wx.Button(rightPanel, wx.ID_OK, u"确定", pos = (100, 125))
        self.btnNo = wx.Button(rightPanel, wx.ID_CANCEL, u"取消",pos =  (200, 125))
        vBoxSizer.Add(self.phonePanel, 1, wx.EXPAND)
        vBoxSizer.Add(self.appPanel, 1, wx.EXPAND)
        hBoxSizer.Add(vBoxSizer, 3, wx.EXPAND)
        hBoxSizer.Add(rightPanel, 1, wx.EXPAND)

        self.SetSizer(hBoxSizer)


if __name__ == "__main__":

    app = wx.App()
    pmDlg = PhoneManagerDialog(None, wx.ID_ANY, u"安装", 12345678)
    pmDlg.Centre()
    ret = pmDlg.ShowModal()
    if ret == wx.ID_OK:
        print pmDlg.tcTid.GetValue()
    pmDlg.Destroy()

    app.MainLoop()

    """
    app = wx.App()
    bossDlg = BossDialog(None , -1 , u"添加账号")
    bossDlg.Centre()
    ret = bossDlg.ShowModal()
    if ret == wx.ID_OK:
        print bossDlg.tcTid.GetValue()
    bossDlg.Destroy()

    app.MainLoop()
    """
