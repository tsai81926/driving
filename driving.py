country = input('請輸入您的國家: ')
age = input('請輸入您的年齡: ')
age = int(age)
if country == '臺灣':
	if age >= 18:
		print('您可以考駕照了!')
	else:
		print('您還不能考駕照!')
elif country == '美國':
	if age >= 16:
		print('You can drive!')
	else:
		print('You can not drive!')
