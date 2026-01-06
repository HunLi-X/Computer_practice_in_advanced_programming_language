#4.3.3  str.lower()方法把字符串str变成小写
field='DO IT NOW'
print('调用lower得到字符串：',field.lower())
#调用lower得到字符串： do it now

greeting='Hello,World'
print('调用lower得到字符串：',greeting.lower())
#调用lower得到字符串： hello,world

field='DO IT NOW'
print(field.find('It') ) #都不转换为小写，找不到匹配字符串
#-1

print(field.lower().find('It')) #被查找字符串'It'不转换为小写，找不到匹配字符串
#-1

print(field.lower().find('It'.lower()))  #使用lower方法转都换成小写后查找，找到了
#3


