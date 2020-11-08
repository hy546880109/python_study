#回文数
#如果一个数正序和倒序都是相同的则称这个数为回文数，例如 abcba

def fun(n):
    '''
    定义个函数判断是否为回文数
    '''
    if len(n) < 2:
        return True
    elif n[0] != n[-1]:
        return False
    return fun(n[1:-1])

print(fun('ascsa'))