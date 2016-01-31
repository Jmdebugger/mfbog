#!/usr/bin/python
# -*- coding:utf-8 -*-
import wx
class BossDialog(wx.Dialog):
    def __init__(self,parent, id, title):
        super(BossDialog, self).__init__(parent, id, title, wx.DefaultPosition, wx.Size(300, 200))
        wx.StaticText(self, -1, u'账号', (20,20))
        self.tcTid  = wx.TextCtrl(self , -1 , "" , (70,20) , wx.Size(150 ,20))
        wx.StaticText(self, -1, u'备注', (20,60))
        self.tcName  = wx.TextCtrl(self , -1 , "" , (70,60) , wx.Size(150 ,20))
        self.btnYes = wx.Button(self ,wx.ID_OK , u"确定" , (100 ,120))
        self.btnNo = wx.Button(self , wx.ID_CANCEL , u"取消" ,(200,120))
        self.Bind(wx.EVT_BUTTON , self.onOK ,self.btnYes)

    def checkTid(self ,tid):
        return True

    def onOK(self ,event):
        if self.checkTid(self.tcTid.GetValue):
            self.EndModal(wx.ID_OK)
        else:
            wx.MessageBox(u"请输入正确的账号！" , u"请输入正确的账号！")

class PhoneManagerDialog(wx.Dialog):
    pass


if __name__ == "__main__":
    app = wx.App()
    bossDlg = BossDialog(None , -1 , u"添加账号")
    bossDlg.Centre()
    ret = bossDlg.ShowModal()
    if ret == wx.ID_OK:
        print bossDlg.tcTid.GetValue()
    bossDlg.Destroy()

    app.MainLoop()

