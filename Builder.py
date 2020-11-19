#简单的生成器方式
ls = [x*x for x in range(10)]
print(type(ls))
print(ls)


ls2 = (x*x for x in range(10))
print(ls2)
for i in ls2:
    print(i,end=',')

#yield制造生成器
def a(x):
    for i in range(x): 
        yield i*i
s = a(5)
print(s)
for i in s:
    print(i)
生成器制作斐波那契数列
def fb(n):
    a,b = 0,1
    for i in range(n):
        yield b
        a,b = b,a+b

f = fb(10)
for i in f:
    print(i,end=',')


#生成器读取大量数据的文本
from datetime import datetime

def read_txt():
    '''
        该函数实现读取文本数据读取并输出执行时间
    '''
    init_read_time = datetime.now()
    with open(r'd:\test.txt','r')as f:
        while True:            
            block = f.read(1024)
            yield block
            if not block:
                break
    now_read_time = datetime.now()
    print("读取执行时间:"+str((now_read_time-init_read_time).seconds)+"秒")
    print('执行结束！！！')
read_now = read_txt()
# print(next(read_now))
# print(next(read_now))
print(read_now)
for i in read_now:
    print(i)


#生成器对比普通循环的优点
import sys
#查看占用内存大小
mylist = [i for i in range(10000000)]
print(type(mylist))
print('列表占用内存大小:',sys.getsizeof(mylist),'字节')

mygen = (i for i in range(10000000))
print(mygen)
print('生成器占用内存大小:',sys.getsizeof(mygen),'字节')



