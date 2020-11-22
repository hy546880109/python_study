import threading 
from datetime import datetime

def read_txt():
    '''
        该函数实现读取文本数据读取并输出执行时间
    '''
    with open(r'd:\test.txt','r')as f:
        while True:
            block = f.read(1024)
            yield block
            if not block:
                break       
            # print(block)

def read_lines():
    ls = read_txt()
    for i in ls:
        print(i)

t = threading.Thread(target=read_lines)
init_read_time = datetime.now()
t.start()
t.join()

now_read_time = datetime.now()
print("读取执行时间:"+str((now_read_time-init_read_time).seconds)+"秒")
print('执行结束！！！')

