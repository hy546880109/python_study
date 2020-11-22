#斐波那契数列 0、1、1、2、3、5、8、13、21、34
list = [0,1]
max = input('输入最大位数:')	#限制循环次数
if max.isdigit():	#判断输入的是否为数字
	for n in range(int(max)-len(list)):	#列表内已经有2个值所以要减少2次循环
		list.append(list[n] + list[n+1])	#将2个顺序排列的值相加然后循环添加进列表尾部
	print(list)
else:
	print('你输入的不是数字')


#递归法
# 斐波那契数列 0、1、1、2、3、5、8、13、21、34
new_list = []
n = int(input('please input number:'))
def fun(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1 
    else:          
        return fun(n-1) + fun(n-2)
for i in range(1,n+1):
    new_list.append(fun(n))
print(new_list)

