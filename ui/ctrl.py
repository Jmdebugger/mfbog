#!/usr/bin/python
# -*- coding:utf-8 -*-
import wx
import core


class AppListCtrl(wx.ListCtrl):
    def __init__(self, tid , *args, **kwargs):
        super(AppListCtrl, self).__init__(*args, **kwargs)
        ret = core.Spy.getListForAndroid(tid)
        softlist = []
        if ret is not None:
            softlist = ret["softlist"]












class PhoneListCtrl(wx.ListCtrl):
    pass



class NotificationPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.mBrowser = wx.html2.WebView.New(self)
        self.mBrowser.LoadURL("http://www.baidu.com")
        sizer.Add(self.mBrowser ,1 , wx.EXPAND)
        self.SetSizer(sizer)


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
        self.bossItem = self.AddRoot(unicode(self.boss), data = wx.TreeItemData(self.boss))
        self.boss.item = self.bossItem
        for phoneManager in self.boss.phoneManagers.values():
            pmItem = self.AppendItem(self.bossItem, unicode(phoneManager) , data = wx.TreeItemData(phoneManager))
            phoneManager.item = pmItem
            for phone in phoneManager.phones.values():
                phoneItem = self.AppendItem(pmItem , unicode(phone) , data = wx.TreeItemData(phone))
                phone.item = phoneItem
                for app in phone.apps:
                    appItem = self.AppendItem(phoneItem , unicode(app) , data = wx.TreeItemData(app))
                    app.item = appItem

    def addPhoneManager(self ,tid , name):
        pm = self.boss.addPhoneManager(tid , name)
        if pm.item == None:
            pmItem = self.AppendItem(self.bossItem ,unicode(pm) , data = wx.TreeItemData(pm))
            pm.item = pmItem
        else:
            wx.MessageBox( u"账号已经存在！",u"错误" )



    def addPhone(self , pmItem , phone):
        pass

