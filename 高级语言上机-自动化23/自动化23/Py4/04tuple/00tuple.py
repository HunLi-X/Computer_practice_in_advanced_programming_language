#3.3  元组：元组的元素不能修改；列表的元素可以修改；字符串的元素不能修改
a=1,2,3             #不用括号定义元组a
print(a)
#(1, 2, 3) 
b='hello','world'   #不用括号定义元组b
print(b)
#('hello', 'world')

c=(1, 2, 3)            #用括号定义元组c
print(c)
#(1, 2, 3) 
d=('hello', 'world')   #用括号定义元组d
print(d)
#('hello', 'world')

e=(1, 2, 3,'hello', 'world')#元组中元素的类型可以不同
print(e)
#(1, 2, 3,'hello', 'world')
print(type(e))
#<class 'tuple'>

f=[1, 2, 3,'hello', 'world']#列表中元素的类型也可以不同
print(f)
#[1, 2, 3,'hello', 'world']
print(type(f))
#<class 'list'>
f[0]=9   #列表的元素可以修改
print(f)
#[9, 2, 3,'hello', 'world']

e[0]=9   #元组的元素不能修改,只能读，不能写
#Traceback (most recent call last):
#  File "E:\ZHF\ING\Python3\Py3d6zhf\02Data\04tuple\00tuple.py", line 31, in <module>
#    e[0]=9
#TypeError: 'tuple' object does not support item assignment
