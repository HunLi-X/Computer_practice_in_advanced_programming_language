#4.1  字符串的基本操作

field='Hello'    #创建字符串Hello，并赋给变量field
print(field)     #字符串完整读可以
#Hello

field='just do it'
print(field[7:])  #字符串切片读可以
# it   #切出一个空格和it

print(field[-3:])  #字符串切片读可以
# it   #切出一个空格和it

print(field[-3:-2])  #字符串切片读可以
#    #切出一个空格

print(field[-3:-1])  #字符串切片读可以
# i  #切出一个空格和一个i

#>>> field[-3:]='now'        #字符串切片写不可以
#Traceback (most recent call last):
#  File "<pyshell#113>", line 1, in <module>
#    field[-3:]='now'
#TypeError: 'str' object does not support item assignment


