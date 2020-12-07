#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:Huny
import urllib.request
import urllib.parse
import json
import tkinter as tk
import tkinter.messagebox

window = tk.Tk()

#标题
window.title('Huny之家')
window.geometry('500x300')

#加载图片
canvas = tk.Canvas(window,width=400,height=135,bg='green')#创建画布
image_file = tk.PhotoImage(file='pic.gif')#添加图片的路径
image = canvas.create_image(200,0,anchor='n',image=image_file)#创建图片并声明大小和位置以及图片的路径
canvas.pack(side='top')
tk.Label(window,text='Wellcome',font=('Arial',16)).pack()#声明一个小部件并放在父部件window中
#名称
tk.Label(window,text='用户名').place(x=50,y=165)
tk.Label(window,text='密码').place(x=50,y=200)

#文本和密码输入框、登录按钮
var_usr_name = tk.StringVar()#记录输入值的变量
var_usr_name.set('huny')#设置默认用户名
e1 =tk.Entry(window ,textvariable=var_usr_name,font=('Arial',14))#定义一个文本框和字体，接受文本框中的值
var_usr_pwd = tk.StringVar()
e2 =tk.Entry(window, show='*',textvariable=var_usr_pwd,font=('Arial',14))
e1.pack()#将小部件组织成块，然后再将其放置在主小部件中
e2.pack()

#登录弹窗提示功能
def login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    user_info = {'huny':'123456'}
    if usr_name in user_info:
        if usr_pwd == '123456':
            tkinter.messagebox.showinfo(title='欢迎来到Huny之家',message='登录成功！')#正确的弹窗提示
        else:
            tkinter.messagebox.showerror(title='提醒',message='密码错误！')#错误的弹窗提示
    else:
        tkinter.messagebox.showerror(title='提醒',message='用户名错误')#错误的弹窗提示
e3 = tk.Button(window,text="登录",width=10,height=2,command=login)#声明一个按钮部件
e3.pack()
window.mainloop()
