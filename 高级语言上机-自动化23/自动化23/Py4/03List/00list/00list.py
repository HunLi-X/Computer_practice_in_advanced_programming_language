#3.2.1  更新列表
a=[1,2,3,2,1]
a[1]=10
print(a)
#[1, 10, 3, 2, 1]
a[3]=10
print(a)
#[1, 10, 3, 10, 1]
a[2]='hello'  #对编号为2的元素赋值，赋一个字符串
print(a)
#[1, 10, 'hello', 10, 1]
print(type(a))
#<class 'list'>
print(type(a[1]))  #别忘了查看类型函数的使用
#<class 'int'>
print(type(a[2]))
#<class 'str'>
tring=[1,2,3]
tring[3]='test'
#Traceback (most recent call last):
#  File "E:\ZHF\ING\...00list.py", line 19, in <module>
#    tring[3]='test'
#IndexError: list assignment index out of range

