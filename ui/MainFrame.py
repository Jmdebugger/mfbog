#!/usr/bin/python
# -*- coding:utf-8 -*-
import wx
import core
import dialog

class ProportionalSplitter(wx.SplitterWindow):
        def __init__(self,parent, id = -1, proportion=0.66, size = wx.DefaultSize, **kwargs):
                super(ProportionalSplitter ,self).__init__(parent,id,wx.Point(0, 0),size, **kwargs)
                self.SetMinimumPaneSize(50) #the minimum size of a pane.
                self.proportion = proportion
                if not 0 < self.proportion < 1:
                        raise ValueError, "proportion value for ProportionalSplitter must be between 0 and 1."
                self.ResetSash()
                self.Bind(wx.EVT_SIZE, self.OnReSize)
                self.Bind(wx.EVT_SPLITTER_SASH_POS_CHANGED, self.OnSashChanged, id=id)
                ##hack to set sizes on first paint event
                self.Bind(wx.EVT_PAINT, self.OnPaint)
                self.firstpaint = True

        def SplitHorizontally(self, win1, win2):
                if self.GetParent() is None: return False
                return wx.SplitterWindow.SplitHorizontally(self, win1, win2,
                        int(round(self.GetParent().GetSize().GetHeight() * self.proportion)))

        def SplitVertically(self, win1, win2):
                if self.GetParent() is None: return False
                return wx.SplitterWindow.SplitVertically(self, win1, win2,
                        int(round(self.GetParent().GetSize().GetWidth() * self.proportion)))

        def GetExpectedSashPosition(self):
                if self.GetSplitMode() == wx.SPLIT_HORIZONTAL:
                        tot = max(self.GetMinimumPaneSize(),self.GetParent().GetClientSize().height)
                else:
                        tot = max(self.GetMinimumPaneSize(),self.GetParent().GetClientSize().width)
                return int(round(tot * self.proportion))

        def ResetSash(self):
                self.SetSashPosition(self.GetExpectedSashPosition())

        def OnReSize(self, event):
                "Window has been resized, so we need to adjust the sash based on self.proportion."
                self.ResetSash()
                event.Skip()

        def OnSashChanged(self, event):
                "We'll change self.proportion now based on where user dragged the sash."
                pos = float(self.GetSashPosition())
                if self.GetSplitMode() == wx.SPLIT_HORIZONTAL:
                        tot = max(self.GetMinimumPaneSize(),self.GetParent().GetClientSize().height)
                else:
                        tot = max(self.GetMinimumPaneSize(),self.GetParent().GetClientSize().width)
                self.proportion = pos / tot
                event.Skip()

        def OnPaint(self,event):
                if self.firstpaint:
                        if self.GetSashPosition() != self.GetExpectedSashPosition():
                                self.ResetSash()
                        self.firstpaint = False
                event.Skip()



class BrushTreeCtrl(wx.TreeCtrl):
    def __init__(self, *args, **kwargs):
        super(BrushTreeCtrl, self).__init__(*args, **kwargs)
        self.boss = core.Boss("Boss")
        bossItem = self.AddRoot(str(self.boss), data = wx.TreeItemData(self.boss))
        for phoneManager in self.boss.phoneManagers.values():
            pmItem = self.AppendItem(bossItem, str(phoneManager) , data = phoneManager)
            for phone in phoneManager.phones.values():
                phoneItem = self.AppendItem(pmItem , str(phone) , data = phone)
                for app in phone.apps:
                    appItem = self.AppendItem(phoneItem , str(app) , data = app)


class MainFrame(wx.Frame):
    ID_ADD_PHONE_MANAGER = 100
    def __initData(self):
        self.mBoss = core.Boss(u"boss")

    def OnSelChanged(self ,event):
        item = event.GetItem()
        data = self.mBrushTree.GetPyData(item)
        print type(data)

    def onSelPopupMenu(self ,event):
        id = event.GetId()
        if id == MainFrame.ID_ADD_PHONE_MANAGER:
            dlg = dialog.BossDialog(self , wx.ID_ANY , u"添加账号")
            dlg.Centre()
            ret = dlg.ShowModal()
            if ret == wx.ID_OK:
                print dlg.tcTid.GetValue()
            dlg.Destroy()

    def OnShowPopup(self ,event):
        data = self.mBrushTree.GetPyData(event.GetItem())
        popupMenu = wx.Menu()
        if isinstance(data , core.Boss):
            menuItem = wx.MenuItem(popupMenu,MainFrame.ID_ADD_PHONE_MANAGER, u"添加账号")
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
        self.mBottomRightPanel = wx.Panel (self.mSplit2)
        self.mBottomRightPanel.SetBackgroundColour('white')

        self.mSplit1.SplitVertically(self.mBrushTree, self.mSplit2)
        self.mSplit2.SplitHorizontally(self.mTopRightPanel, self.mBottomRightPanel)
        self.mStatusBar = self.CreateStatusBar()

    def __init__(self, *args, **kwargs):
        super(MainFrame, self).__init__(*args, **kwargs)
        self.__initData()
        self.__initView()
        self.Centre()
        self.Show(True)


if __name__ == "__main__":
    mainFrame = MainFrame()

