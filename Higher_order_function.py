#高阶函数
l = [1,2,3,4,5,6,7,8,9]
new_list = []
def fun(func,i):
    for n in i:
        if func(n):
            new_list.append(n)
    return new_list

def fun1(i):
    if i % 3 == 0:
        return True
    return False
def fun2(i):
    if i % 2 != 0:
        return True
    return False

print(fun(fun2,l))

f = lambda x,y : x+y
print(f(3,4))


#map函数
lie = [1,2,3,4,5]
new_list = map(lambda x: x*x,lie)
print(new_list)
print(list(new_list))

#filter函数
lie = [1,2,3,4,5]
def test(n):
    return n % 2 == 0
new_list = filter(test,lie)
print(new_list)
print(list(new_list))

#reduce函数
from functools import reduce
listDemo = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, listDemo)
print(product)





