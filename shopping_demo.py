shop_list = [
	('Mac电脑',9500),
	('windows电脑',3000),
	('法拉利',80000000),
	('python教程书籍',100),
]

saving=input('输入你的金钱:')
shopping_car=[]
not_q = True
print('你的金钱总数为:%s'%saving)
while not_q:
	if saving.isdigit(): #判断输入的金钱是否为数字格式
		saving=int(saving) 
		while not_q:
			for i,v in enumerate(shop_list,1):
				print(i,'>>>>>',v)

			choice = input("选择商品号码进行购买,退出请按q:")
			if choice.isdigit(): #判断选择项是否为数字
				choice=int(choice)
				if choice >= 1 and choice <= len(shop_list):  #判断选择项在1-末尾
					shop_item = shop_list[choice-1]  #根据位置提取商品和价格

					if shop_item[1]<=saving:   #判断你要买的东西的价格小于你的金钱
						
						saving = saving - shop_item[1]	#你的钱等于之前的金钱减去买的东西的用掉的钱
						shopping_car.append(shop_item)	#将购买的商品和价格添加进购物车
						print('购买成功，你还剩%s元'%saving)

					else:
						print('余额不足,还剩%s'%saving)
				else:
					print('选择错误')
			elif choice == 'q' or choice == 'Q':
				print('你已经购买如下商品:')
				
				for i in shopping_car:
					print(i[0])
			
				# print('你的消费金额为:%s'%sum)
				print('当前剩余%s元钱'%saving)
				not_q = False
			else:
				print('输入语法错误')
	else:
		print('你输入的不是金钱数量,请重新输入！')
		saving=input('输入你的金钱:')