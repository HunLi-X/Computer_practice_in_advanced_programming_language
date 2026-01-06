#5.1  字典的使用
students=['小萌','小智','小强','小张','小李']  #list列表
numbers=['1001','1002','1003','1004','1005']   #list列表
print('小智的学号是：',numbers[students.index('小智')])
#小智的学号是： 1002

#print('小智的学号是：',numbers['小智'])
#期望显示：小智的学号是： 1002
#实际报错
#Traceback (most recent call last):
#  File "E:\ZHF\ING\...\00dict_read.py", line 7, in <module>
#    print('小智的学号是：',numbers['小智'])
#TypeError: list indices must be integers or slices, not str

#5.2  创建和使用字典by {key1:value1,key2:value2,左键:右值,,,}大括号
dict = {'小萌': '1001', '小智': '1002', '小强': '1003'}
print(dict)
#{'小萌': '1001', '小智': '1002', '小强': '1003'}
print(dict['小萌'])
#1001
print(dict['小强'])
#1003

#print(dict['1003'])
#期望显示：小强      实际报错
#Traceback (most recent call last):
#  File "E:\ZHF\ING....\00dict_read.py", line 23, in <module>
#    print(dict['1003'])
#KeyError: '1003'

dict1 = { 'abc': 456 }
print(dict1)
#{'abc': 456}

dict2 = { 'abc': 123, 98.6: 37 }
print(dict2)
#{'abc': 123, 98.6: 37}
