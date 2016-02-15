#!/usr/bin/python
# -*- coding:utf-8 -*-
import wx
import core
import sys
from wx.lib.mixins.listctrl import CheckListCtrlMixin
try:
    from agw import ultimatelistctrl as ULC
except ImportError: # if it's not there locally, try the wxPython lib.
    from wx.lib.agw import ultimatelistctrl as ULC


class PhoneListCtrl(ULC.UltimateListCtrl):
    def __loadData(self):
        for i in range(0,10):
            cb = wx.CheckBox(self, -1, u"荣耀4X")
            cbb = wx.ComboBox(self, -1, value = '1', choices = ['10', '20', '40', '60', '80','100'], style = wx.CB_DROPDOWN|wx.TE_PROCESS_ENTER)
            index = self.InsertStringItem(sys.maxint, "")
            self.SetItemWindow(index, 0, cb, expand = True)
            self.SetStringItem(index, 1, "packagename")
            self.SetStringItem(index, 2, "packagenaddme")
            self.SetStringItem(index, 3, "packagenaddme")
            self.SetItemWindow(index, 4, cbb, expand = True)
            self.SetItemData(index , [cb,cbb])





    def __init__(self, parent, tid , id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style = ULC.ULC_MASK_TYPE, agwStyle = ULC.ULC_REPORT|ULC.ULC_HAS_VARIABLE_ROW_HEIGHT|ULC.ULC_HRULES|ULC.ULC_VRULES|ULC.ULC_NO_FULL_ROW_SELECT,
                 validator=wx.DefaultValidator, name="PhoneListCtrl"):
        super(PhoneListCtrl, self).__init__(parent, id, pos, size, style, agwStyle, validator, name)
        self.tid = tid
        self.InsertColumn(0, u"机型")
        self.InsertColumn(1, u"商标")
        self.InsertColumn(2, u"分辨率")
        self.InsertColumn(3, u"系统版本")
        #self.InsertColumn(3, u"MODEL")
        self.InsertColumn(4, u"数量")
        self.__loadData()
        self.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        self.SetColumnWidth(3, wx.LIST_AUTOSIZE)
        self.SetColumnWidth(4, wx.LIST_AUTOSIZE)

class PhonePanel(wx.Panel):
    def __init__(self, parent ,tid):
        wx.Panel.__init__(self, parent, -1)
        self.list = PhoneListCtrl(self ,tid)
        sizer = wx.BoxSizer()
        sizer.Add(self.list, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected, self.list)
        self.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.OnItemDeselected, self.list)
    def OnItemSelected(self, evt):
        pass
    def OnItemDeselected(self, evt):
        pass



class AppListCtrl(ULC.UltimateListCtrl):
    def __loadData(self):
        ret = core.Spy.getListForAndroid(self.tid)
        softlist = []
        if ret is not None:
            softlist = ret["softlist"]
            print softlist
        for soft in softlist:
            cb = wx.CheckBox(self, -1, soft["softname"])
            index =  self.InsertStringItem(sys.maxint ,"")
            self.SetItemWindow(index, 0, cb, expand = True)
            self.SetStringItem(index, 1, soft["packagename"])
            self.SetStringItem(index, 2, soft["versionName"])
            self.SetStringItem(index, 3, soft["description"])
            self.SetItemData(index , [cb])

    def __init__(self, parent, tid , id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style = ULC.ULC_MASK_TYPE, agwStyle = ULC.ULC_REPORT|ULC.ULC_HAS_VARIABLE_ROW_HEIGHT|ULC.ULC_HRULES|ULC.ULC_VRULES|ULC.ULC_NO_FULL_ROW_SELECT,
                 validator=wx.DefaultValidator, name="AppListCtrl"):
        super(AppListCtrl, self).__init__(parent, id, pos, size, style, agwStyle, validator, name)
        self.tid = tid
        self.InsertColumn(0, u"应用名")
        self.InsertColumn(1, u"包名")
        self.InsertColumn(2, u"版本")
        self.InsertColumn(3, u"描述")
        self.__loadData()
        self.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.SetColumnWidth(2, wx.LIST_AUTOSIZE)


class AppPanel(wx.Panel):
    def __init__(self, parent ,tid):
        wx.Panel.__init__(self, parent, -1)
        self.list = AppListCtrl(self ,tid)
        sizer = wx.BoxSizer()
        sizer.Add(self.list, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected, self.list)
        self.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.OnItemDeselected, self.list)
    def OnItemSelected(self, evt):
        pass
    def OnItemDeselected(self, evt):
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

