#bin(x)函数：把十进制数转换为二进制形式字符串
a=bin(15)
print(a)
#0b1111
print(type(a))
#<class 'str'>

print(bin(10))
#0b1010
print(type(bin(10)))
#<class 'str'>


#int(x)函数：把十六进制形式字符串转换为十进制数
a=int(0b1111)
print(a)
#15
print(type(a))
#<class 'int'>

print(int(0b1010))
#10
print(type(int(10)))
#<class 'int'>
