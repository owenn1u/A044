password = '12345678'

i = 0

while i < 3:
	pwd = input('請輸入密碼: ')
	if password == pwd:
		print('登入成功!')
		break
	else:
		i = i + 1
		print('密碼錯誤!還有', 3-i, '次機會')
		if i == 0:
			break

		
