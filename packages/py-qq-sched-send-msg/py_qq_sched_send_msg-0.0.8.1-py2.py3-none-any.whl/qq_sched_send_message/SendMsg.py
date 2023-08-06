# -*- coding:utf-8 -*-
from .Erorr import MessageDoesNotExistException
from .Erorr import WindowDoesNotExistException

from .Sched import Schedar


import win32gui
import win32con
import win32clipboard
from functools import wraps


class Send_Msg:
    scheds = Schedar()

    def __init__(self, name: str, time=0):
        self.handle = None
        self.name = name
        """窗体名字"""
        self.time = time
        """发送间隔为0则无间隔"""

    def __call__(self, func):
        wraps(func)
        self.func = func

        Send_Msg.scheds.add_task(
            self.run, id=str(self.func.__name__), time=self.time)

    def run(self):
        """运行"""

        self.handle = self.ifwindow(self.name)
        """窗口句柄"""
        if not self.handle:
            Send_Msg.scheds.remove(str(self.func.__name__))
            raise WindowDoesNotExistException(self.name)

        msg = self.func()
        if msg is None:
            Send_Msg.scheds.remove(str(self.func.__name__))
            raise MessageDoesNotExistException(self.func.__name__)

        self.copy_msg(msg)
        self.send(self.handle)

    def copy_msg(self, msg):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, msg)
        win32clipboard.CloseClipboard()

    def send(self, handle):
        win32gui.SendMessage(handle, 770, 0, 0)
        win32gui.SendMessage(
            handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)

    def ifwindow(self, name):
        return win32gui.FindWindow(None, name)
