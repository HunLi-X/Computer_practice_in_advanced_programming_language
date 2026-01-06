#4.3.2  str.join()方法
#
num=[1,2,3,4,5]
mark='+'
#abc=mark.join(num)
#Traceback (most recent call last):
#  File "<pyshell#219>", line 1, in <module>
#    abc=mark.join(num)
#TypeError: sequence item 0: expected str instance, int found
#mark是string类型，num是列表类型，无法join连接

#abc=num.join(mark)
#Traceback (most recent call last):
#  File "<pyshell#216>", line 1, in <module>
#    abc=num.join(mark)
#AttributeError: 'list' object has no attribute 'join'
#mark是string类型，num是列表类型，无法join连接

field=['1','2','3','4','5']
print('连接字符串列表：',mark.join(field))
#连接字符串列表： 1+2+3+4+5

#print(field.join(mark))
#Traceback (most recent call last):
#  File "<pyshell#228>", line 1, in <module>
#    print(field.join(mark))
#AttributeError: 'list' object has no attribute 'join'

dirs='','home','data','hdfs'
print('路径：','/'.join(dirs))
#路径： /home/data/hdfs
