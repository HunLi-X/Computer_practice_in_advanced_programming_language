#str.eval()评估函数去掉字符串两端的引号
str2="123"
print(str2)
#123
print(type(str2))
#<class 'str'>

b=eval(str2)
print(b)
#123
print(type(b))
#<class 'int'>

str1="Hello Python!"
a=eval(str1)
print(a)
#Traceback (most recent call last):
#  File "E:\ZHF\ING\...\10str.eval\10str.eval评估函数去掉字符串两端的引号.py",
#    line 10, in <module>
#    a=eval(str1)
#  File "<string>", line 1
#    Hello Python!
#               ^
#SyntaxError: invalid syntax
