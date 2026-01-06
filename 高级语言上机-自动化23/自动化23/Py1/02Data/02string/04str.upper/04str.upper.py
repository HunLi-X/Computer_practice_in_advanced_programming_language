#4.3.4  str.upper()方法把字符串str变成大写
field='do it now'
print('调用upper得到字符串：',field.upper())
#调用upper得到字符串： DO IT NOW

greeting='Hello,World'
print('调用upper得到字符串：',greeting.upper())
#调用upper得到字符串： HELLO,WORLD

field='do it now'
print(field.find('It')) #都不转换为大写，找不到匹配字符串
#-1
print(field.upper().find('It')) #被查找字符串'It'不转换为大写，找不到匹配字符串
#-1
print(field.upper().find('It'.upper()))  #使用upper方法转都换为大写后查找，找到了
#3
