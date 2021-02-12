# -*- coding: utf-8 -*-

from os import name
import string
import json
import time
import wx
from wx.core import MenuBar, Position, Size, Button

import pretty_errors
import mi_motion
import RSA


menu_title = {
    "main": {
        "name": "界面",
        "more": ["主界面-主界面"]
    },
    "login": {
        "name": "登录",
        "more": ["登录-登录", "重新登录-重新登录"]
    },
    "software": {
        "name": "软件",
        "more": ["酷安-酷安", "豌豆荚-豌豆荚", "吾爱论坛-吾爱论坛"]
    },
    "more": {
        "name": "更多选项",
        "more": ["更多选项-更多选项"]
    }
}


class MainFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MainFrame, self).__init__(*args, **kw)

        self.initMenuBar()

        self.status_bar = self.CreateStatusBar()
        self.status_bar.SetFieldsCount(3)
        self.status_bar.SetStatusWidths([-1, -2, -1])

        # self.outputTextPanel = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, False, '', wx.FONTENCODING_DEFAULT)

        # self.createWidget()

        self.pushToStatusBar('Already', 0)

    def creatFrame(self):
        self.new_frame = funcFrame()

    # 创建部件

    def createWidget(self):

        buttonBoxSize = [120, 50]

        size = wx.Size(buttonBoxSize[0], buttonBoxSize[1])

        functionPanel1 = wx.Panel(self, -1, size=size, pos=(10, 10))
        functionPanel2 = wx.Panel(self,
                                  -1,
                                  size=size,
                                  pos=(10, buttonBoxSize[1] + 10))
        functionPanel3 = wx.Panel(self,
                                  -1,
                                  size=size,
                                  pos=(10, buttonBoxSize[1] * 2 + 10))
        miMitionPanel = wx.Panel(self,
                                 -1,
                                 size=size,
                                 pos=(10, buttonBoxSize[1] * 3 + 10))

        self.functionBotton1 = wx.Button(functionPanel1,
                                         -1,
                                         label='获取时间',
                                         size=functionPanel1.GetSize(),
                                         pos=self.calculatePosPoint(
                                             buttonBoxSize, buttonBoxSize))
        self.functionButton2 = wx.Button(functionPanel2,
                                         -1,
                                         label='加密',
                                         size=functionPanel2.GetSize(),
                                         pos=self.calculatePosPoint(
                                             buttonBoxSize, buttonBoxSize))
        self.functionButton3 = wx.Button(functionPanel3,
                                         -1,
                                         label='功能3',
                                         size=functionPanel3.GetSize(),
                                         pos=self.calculatePosPoint(
                                             buttonBoxSize, buttonBoxSize))
        self.miMotionButton = wx.Button(miMitionPanel,
                                        -1,
                                        label='小米运动',
                                        size=miMitionPanel.GetSize(),
                                        pos=self.calculatePosPoint(
                                            buttonBoxSize, buttonBoxSize))

        self.functionBotton1.SetDefault()
        self.functionButton2.SetDefault()
        self.functionButton3.SetDefault()
        self.miMotionButton.SetDefault()

        inputTextPanel = wx.Panel(self, size=(300, 60), pos=(266, 10))
        self.inputText = wx.TextCtrl(inputTextPanel, -1, value='', pos=(
            0, 0), size=inputTextPanel.GetSize(), style=wx.TE_MULTILINE)

        outputTextPanel = wx.Panel(self, size=(315, 200), pos=(266, 100))
        self.outputText = wx.TextCtrl(outputTextPanel,
                                      -1,
                                      value='',
                                      pos=(0, 0),
                                      size=outputTextPanel.GetSize(),
                                      style=wx.TE_READONLY | wx.TE_MULTILINE)
        # outputTextPanel.SetFont(self.outputTextPanel)

        self.Bind(wx.EVT_BUTTON,
                  lambda msg: self.pushText(self.outputText, self.getTime()),
                  self.functionBotton1)
        self.Bind(wx.EVT_BUTTON, lambda msg: self.RSAEncDec(
            self.inputText.GetValue()), self.functionButton2)
        self.Bind(wx.EVT_BUTTON, lambda msg: self.showMsgBox('已开启功能3', '功能'),
                  self.functionButton3)
        self.Bind(wx.EVT_BUTTON, lambda param: self.miMotion('param'),
                  self.miMotionButton)

    # 在底部创建一个状态栏

    def initStatusBar(self):
        self.status_bar = self.CreateStatusBar()
        # 创建三个分栏
        self.status_bar.SetFieldsCount(3)
        # 设置分栏宽度
        self.status_bar.SetStatusWidths([-1, -2, -1])

    # 创建菜单栏

    def initMenuBar(self):

        # wx.Menu.Append()
        # params:helpString -> 提示信息 显示在状态栏

        # 主菜单栏
        main_menu = wx.Menu()

        # 子选项命名
        frame_1_str = self.splitStr(menu_title['main']['more'][0])
        frame_1_item = main_menu.Append(-1, frame_1_str[0], frame_1_str[1])
        # 登录菜单栏
        login_menu = wx.Menu()
        # 子选项命名
        login_str = self.splitStr(menu_title['login']['more'][0])
        login_item = login_menu.Append(-1, login_str[0], login_str[1])

        re_login_str = self.splitStr(menu_title['login']['more'][1])
        reLogin_item = login_menu.Append(-1, re_login_str[0], re_login_str[1])
        # 软件菜单栏
        soft_menu = wx.Menu()
        # 子选项命名
        kuAn_str = self.splitStr(menu_title['software']['more'][0])
        kuAn_item = soft_menu.Append(-1, kuAn_str[0], kuAn_str[1])

        wanDouJia_str = self.splitStr(menu_title['software']['more'][1])
        wanDouJia_item = soft_menu.Append(-1, wanDouJia_str[0],
                                          wanDouJia_str[1])

        wu2_str = self.splitStr(menu_title['software']['more'][2])
        wu2_item = soft_menu.Append(-1, wu2_str[0], wu2_str[1])
        # 更多菜单栏
        more_menu = wx.Menu()
        # 子选项命名
        more_str = self.splitStr(menu_title['more']['more'][0])
        more_item = more_menu.Append(-1, more_str[0], more_str[1])

        menubar = wx.MenuBar()

        # 菜单选项命名
        menubar.Append(main_menu, menu_title['main']['name'])
        menubar.Append(login_menu, menu_title['login']['name'])
        menubar.Append(soft_menu, menu_title['software']['name'])
        menubar.Append(more_menu, menu_title['more']['name'])

        self.SetMenuBar(menubar)

        # 绑定事件
        # lambda vars: function(vars) -> 做到响应传参函数
        # 菜单栏 点击 事件
        # main Menu
        # self.Bind(wx.EVT_MENU, lambda msg: self.createWidget(), main_menu)
        self.Bind(wx.EVT_MENU, lambda msg: self.createWidget(), frame_1_item)
        # Login Menu
        self.Bind(wx.EVT_MENU, lambda msg: self.creatFrame(), login_item)
        self.Bind(wx.EVT_MENU, lambda msg: self.showMsgBox("RELOGIN"),
                  reLogin_item)
        # software Menu
        self.Bind(wx.EVT_MENU, lambda msg: self.showMsgBox("酷安"), kuAn_item)
        self.Bind(wx.EVT_MENU, lambda msg: self.showMsgBox("豌豆荚"),
                  wanDouJia_item)

    def splitStr(self, text):
        # return title, desp
        return text.split('-')

    # 在状态栏里推送消息

    def pushToStatusBar(self, text, num):
        self.status_bar.SetStatusText(text, num)

    def showMsgBox(self, msg, title='MsgDialog'):

        msg_box = wx.MessageDialog(self, msg, title,
                                   wx.YES_NO | wx.ICON_QUESTION)
        if msg_box.ShowModal() == wx.ID_YES:
            msg_box.Destroy()

    def calculatePosPoint(self, bigger, smaller):
        point = [
            int((bigger[0] - smaller[0]) / 2),
            int((bigger[1] - smaller[1]) / 2)
        ]
        return wx.Point(point[0], point[1])

    def pushText(self, Panel, text):
        Panel.AppendText(f"{text}\n")

    # 外部小功能

    def miMotion(self, param):
        if param is param:
            self.pushText(self.outputText,
                          f"{self.getTime()} {self.miMotionButton.GetLabelText()}正在执行..."
                          )

            text = mi_motion.MAIN()
            self.pushText(self.outputText, f"{self.getTime()}\n{text}")
            self.pushText(self.outputText,
                          f"{self.getTime()} {self.miMotionButton.GetLabelText()}执行完成..."
                          )

    def RSAEncDec(self, message):
        if message != '':
            message = message.split('\n')
            print(message)
            for i  in message:
                cipher, plainNum = RSA.RsaEncDec(i)
                self.pushText(self.outputText,
                              f"cipher:{cipher}\nplainNum:{plainNum}")
        else:
            self.pushText(self.outputText, "请输入...")

    # 获取时间

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

        now = '[ {:0>2d}-{:0>2d}-{:0>2d} {:0>2d}:{:0>2d}:{:0>2d} ]'.format(
            Year, Month, Day, Hour, Minute, Second)
        return now


class funcFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(funcFrame, self).__init__(*args, **kw)


if __name__ == "__main__":

    # with open("./config.json", 'r', encoding='utf-8') as f:
    #     # json.dump(menu_title, f, ensure_ascii=False)
    #     menu_title = json.load(f)

    # 设备显示器信息
    sys_windows_size = [1920, 1080]
    # 主窗口大小 像素
    main_frame_size = [600, 400]
    # 主窗口位置 像素
    main_frame_pos = [
        int((sys_windows_size[0] - main_frame_size[0]) / 2),
        int((sys_windows_size[1] - main_frame_size[1]) / 2)
    ]

    # 主窗口的大小-<-赋值
    main_size = wx.Size(int(main_frame_size[0]), int(main_frame_size[1]))
    # 主窗口的位置-<-赋值
    main_pos = wx.Point(main_frame_pos[0], main_frame_pos[1])

    app = wx.App()
    frame = MainFrame(None,
                      title="My App",
                      size=main_size,
                      pos=main_pos,
                      name='mainFrame')

    frame.Show()
    app.MainLoop()
