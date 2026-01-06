#2.7  字符串操作p45，p46
#7个算术运算符
# +   str+str可以；str+int不能；str+float不能；
# -   不能
# *   str*int可以；str*float不能；str*str不能
# **  不能
# /   不能
# //  不能
# %   不能


#>>> 'hello'+3
#Traceback (most recent call last):
#  File "<pyshell#1>", line 1, in <module>
#    'hello'+3
#TypeError: must be str, not int

#>>> 'hello'+3.0
#Traceback (most recent call last):
#  File "<pyshell#2>", line 1, in <module>
#    'hello'+3.0
#TypeError: must be str, not float

string1='hello'
string2='world'
print(string1+string2)
#helloworld

string1='hello'
string2='world'
space=' '
print(string1+space+string2)
#hello world

string1='Hello'
string2=' world'
print(string1+string2)
#Hello world

print('你好，世界！') #可以显示汉字
#你好，世界！
print('馕齉')         #可以显示复杂汉字
#馕齉

#>>> 'world'-1
#Traceback (most recent call last):
#  File "<pyshell#84>", line 1, in <module>
#    'world'-1
#TypeError: unsupported operand type(s) for -: 'str' and 'int'

#>>> 'hello'-'world'
#Traceback (most recent call last):
#  File "<pyshell#86>", line 1, in <module>
#    'hello'-'world'
#TypeError: unsupported operand type(s) for -: 'str' and 'str'

#>>> 'hello'-'he'
#Traceback (most recent call last):
#  File "<pyshell#5>", line 1, in <module>
#    'hello'-'he'
#TypeError: unsupported operand type(s) for -: 'str' and 'str'

print('hello '*3)
#hello hello hello 

#print('hello '*3.0)
#Traceback (most recent call last):
#  File "E:\ZHF\ING\Python3\Py3d6zhf\02Data\02string\00string\00string.py", line 25, in <module>
#    print('hello '*3.0)
#TypeError: can't multiply sequence by non-int of type 'float'

#>>> 'hello'*world
#Traceback (most recent call last):
#  File "<pyshell#85>", line 1, in <module>
#    'hello'*world
#NameError: name 'world' is not defined


#>>> 'hello'/3
#Traceback (most recent call last):
#  File "<pyshell#83>", line 1, in <module>
#    'hello'/3
#TypeError: unsupported operand type(s) for /: 'str' and 'int'


#>>> 'hello'//3
#Traceback (most recent call last):
#  File "<pyshell#3>", line 1, in <module>
#    'hello'//3
#TypeError: unsupported operand type(s) for //: 'str' and 'int'

#>>> 'hello'%2
#Traceback (most recent call last):
#  File "<pyshell#4>", line 1, in <module>
#    'hello'%2
#TypeError: not all arguments converted during string formatting
