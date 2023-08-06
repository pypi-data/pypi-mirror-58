"""
 # @Author: chang_an
 # @Date: 2019-12-18 18:13:11
 # @LastEditors: chang_an
 # @LastEditTime: 2019-12-21 10:14:20
 # @FilePath: \calculator2.1.0\calculation\calculator_date_page.py
"""

from tkinter import *
from calculator8 import calculator_date
from calculator8 import calculator_standard_science
from calculator8 import button_names


class dateFrame(Frame):
    """[日期计算页面实现]
    
    Arguments:
        Frame {[class]} -- [tkinter子类]
    """

    def __init__(self, master=None):
        """[日期计算页面初始化]
 
        """
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root

        self.datepage()

    def datepage(self):
        """[设定日期计算页面具体细节]
        
        """
        self.show = Label(
            self,
            relief=SUNKEN,
            font=("Courier New", 20),
            width=23,
            bg="white",
            anchor=W,
        )
        self.show.pack(side=TOP, pady=24)
        label = Label(
            self, anchor=W, text="日期计算(请输入类似日期：2019.12.9+(-)12或者2019.12.9-2019.2.2)"
        )
        label.place(x=0, y=62)
        p = Frame(self)
        p.pack(side=BOTTOM)
        button_names.button_name(
            p,
            name=(
                "1",
                "2",
                "3",
                "4",
                "6",
                "6",
                "8",
                "8",
                "9",
                "0",
                "+",
                "-",
                ".",
                "=",
                "←",
                "↺",
            ),
            number=4,
            click_method=self.date_click,
            clean_method=self.clean,
        )

    def date_click(self, event):
        """[日期点击计算函数]
        
        Arguments:
            event {['tkinter.Event']} -- [点击事件]
        """

        if event.widget["text"] == "=" and self.show["text"] is not None:
            self.show["text"] = calculator_date.date_calculation_click(
                event, self.show["text"]
            )

        self.show["text"] = calculator_standard_science.standard_science_calc(
            event, self.show["text"]
        )

    def clean(self, event):
        """[清空函数]

        Arguments:
            event {['tkinter.Event']} -- [点击事件]
        """
        self.show["text"] = ""
