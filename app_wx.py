# -*- coding: utf-8 -*-

from os import name
import string
import json
import pretty_errors
import time
import wx
from wx.core import MenuBar, Position, Size, Button

import mi_motion

# menu_title = {
#     1:
#         {
#             'name': "登录",
#             'more': ["登录-", "重新登录-"]
#         },
#     2:
#         {
#             'name': "选项",
#             'more': ["更多选项-"]
#         },
# }


class MainFrame(wx.Frame):

    def __init__(self, *args, **kw):
        super(MainFrame, self).__init__(*args, **kw)

        self.initMenuBar()

        self.status_bar = self.CreateStatusBar()
        self.status_bar.SetFieldsCount(3)
        self.status_bar.SetStatusWidths([-1, -3, -1])

        # self.font_text = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, False, '', wx.FONTENCODING_DEFAULT)

        self.createWidget()

        self.pushToStatusBar('Already', 0)

    # 创建部件

    def createWidget(self):

        func_size = [180, 80]

        size = wx.Size(func_size[0], func_size[1])

        panel_func_1 = wx.Panel(self, -1, size=size, pos=(10, 10))
        panel_func_2 = wx.Panel(self, -1, size=size, pos=(10, func_size[1]+10))
        panel_func_3 = wx.Panel(self, -1, size=size,
                                pos=(10, func_size[1]*2+10))
        mi_mition_panel = wx.Panel(
            self, -1, size=size, pos=(10, func_size[1]*3+10))

        self.button_func_1 = wx.Button(
            panel_func_1, -1, label='功能1', size=panel_func_1.GetSize(), pos=self.calculatePosPoint(func_size, func_size))
        self.button_func_2 = wx.Button(
            panel_func_2, -1, label='功能2', size=panel_func_2.GetSize(), pos=self.calculatePosPoint(func_size, func_size))
        self.button_func_3 = wx.Button(
            panel_func_3, -1, label='功能3', size=panel_func_3.GetSize(), pos=self.calculatePosPoint(func_size, func_size))
        self.mi_motion_button = wx.Button(
            mi_mition_panel, -1, label='小米运动', size=mi_mition_panel.GetSize(), pos=self.calculatePosPoint(func_size, func_size))

        self.button_func_1.SetDefault()
        self.button_func_2.SetDefault()
        self.button_func_3.SetDefault()
        self.mi_motion_button.SetDefault()

        panel_text = wx.Panel(self, size=(600, 400), pos=(266, 10))
        self.text = wx.TextCtrl(
            panel_text, -1, value='', pos=(0, 0), size=panel_text.GetSize(), style=wx.TE_READONLY | wx.TE_MULTILINE)
        # self.text.SetFont(self.font_text)

        self.Bind(wx.EVT_BUTTON, lambda text: self.pushText(
            'text'), self.button_func_1)
        self.Bind(wx.EVT_BUTTON, lambda msg: self.showMsgBox(
            '已开启功能2', '功能'), self.button_func_2)
        self.Bind(wx.EVT_BUTTON, lambda msg: self.showMsgBox(
            '已开启功能3', '功能'), self.button_func_3)
        self.Bind(wx.EVT_BUTTON, lambda param: self.miMotion(
            0), self.mi_motion_button)

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
        # 子选项命名
        item_open = file_menu.Append(-1, self.splitStr(menu_title['1']['more'][0])[
                                     0], self.splitStr(menu_title['1']['more'][0])[1])
        item_save = file_menu.Append(-1, self.splitStr(menu_title['1']['more'][1])[
                                     0], self.splitStr(menu_title['1']['more'][1])[1])

        option_menu = wx.Menu()
        item_edit = option_menu.Append(-1, self.splitStr(menu_title['2']['more'][0])[
                                       0], self.splitStr(menu_title['2']['more'][0])[1])

        menubar = wx.MenuBar()

        # 菜单选项命名
        menubar.Append(file_menu, menu_title['1']['name'])
        menubar.Append(option_menu, menu_title['2']['name'])

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

    def pushText(self, text):
        self.text.AppendText(f"{text}\n")

    def miMotion(self, param):
        if param is param:
            self.pushText(f"{self.getTime()} {self.mi_motion_button.GetLabelText()}正在执行...")
            mi_motion.MAIN()
            self.pushText(f"{self.getTime()} {self.mi_motion_button.GetLabelText()}执行完成...")

    def getTime(self):
        # 年月日
        today = time.strftime("%F")

        Year = int(time.strftime('%Y'))
        Month = int(time.strftime('%m'))
        Day = int(time.strftime('%d'))

        # 时分秒
        Hour = int(time.strftime('%H'))
        Minute = int(time.strftime('%M'))
        Second = int(time.strftime('%S'))

        now = f'[{Year}-{Month}-{Day} {Hour}:{Minute}:{Second}]'

        return now


class funcFrame(wx.Frame):

    def __init__(self, *args, **kw):
        super(funcFrame, self).__init__(*args, **kw)


if __name__ == "__main__":

    with open("./config.json", 'r', encoding='utf-8') as f:
        # json.dump(menu_title, f, ensure_ascii=False)
        menu_title = json.load(f)

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
