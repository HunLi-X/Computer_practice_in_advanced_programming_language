#7.1  调用函数
print('hello world')  #print()是函数
#hello world
print(type('hello'))  #type()是函数，获得数据类型
#<class 'str'>
print(int(12.1))      #int()是函数，转换为int整数
#12


#>>> help(abs)        #获得abs()函数的帮助说明，求绝对值
#Help on built-in function abs in module builtins:
#abs(x, /)
#    Return the absolute value of the argument.

	
print(abs(20))
#20
print(abs(-20))
#20
print(abs(3.14))
#3.14
print(abs(-3.14))
#3.14

fun=abs  # 变量fun指向abs函数，给同一个函数起第二个名字
print(fun(-5))  # 所以可以通过fun调用abs函数
#5
print(fun(-3.14))  # 所以可以通过fun调用abs函数
#3.14
print(fun(3.14))  # 所以可以通过fun调用abs函数
#3.14

#print(abs(5,6))     #abs()中不允许多个数值
#Traceback (most recent call last):
#  File "<pyshell#171>", line 1, in <module>
#    abs(5,6)
#TypeError: abs() takes exactly one argument (2 given)


print(abs('hello')) #abs()中不允许字符串
#Traceback (most recent call last):
#  File "<pyshell#172>", line 1, in <module>
#    abs('hello')
#TypeError: bad operand type for abs(): 'str'



