# 碼重試程式
# password = 'a123456'
# 讓使用者重複輸入密碼
# 最多輸入3次
# 如果正確 就印出 "登入成功!"
# 如果不正確 就印出 "密碼錯誤! 還有__次機會!"

password = 'a123456'
i = 3 #剩餘機會
while i > 0:
	pwd = input('請輸入密碼: ')	
	if pwd == password:
		print('登入成功')
		break

	else:
		i = i - 1
		print('密碼錯誤!還有', i,'次機會')	
	