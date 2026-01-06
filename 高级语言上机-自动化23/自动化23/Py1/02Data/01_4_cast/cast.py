#cast.py强制类型转换
#2.2.4  数据类型转换

#>>> int(152.1)
#152
a=152.1
print(a)        #152.1
print(type(a))  #<class 'float'>
b=int(a)
print(b)        #152
print(type(b))  #<class 'int'>

#>>> float(252.1)
#252.1
a=252.1
print(a)        #252.1
print(type(a))  #<class 'float'>
b=float(a)
print(b)        #252.1
print(type(b))  #<class 'float'>

#>>> float(int(352.6))
#352.0
a=352.6
print(a)        #352.6
print(type(a))  #<class 'float'>

b=int(a)        # int()仅取整，不四舍五入
print(b)        #352
print(type(b))  #<class 'int'>

c=float(b)
print(c)        #352.0
print(type(c))  #<class 'float'>
