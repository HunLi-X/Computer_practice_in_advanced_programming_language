#hex(x)函数：把十进制数转换为十六进制形式字符串
a=hex(15)
print(a)
#0xf
print(type(a))
#<class 'str'>

print(hex(10))
#0xa
print(type(hex(10)))
#<class 'str'>


#int(x)函数：把十六进制形式字符串转换为十进制数
a=int(0xf)
print(a)
#15
print(type(a))
#<class 'int'>

print(int(0xa))
#10
print(type(int(10)))
#<class 'int'>
