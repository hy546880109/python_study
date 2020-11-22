#property装饰器
#方法加入@property后，这个方法相当于一个属性，这个属性可以让用户进行使用，而且用户有没办法随意修改
class DataSet(object):
    def __init__(self):
        self.__name = "张三"
        self.__age = 18 #定义属性的名称
    @property
    def name(self): 
        return self.__name
    @property
    def age(self):
        return self.__age

test_object = DataSet()
print(test_object.name) # 加了@property后，可以用调用属性的形式来调用方法,后面不需要加（）。
print(test_object.age)