import wx

class AppListCtrl(wx.ListCtrl):
    def __init__(self, parent):
        super(AppListCtrl, self).__init__(parent, style=wx.LC_REPORT)

        # Attributes
        self._il = wx.ImageList(16, 16)

        # Setup Image List
        bmp = wx.ArtProvider.GetBitmap(wx.ART_INFORMATION, wx.ART_MENU, (16,16))
        img_idx = self._il.Add(bmp)
        self.SetImageList(self._il, wx.IMAGE_LIST_SMALL)

        # Setup ListCtrl
        self.InsertColumn(0, "Column One")
        self.InsertColumn(1, "Column two")

        # Add Some items to the ListCtrl
        for x in range(10):
            self.Append(("ListCtrl Item #%d" % x,"ListCtrl Item #%d" % (x+1)))
            print self.GetItemCount()
            self.SetItemImage(self.GetItemCount()-1, img_idx)

class MyFrame(wx.Frame):
    def __init__(self, parent):
        super(MyFrame, self).__init__(parent, title="ListCtrl with Icons")

        # Attributes
        self._list = AppListCtrl(self)

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None)
        self.frame.Show()
        return True

if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
