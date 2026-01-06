#variate变量，区分大小写，以字母或下划线_开始,
#2.3.1  变量,type(变量)可获得变量类型

xiaohong='XiaoHong'
print(xiaohong)
#XiaoHong


#>>> abc
#Traceback (most recent call last):
#  File "<pyshell#33>", line 1, in <module>
#    abc
#NameError: name 'abc' is not defined


a = 123
print(a)
#123
print(type(a))
#<class 'int'>

_a='ABC'
print(_a)
#ABC
print(type(_a))
#<class 'str'>


print(type('Hello,world!'))
#<class 'str'>

print(type(100))
#<class 'int'>

print(type(3.0))
#<class 'float'>


a1='test type'
print(type(a1))
#<class 'str'>


b_2=100
print(type(b_2))
#<class 'int'>


c=3.0
print(type(c))
#<class 'float'>


print(type('test single quotes'))
#<class 'str'>

print(type("test double quote"))
#<class 'str'>

print(type("100"))
#<class 'str'>

print(type("3.0"))
#<class 'str'>

b=3
print(type(b))
#<class 'int'>

b=100
print(type(b))
#<class 'int'>

c=3.0
print(type(c))
#<class 'float'>


a=100
a=a+200
print(a)
#300


a='ABC'
b=a
a='XYZ'
print(b)
#ABC

#2.3.2  变量名称,区分大小写
name='study python is happy'
Name='I aggree with you'
print(name)
#study python is happy
print(Name)
#I aggree with you


happy_study='stay hungry stay foolish'
print(happy_study)
#stay hungry stay foolish


#>>> 2wrongtest='just for test'
#SyntaxError: invalid syntax
#数字不能作为变量的第一个字符


#>>> xiaoming@me='surprised'
#SyntaxError: can't assign to operator
#@不能作为变量的字符


#>>> from='from'
#SyntaxError: invalid syntax
#from关键字不能作为变量的字符，

#33个关键字KeyWord，又称【保留字】：p33
#01 False
#02 None
#03 true
#04 and
#05 as
#06 assert
#07 break
#08 class
#09 continue
#10 def
#11 del
#12 elif
#13 else
#14 except
#15 finally
#16 for
#17 from
#18 global
#19 if
#20 import
#21 in
#22 nonlocal
#23 lambda
#24 is
#25 not
#26 or
#27 pass
#28 raise
#29 return
#30 try
#31 while
#32 with
#33 yield



