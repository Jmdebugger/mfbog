import wx

class PackageTree(wx.TreeCtrl):
    def __init__(self, parent, *args, **kwargs):
        super(PackageTree, self).__init__(parent, style=wx.TR_DEFAULT_STYLE|wx.TR_HIDE_ROOT)

        self.Bind(wx.EVT_TREE_ITEM_RIGHT_CLICK, self.OnShowPopup)
        self.root = self.AddRoot('')
        self.SetItemHasChildren(self.root, True)

        self.node1 = self.AppendItem(self.root, 'Node 1')
        self.node2 = self.AppendItem(self.root, 'Node 2')
        self.SetItemHasChildren(self.node2, True)
        self.node3 = self.AppendItem(self.node2, 'Node 3')

    def OnShowPopup(self, event):
        self.popupmenu = wx.Menu()
        for text in "Add Delete Edit".split():
            item = self.popupmenu.Append(-1, text)
            self.Bind(wx.EVT_MENU, self.onSelectContext)
        self.PopupMenu(self.popupmenu, event.GetPoint())
        self.popupmenu.Destroy()

    def onSelectContext(self, event):
        item = self.popupmenu.FindItemById(event.GetId())
        text = item.GetText()
        print "Select context: %s" % item.GetText()

    def CreateContextMenu(self, menu):
        item = self._menu.Append(wx.ID_ADD)
        self.Bind(wx.EVT_MENU, self.onSelectContext, item)
        item = self._menu.Append(wx.ID_DELETE)
        self.Bind(wx.EVT_MENU, self.onSelectContext, item)
        item = self._menu.Append(wx.ID_EDIT)
        self.Bind(wx.EVT_MENU, self.onSelectContext, item)

class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MainFrame, self).__init__(*args, **kwargs)

        self.panel = wx.Panel(self)
        self.tree = PackageTree(self.panel)
        self.text = wx.TextCtrl(self.panel)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.tree, 1, wx.EXPAND)
        sizer.Add(self.text, 2, wx.EXPAND)
        self.panel.SetSizer(sizer)

        self.panel.Fit()
        self.SetInitialSize()

class App(wx.App):
    def __init__(self):
        super(App, self).__init__(redirect=False)
        MainFrame(None, title='Test').Show()

App().MainLoop()