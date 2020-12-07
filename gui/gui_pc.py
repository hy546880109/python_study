#!/usr/bin/ python
# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import json
from tkinter import *
import hashlib
import time

LOG_LINE_NUM = 0

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name


    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("翻译工具")           #窗口名
        # self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('1080x581+10+10')
        self.init_window_name["bg"] = "green"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        # self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
        #标签
        self.init_data_label = Label(self.init_window_name, text="待处理数据")
        self.init_data_label.grid(row=0, column=4)
        self.result_data_label = Label(self.init_window_name, text="输出结果")
        self.result_data_label.grid(row=0, column=16)
        self.log_label = Label(self.init_window_name, text="日志")
        self.log_label.grid(row=12, column=4)
        #文本框
        self.init_data_Text = Text(self.init_window_name, width=67, height=25)  #原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.result_data_Text = Text(self.init_window_name, width=70, height=39)  #处理结果展示
        self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)
        self.log_data_Text = Text(self.init_window_name, width=66, height=12)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)
        #按钮
        self.str_trans_to_md5_button = Button(self.init_window_name, text="一键翻译", bg="lightblue", width=8,command=self.translate)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=5, column=11)


    #功能函数
    def  translate(self):        
        centens = self.init_data_Text.get(1.0,END).strip().replace("\n","")
        if centens:
            try:
                url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
                data = {}
                data['i'] = centens
                data['from'] = 'AUTO'
                data['to'] = 'AUTO'
                data['smartresult'] = 'dict'
                data['client'] = 'fanyideskweb'
                data['salt'] = '16057996372935'
                data['sign'] = '0965172abb459f8c7a791df4184bf51c'
                data['lts'] = '1605799637293'
                data['bv'] = 'f7d97c24a497388db1420108e6c3537b'
                data['doctype'] = 'json'
                data['version'] = '2.1'
                data['keyfrom'] = 'fanyi.web'
                data['action'] = 'FY_BY_REALTlME'
                data = urllib.parse.urlencode(data).encode('utf-8')
                response = urllib.request.urlopen(url,data)
                html = response.read().decode('utf-8')
                req = json.loads(html)
                result = req['translateResult'][0][0]['tgt']
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,result)
                self.write_log_to_Text("INFO:str_trans_ success")
            except:
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"操作错误")
        else:
            self.write_log_to_Text("ERROR:str_trans_ failed")
                    
    #获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time

    #日志动态打印
    def write_log_to_Text(self,logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      #换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0,2.0)
            self.log_data_Text.insert(END, logmsg_in)

def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()
    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示

gui_start()