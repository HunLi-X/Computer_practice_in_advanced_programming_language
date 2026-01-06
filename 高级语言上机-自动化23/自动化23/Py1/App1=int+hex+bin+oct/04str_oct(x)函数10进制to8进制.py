#october(x)，oct(x)函数：把十进制数转换为八进制形式字符串

a=oct(15)
print(a)
#0o17
print(type(a))
#<class 'str'>

print(oct(10))
#0o12
print(type(oct(10)))
#<class 'str'>


#int(x)函数：把八进制形式字符串转换为十进制数

a=int(0o17)
print(a)
#15
print(type(a))
#<class 'int'>

print(int(0o12))
#10
print(type(int(0o12)))
#<class 'str'>
