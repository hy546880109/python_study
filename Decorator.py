#装饰器统计程序运行时间
from datetime import datetime
from time import sleep

def run_time(fun):
    """
        将其他函数当作参数传入，计算这个函数的执行时间
    """
    def wrapper(*arg,**args):
        init_time = datetime.now()     
        f = fun(*arg,**args)
        now_time = datetime.now()
        print('程序执行时间:',str((now_time - init_time).seconds),'秒')
        print('程序执行结果:')
        return f
    return wrapper

@run_time
def run(x):
    sleep(1)    
    print(x,'程序执行完成')
    return x

@run_time
def run2(x,y):
    sleep(2)
    print(x ,'+', y,'程序执行完成')
    return x + y
print(run(1))
print(run2(1,1))


