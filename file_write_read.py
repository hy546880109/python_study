from faker import Faker
from datetime import datetime
from time import sleep
import traceback
#利用随机数据生成函数将数据循环写入到文本中，并计算运行时间
try:
    number = int(input('输入你需要的数据行数:'))
    init_time = datetime.now()
    fake = Faker(locale='zh_CN')
    with open(r'd:\test.txt','w')as f:
        for i in range(1,number+1):
            name = fake.name()
            phone = fake.phone_number()
            test_number = '姓名: '+ name+' 手机号: '+ phone + '\n'
            f.write(test_number)
            print(f'第{i}条正在写入>>>！')
        print('写入完成，开始读取！！！')
    now_time = datetime.now()
    sleep(2)
#循环读取上面写入的文本内容，并计算运行时间
    init_read_time = datetime.now()
    with open(r'd:\test.txt','r')as f:
        while True:
            block = f.read(1024)
            if not block:
                break
            print(block)
    now_read_time = datetime.now()
    print("写入执行时间:"+str((now_time-init_time).seconds)+"秒")
    print("读取执行时间:"+str((now_read_time-init_read_time).seconds)+"秒")
    print('执行结束！！！')
# #如果出现错误则捕获错误并打印
except Exception as e:
    print('出现异常')
    print(e)
    error = traceback.format_exc()
    print(error)
# #不管是否错误都执行关闭文件
# finally:
#     f.close()

