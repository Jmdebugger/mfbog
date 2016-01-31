#!/usr/bin/python
# -*- coding:utf-8 -*-
import wx
import core

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
        self.mBoss = core.Boss("Boss")
        root = self.AddRoot(self.mBoss.mName, data = wx.TreeItemData(self.mBoss))
        for phoneManager in self.mBoss.mPhoneManagers:
            pm = self.AppendItem(root, phoneManager.tid , data = phoneManager)
            for phone in pm.m

        os = self.AppendItem(root, 'Operating Systems')
        pl = self.AppendItem(root, 'Programming Languages')
        tk = self.AppendItem(root, 'Toolkits')
        self.AppendItem(os, 'Linux')
        self.AppendItem(os, 'FreeBSD')
        self.AppendItem(os, 'OpenBSD')
        self.AppendItem(os, 'NetBSD')
        self.AppendItem(os, 'Solaris')
        cl = self.AppendItem(pl, 'Compiled languages')
        sl = self.AppendItem(pl, 'Scripting languages')
        self.AppendItem(cl, 'Java')
        self.AppendItem(cl, 'C++')
        self.AppendItem(cl, 'C')
        self.AppendItem(cl, 'Pascal')
        self.AppendItem(sl, 'Python')
        self.AppendItem(sl, 'Ruby')
        self.AppendItem(sl, 'Tcl')
        self.AppendItem(sl, 'PHP')
        self.AppendItem(tk, 'Qt')
        self.AppendItem(tk, 'MFC')
        self.AppendItem(tk, 'wxPython')
        self.AppendItem(tk, 'GTK+')
        self.AppendItem(tk, 'Swing')

class MainFrame(wx.Frame):
    def __initData(self):
        self.mBoss = core.Boss(u"boss")

    def OnSelChanged(self ,event):
        item = event.GetItem()
        print self.mBrushTree.GetItemText(item)

    def onSelPopupMenu(self ,event):
        item = event.GetItem()
        print self.mBrushTree.GetItemText(item)

    def OnShowPopup(self ,event):
        item = event.GetItem()
        print self.mBrushTree.GetItemText(item)
        popupMenu = wx.Menu()
        for text in "Add Delete Edit".split():
            item = popupMenu.Append(-1, text)
        self.mBrushTree.Bind(wx.EVT_MENU, self.onSelPopupMenu)
        self.mBrushTree.PopupMenu(popupMenu, event.GetPoint())
        popupMenu.Destroy()

    def __initView(self):
        self.mSplit1 = ProportionalSplitter(self,-1, 0.3)
        self.mSplit2 = ProportionalSplitter(self.mSplit1,-1, 0.7)

        self.mBrushTree = BrushTreeCtrl(self.mSplit1 , 1)
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

