#类装饰器
import time

class Show_time():
    def __init__(self,fun):
        self.fun = fun
    def __call__(self):
        start_time = time.time()
        self.fun()
        end_time = time.time()
        show_time = end_time - start_time
        print('运行时间:%.3f秒'%show_time)
@Show_time
def fun_a():
    time.sleep(1)
    print('fun_a is running')

@Show_time
def fun_b():
    time.sleep(2)
    print('fun_b is running')
fun_a()
fun_b()