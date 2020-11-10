#创建一个函数power为任意数字做幂运算 n ** i
#递归方法实现
def power(n,i):
    if i == 1:
        return n
    return n * power(n,i-1)
print(power(10,3))
