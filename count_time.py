from time import *

begin = time()
i = 2
while i < 10000:
	flag = True
	j = 2
	while j < i ** 0.5:
		if i % j == 0:
			flag = False
			break
		j += 1
	if flag :
		print(i)
	i += 1	
end = time()
print('程序运行的时间:',end-begin ,'秒')