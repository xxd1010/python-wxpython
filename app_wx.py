# -*- coding: utf-8 -*-

from os import name
import wx
from wx.core import Position, Size


class MainFrame(wx.Frame):

	def __init__(self, *args, **kw):
		super(MainFrame, self).__init__(*args, **kw)
		# 在底部创建一个状态栏
		self.CreateStatusBar()
		self.pushToStatusBar('Already')


	def createWidget(self):

		panel = wx.Panel(self)

		panel_str = wx.StaticText(panel, label= "panel")

	def createMenuBar(self):
		# 创建菜单栏
		file_title = '文件'
		option_title = '操作'

		menu_file = wx.Menu(file_title)
		menu_option = wx.Menu(option_title)

		menubar = wx.MenuBar()

		menubar.Append(menu_file, file_title)
		menubar.Append(menu_option, option_title)

		menubar.Attach(self)

	# 在状态栏里推送消息

	def pushToStatusBar(self, text):
		self.PushStatusText(text)







class Box(wx.Frame):
	
	def __init__(self, *args, **kw):
		super(Box, self).__init__(*args, **kw)
		













if __name__ == "__main__":

	# 设备显示器信息
	sys_windows_size = [1920,1080]
	# 主窗口大小	像素
	main_frame_size = [500,350]
	# 主窗口位置	像素
	main_frame_pos = [int((sys_windows_size[0]-main_frame_size[0])/2), int((sys_windows_size[1]-main_frame_size[1])/2)]

	# 主窗口的大小->赋值
	main_size = wx.Size(int(main_frame_size[0]),int(main_frame_size[1]))
	# 主窗口的位置->赋值
	main_pos = wx.Point(main_frame_pos[0], main_frame_pos[1])

	app = wx.App()
	frame = MainFrame(None, title="My App", size=main_size, pos=main_pos, name='mainFrame')

	
	frame.Show()
	app.MainLoop()