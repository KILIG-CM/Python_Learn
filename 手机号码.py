import re
pattern = r'(13[4-9]\d{8})$|(15[01289]\d{8})$'
mobile = '1363*******' #*号换成数字7位
match = re.match(pattern, mobile)
if match == None:
	print(mobile, '不是有效的中国移动手机号')
else:
	print(mobile, '是有效的中国移动手机号')
mobile = '1314*******' #*号换成数字7位
match =re.match(pattern, mobile)
if match == None:
	print(mobile, '不是有效的中国移动手机号')
else:
	print(mobile, '是有效的中国移动手机号')