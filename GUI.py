# -*- coding: UTF-8 -*- 
# 创建人：LeK
# 创建日期：2022/3/31

import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title='TEST', pos=(200, 300), size=(600, 300))
        self.panel = wx.Panel(self)
        self.title = wx.StaticText(self.panel, label='TEST TEST', pos=(80, 20))
        self.font = wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL,
                            wx.FONTENCODING_DEFAULT)
        self.title.SetFont(self.font)
        self.label_user = wx.StaticText(self.panel, label='user:', pos=(30, 60))
        self.label_pwd = wx.StaticText(self.panel, label='pwd:', pos=(30, 90))
        self.text_user = wx.TextCtrl(self.panel, pos=(70, 60), size=(200, 20), style=wx.TE_LEFT)
        self.text_pwd = wx.TextCtrl(self.panel, pos=(70, 90), size=(200, 20), style=wx.TE_PASSWORD)
        self.bt_confirm = wx.Button(self.panel, label='确认', pos=(70, 130))
        self.bt_cancel = wx.Button(self.panel, label='取消', pos=(170, 130))

        self.hsizer_user = wx.BoxSizer(wx.HORIZONTAL)
        self.hsizer_pwd = wx.BoxSizer(wx.HORIZONTAL)
        self.hsizer_bt = wx.BoxSizer(wx.HORIZONTAL)
        self.vsizer = wx.BoxSizer(wx.VERTICAL)

        self.hsizer_user.Add(self.label_user, proportion=0, flag=wx.LEFT, border=5)
        self.hsizer_user.Add(self.text_user, proportion=0, flag=wx.LEFT, border=5)
        self.hsizer_pwd.Add(self.label_pwd, proportion=0, flag=wx.LEFT | wx.TOP, border=5)
        self.hsizer_pwd.Add(self.text_pwd, proportion=0, flag=wx.LEFT, border=5)
        self.hsizer_bt.Add(self.bt_confirm, proportion=0, flag=wx.LEFT, border=30)
        self.hsizer_bt.Add(self.bt_cancel, proportion=0, flag=wx.LEFT, border=25)

        self.vsizer.Add(self.title, proportion=0, flag=wx.TOP | wx.ALIGN_CENTER | wx.LEFT, border=20)
        self.vsizer.Add(self.hsizer_user, proportion=0, flag=wx.TOP | wx.ALIGN_CENTER, border=10)
        self.vsizer.Add(self.hsizer_pwd, proportion=0, flag=wx.TOP | wx.ALIGN_CENTER, border=5)
        self.vsizer.Add(self.hsizer_bt, proportion=0, flag=wx.TOP | wx.ALIGN_CENTER, border=15)

        self.panel.SetSizer(self.vsizer)


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
