# -*- coding: utf-8 -*-

from os import name

import pretty_errors
import wx
from wx.core import MenuBar, Position, Size

menu_title = {
    1:
        {
            1: "打开-打开一个文件",
            2: "保存-保存当前文件",
        },
    2:
        {
            1: "编辑-编辑",
        },
}


class MainFrame(wx.Frame):

    def __init__(self, *args, **kw):
        super(MainFrame, self).__init__(*args, **kw)

        self.createMenuBar()
        # 在底部创建一个状态栏
        self.CreateStatusBar()

        self.pushToStatusBar('Already')

    def createWidget(self):

        panel = wx.Panel()

        panel_str = wx.StaticText(panel, label="panel")

    # 创建菜单栏

    def createMenuBar(self):
        
        # wx.Menu.Append()
        # params:helpString -> 提示信息 显示在状态栏

        file_menu = wx.Menu()
        item_open = file_menu.Append(-1, self.splitStr(menu_title[1][1])[
                                     0], self.splitStr(menu_title[1][1])[1])
        item_save = file_menu.Append(-1, self.splitStr(menu_title[1][2])[
                                     0], self.splitStr(menu_title[1][2])[1])

        option_menu = wx.Menu()
        item_edit = option_menu.Append(-1, self.splitStr(menu_title[2][1])[
                                       0], self.splitStr(menu_title[2][1])[1])

        menubar = wx.MenuBar()

        menubar.Append(file_menu, "文件")
        menubar.Append(option_menu, "操作")

        self.SetMenuBar(menubar)

        # 绑定事件
        self.Bind(wx.EVT_MENU, lambda event: self.menuOpenEvt(event), item_open)
        self.Bind(wx.EVT_MENU, lambda event: self.menuSaveEvt(event), item_save)
        self.Bind(wx.EVT_MENU, lambda event: self.menuEditEvt(event), item_edit)

    def splitStr(self, text):
        return text.split('-')

    # 在状态栏里推送消息

    def pushToStatusBar(self, text):
        self.PushStatusText(text)

    # 菜单栏 Open 事件
    def menuOpenEvt(self, event):
        msg = "Opened"
        self.showMsgBox(msg)

    # 菜单栏 Save 事件
    def menuSaveEvt(self, event):
        msg = "Saved"
        self.showMsgBox(msg)

    # 菜单栏 Edit 事件
    def menuEditEvt(self, event):
        msg = "Edited"
        self.showMsgBox(msg)

    def showMsgBox(self, text):

        msg_box = wx.MessageDialog(
            self, text, 'MsgDialog', wx.YES_NO | wx.ICON_QUESTION)
        if msg_box.ShowModal() == wx.ID_YES:
            msg_box.Destroy()


class Box(wx.Frame):

    def __init__(self, *args, **kw):
        super(Box, self).__init__(*args, **kw)


if __name__ == "__main__":

    # 设备显示器信息
    sys_windows_size = [1920, 1080]
    # 主窗口大小	像素
    main_frame_size = [500, 350]
    # 主窗口位置	像素
    main_frame_pos = [int((sys_windows_size[0]-main_frame_size[0])/2),
                      int((sys_windows_size[1]-main_frame_size[1])/2)]

    # 主窗口的大小-<-赋值
    main_size = wx.Size(int(main_frame_size[0]), int(main_frame_size[1]))
    # 主窗口的位置-<-赋值
    main_pos = wx.Point(main_frame_pos[0], main_frame_pos[1])

    app = wx.App()
    frame = MainFrame(None, title="My App", size=main_size,
                      pos=main_pos, name='mainFrame')

    frame.Show()
    app.MainLoop()
