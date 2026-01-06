#chr(数字编码)函数，把【十进制数字Unicode编码】转换为【字符】，
#或称：查看(数字)Unicode编码对应的字符

a1=chr(97)
print('chr(97)',a1) #97 0x61
#chr(97) a
print(type(a1))
#<class 'str'>

a2=chr(0x61)
print('chr(0x61)',a2) #97 0x61
#chr(0x61) a
print(type(a2))
#<class 'str'>

b1=chr(65)
print('chr(65)',b1) #65 0x41
#chr(65) A
print(type(b1))
#<class 'str'>

b2=chr(0x41)
print('chr(0x41)',b2) #65 0x41
#chr(0x41) A
print(type(b2))
#<class 'str'>

c1=chr(23398)
print('chr(23398)',c1) #23398 0x5b66 是学的Unicode编码
#chr(23398) 学
print(type(c1))
#<class 'str'>

c2=chr(0x5b66)
print('chr(0x5b66)',c2) #23398 0x5b66 是学的Unicode编码
#chr(0x5b66) 学
print(type(c2))
#<class 'str'>

e1=chr(35821)
print('chr(35821)',e1) #35821 0x8bed 是语的Unicode编码
#chr(35821) 语
print(type(e1))
#<class 'str'>

e2=chr(0x8bed)
print('chr(0x8bed)',e2) #35821 0x8bed 是语的Unicode编码
#chr(0x8bed) 语
print(type(e2))
#<class 'str'>

f1=chr(35328)
print('chr(35328)',f1) #35328 0x8a00 是言的Unicode编码
#chr(35328) 言
print(type(f1))
#<class 'str'>

f2=chr(0x8a00)
print('chr(0x8a00)',f2) #35328 0x8a00 是言的Unicode编码
#chr(0x8a00) 言
print(type(f2))
#<class 'str'>


