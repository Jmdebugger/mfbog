#!/usr/bin/python
# -*- coding:utf-8 -*-
import wx
import core
import dialog
import wx.html2
from ctrl import *

ID_ADD_PHONE_MANAGER = 100
ID_ADD_PHONE = 101


class MainFrame(wx.Frame):
    def __initData(self):
        pass

    def OnSelChanged(self ,event):
        item = event.GetItem()
        data = self.mBrushTree.GetPyData(item)
        print type(data)

    def onSelPopupMenu(self ,event):
        id = event.GetId()
        if id == ID_ADD_PHONE_MANAGER:
            dlg = dialog.BossDialog(self , wx.ID_ANY , u"添加账号")
            dlg.Centre()
            ret = dlg.ShowModal()
            if ret == wx.ID_OK:
                tid = dlg.tcTid.GetValue()
                name = dlg.tcName.GetValue()
                self.mBrushTree.addPhoneManager(tid ,name)
            dlg.Destroy()
        elif id == ID_ADD_PHONE:
            pass

    def OnShowPopup(self ,event):
        data = self.mBrushTree.GetPyData(event.GetItem())
        popupMenu = wx.Menu()
        if isinstance(data , core.Boss):
            menuItem = wx.MenuItem(popupMenu,ID_ADD_PHONE_MANAGER, u"添加账号")
        elif isinstance(data ,core.PhoneManager):
            menuItem = wx.MenuItem(popupMenu,ID_ADD_PHONE, u"添加手机")

        popupMenu.AppendItem(menuItem)
        self.Bind(wx.EVT_MENU, self.onSelPopupMenu ,menuItem )
        self.mBrushTree.PopupMenu(popupMenu, event.GetPoint())
        popupMenu.Destroy()

    def __initView(self):
        self.mSplit1 = ProportionalSplitter(self,-1, 0.3)
        self.mSplit2 = ProportionalSplitter(self.mSplit1,-1, 0.7)

        self.mBrushTree = BrushTreeCtrl(self.mSplit1 , wx.ID_ANY)
        self.mBrushTree.SetBackgroundColour('gray')
        self.mBrushTree.Bind(wx.EVT_TREE_SEL_CHANGED , self.OnSelChanged)
        self.mBrushTree.Bind(wx.EVT_TREE_ITEM_RIGHT_CLICK, self.OnShowPopup)
        self.mTopRightPanel = wx.Panel (self.mSplit2)
        self.mTopRightPanel.SetBackgroundColour('white')
        self.mNotificationPanel = NotificationPanel(self.mSplit2)

        self.mSplit1.SplitVertically(self.mBrushTree, self.mSplit2)
        self.mSplit2.SplitHorizontally(self.mTopRightPanel, self.mNotificationPanel)
        self.mStatusBar = self.CreateStatusBar()

    def __init__(self, *args, **kwargs):
        super(MainFrame, self).__init__(*args, **kwargs)
        self.__initData()
        self.__initView()
        self.Centre()
        self.Show(True)


if __name__ == "__main__":
    mainFrame = MainFrame()

