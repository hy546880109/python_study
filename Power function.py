#创建一个函数power为任意数字做幂运算 n ** i
#递归方法
def power(n,i):
'''
n当作幂函数的运算数
i当作幂函数的指数
'''
    if i == 1:
        return n
    return n * power(n,i-1)

