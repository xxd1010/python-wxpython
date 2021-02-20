# -*- coding: utf-8 -*-

from os import name
from re import I
import string
import json
import time
import wx
import wx.grid
from wx.core import MenuBar, Position, Size, Button

import pretty_errors
import mi_motion
import RSAEnDecrypt
import hutlib.main as hutlib

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

    def createFrame(self):
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
        miMitionPanel = wx.Panel(self,
                                 -1,
                                 size=size,
                                 pos=(10, buttonBoxSize[1] * 2 + 10))
        functionPanel3 = wx.Panel(self,
                                  -1,
                                  size=size,
                                  pos=(10, buttonBoxSize[1] * 3 + 10))

        self.functionBotton1 = wx.Button(functionPanel1,
                                         -1,
                                         label='获取时间',
                                         size=functionPanel1.GetSize(),
                                         pos=self.calculatePosPoint(
                                             buttonBoxSize, buttonBoxSize))
        self.encryptButton = wx.Button(functionPanel2,
                                       -1,
                                       label='加密',
                                       size=functionPanel2.GetSize(),
                                       pos=self.calculatePosPoint(
                                           buttonBoxSize, buttonBoxSize))
        self.loginLibButton = wx.Button(functionPanel3,
                                        -1,
                                        label='登录学校图书馆',
                                        size=functionPanel3.GetSize(),
                                        pos=self.calculatePosPoint(
                                            buttonBoxSize, buttonBoxSize))
        self.miMotionButton = wx.Button(miMitionPanel,
                                        -1,
                                        label='小米运动',
                                        size=miMitionPanel.GetSize(),
                                        pos=self.calculatePosPoint(
                                            buttonBoxSize, buttonBoxSize))

        self.encryptButton.SetDefault()
        self.miMotionButton.SetDefault()
        self.loginLibButton.SetDefault()
        self.functionBotton1.SetDefault()

        inputTextPanel = wx.Panel(self, size=(600, 60), pos=(350, 20))
        self.inputText = wx.TextCtrl(inputTextPanel, -1, value='', pos=(
            0, 0), size=inputTextPanel.GetSize())

        outputTextPanel = wx.Panel(self, size=(600, 400), pos=(350, 80))
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
            self.inputText.GetValue()), self.encryptButton)
        self.Bind(wx.EVT_BUTTON, lambda user: self.hutLib(),
                  self.loginLibButton)
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

    def createTable(self):

        grid = wx.grid.Grid(self, -1)

        grid.createGrid(100, 10)

        grid.SetRowSize(0, 60)
        grid.SetColSize(0, 120)

        grid.SetCellValue(0, 0, 'wxGrid is good')

    # 划分字符

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

    # 计算坐标点

    def calculatePosPoint(self, bigger, smaller):
        point = [
            int((bigger[0] - smaller[0]) / 2),
            int((bigger[1] - smaller[1]) / 2)
        ]
        return wx.Point(point[0], point[1])

    # 推送

    def pushText(self, Panel, text):
        Panel.AppendText(f"{text}\n")

    # 外部小功能
    # 小米运动

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

    # RSA加密

    def RSAEncDec(self, message):
        if message != '':
            message = message.split('\n')
            for i in message:
                encrypt = RSAEnDecrypt.main(i)
                self.pushText(self.outputText,
                              f"encPwd:{encrypt.decode('utf8')}\nPWD:{i}")
        else:
            self.pushText(self.outputText, "请输入...")

    # 登录学校图书馆

    def hutLib(self):
        # self.pushText(self.outputText, '输入用户名:')
        username = self.inputText.GetValue()
        username = '17405702222'
        password = 'hutlib@#$'
        result = hutlib.main(username, password)

        item_info, list_lib = hutlib.getItemInfo(result)
        for i in item_info:
            self.pushText(self.outputText, i)
        # self.outputText.Hide()
        # grid = wx.grid.Grid(self, pos=(200, 80), size=(700, 400))
        # grid.CreateGrid(10, 5)
        # table = GridTable(item_info)
        # grid.SetTable(table, True)

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

    # 装饰器

    def warpper(func):
        def warp():
            print('正在请求...')
            result = func()
            print('请求完成...')
            return result


class funcFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(funcFrame, self).__init__(*args, **kw)


class GridTable(wx.grid.PyGridTableBase):

    def __init__(self, data):
        wx.grid.GridTableBase.__init__(self)
        self.row = 10
        self.column = 5
        self.data = data
        self.column = ['名称', '分类', '链接', 'rid']

        self.odd = wx.grid.GridCellAttr()
        # self.odd.SetBackgroundColour('white')
        # self.odd.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        #
        self.event = wx.grid.GridCellAttr()
        # self.event.SetBackgroundColour('sky blue')
        # self.event.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))

    def GetNumberRows(self):
        return 50

    def GetNumberCols(self):
        return 50

    def IsEmptyCell(self, row, col):
        return self.data.get((row, col)) is not None

    def GetValue(self, row, col):
        value = self.data.get((row, col))
        if value is not None:
            return value
        else:
            return ''

    def SetValue(self, row, col, value):
        self.data[(row, col)] = value
        self.data.clear()

    def GetAttr(self, row, col, kind):
        attr = [self.event, self.odd][row % 2]
        attr.IncRef()
        return attr


if __name__ == "__main__":
    # with open("./config.json", 'r', encoding='utf-8') as f:
    #     # json.dump(menu_title, f, ensure_ascii=False)
    #     menu_title = json.load(f)

    # 设备显示器信息
    sys_windows_size = [1920, 1080]
    # 主窗口大小 像素
    main_frame_size = [1000, 600]
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
