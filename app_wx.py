# -*- coding: utf-8 -*-

from os import name

import pretty_errors
import wx
from wx.core import MenuBar, Position, Size, Button

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

        self.initMenuBar()

        self.status_bar = self.CreateStatusBar()
        self.status_bar.SetFieldsCount(3)
        self.status_bar.SetStatusWidths([-1, -3, -1])

        self.createWidget()

        self.pushToStatusBar('Already', 0)

    # 创建部件

    def createWidget(self):

        func_size = [150, 100]
        size = wx.Size(func_size[0], func_size[1])
        self.panel_func_1 = wx.Panel(self, -1, size=size, pos=(10, 0))
        self.panel_func_2 = wx.Panel(self, -1, size=size, pos=(10, 100))
        self.panel_func_3 = wx.Panel(self, -1, size=size, pos=(10, 200))

        self.button_func_1 = wx.Button(
            self.panel_func_1, -1, label='功能1', size=size, pos=self.calculatePosPoint(func_size, func_size))
        self.button_func_2 = wx.Button(
            self.panel_func_2, -1, label='功能2', size=size, pos=self.calculatePosPoint(func_size, func_size))
        self.button_func_3 = wx.Button(self.panel_func_3, -1, label='功能3', size=size, pos=self.calculatePosPoint(func_size, func_size))

        self.Bind(wx.EVT_BUTTON, lambda msg: self.showMsgBox(
            '已开启功能1', '功能'), self.button_func_1)
        self.Bind(wx.EVT_BUTTON, lambda msg: self.showMsgBox(
            '已开启功能2', '功能'), self.button_func_2)
        self.Bind(wx.EVT_BUTTON, lambda msg: self.showMsgBox('已开启功能3', '功能'), self.button_func_3)

        self.button_func_1.SetDefault()
        self.button_func_2.SetDefault()
        self.button_func_3.SetDefault()

    # 在底部创建一个状态栏

    def initStatusBar(self):
        self.status_bar = self.CreateStatusBar()
        # 创建三个分栏
        self.status_bar.SetFieldsCount(3)
        # 设置分栏宽度
        self.status_bar.SetStatusWidths([-1, -3, -1])

    # 创建菜单栏

    def initMenuBar(self):

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
        # lambda vars: function(vars) -> 做到响应传参函数
        # 菜单栏 点击 事件
        self.Bind(wx.EVT_MENU, lambda msg: self.showMsgBox(
            "opened"), item_open)
        self.Bind(wx.EVT_MENU, lambda msg: self.showMsgBox("saved"), item_save)
        self.Bind(wx.EVT_MENU, lambda msg: self.showMsgBox(
            "Editing"), item_edit)

    def splitStr(self, text):
        return text.split('-')

    # 在状态栏里推送消息

    def pushToStatusBar(self, text, num):
        self.status_bar.SetStatusText(text, num)

    def showMsgBox(self, msg, title='MsgDialog'):

        msg_box = wx.MessageDialog(
            self, msg, title, wx.YES_NO | wx.ICON_QUESTION)
        if msg_box.ShowModal() == wx.ID_YES:
            msg_box.Destroy()

    def calculatePosPoint(self, bigger, smaller):
        point = [int((bigger[0]-smaller[0])/2), int((bigger[1]-smaller[1])/2)]
        return wx.Point(point[0], point[1])


class Box(wx.Frame):

    def __init__(self, *args, **kw):
        super(Box, self).__init__(*args, **kw)


if __name__ == "__main__":

    # 设备显示器信息
    sys_windows_size = [1920, 1080]
    # 主窗口大小	像素
    main_frame_size = [900, 600]
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
