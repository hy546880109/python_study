# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author :  Huny
# @Email : hy54688010@qq.com
# @File : app.py
# @Project: 第22课时作业
import itertools

# case_list = ['用户名', '密码']
# value_list = ['正确', '不正确', '特殊符号', '超过最大长度','为空']

case_list = input('输入所有测试对象,并用空格分开：') 
step = input('输入执行的动作：')
value_list = input('输入所有测试结果,并用空格分开：')
print('测试用例集合》》》')
str1 = case_list.split(' ')
str2 = value_list.split(' ')
def get_case(step=step, item=str1, value=str2):
    '''输出笛卡尔用例集合'''
    for i in itertools.product(item, value):
        print(f'{step}'.join(i))

if __name__ == '__main__':
    get_case()

