print('*'*10,'欢迎登陆游戏','*'*10)
print('请选择你的角色:')
print('1:战士\n2:法师')
a = 2 
b = 1
c = 1 
d = 2
e = 10
f = 10 
while True:
	user = input('输入你的选项：')
	if user == '1':
		print('你选择了战士:生命值:%d,攻击力:%d'%(a,b))
		break
	if user == '2':
		print('你选择了法师:生命值:%d,攻击力:%d'%(c,d))
		break
	else:
		print('你的选择有误,请重新选择')
while True:	
	print('选择你的游戏模式')
	print('1:升级模式\n2:挑战模式\n3:逃跑模式')
	mode = input('输入你的选择:')
	if mode == '1':
		a += 1
		b += 1
		c += 1
		d += 1
		if user == '1':
			print('等级上升,生命值:%d,攻击力:%d'%(a,b))
		if user == '2':
			print('等级上升,生命值:%d,攻击力:%d'%(c,d))
	if mode == '2':
		print('BOSS:生命值:%d,攻击力%d'%(e,f),'你将对BOSS发起挑战')
		if e <= b or e <= d:
			print('恭喜你成功击败BOSS，成功通关！')
			break	
		else:
			print('很遗憾，你被BOSS击杀,未能通关')
			break	

	if mode == '3':
		print('正在退出游戏...')
		break	