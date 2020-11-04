max = int(input('输入最大位数:'))
list = [0,1]
for n in range(max-len(list)):
	list.append(list[n] + list[n+1])
print(list)