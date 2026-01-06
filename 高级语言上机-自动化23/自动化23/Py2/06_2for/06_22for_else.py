#2. 在for循环中使用else语句
#! /usr/bin/python3
#-*- coding:UTF-8 -*-

names = ['xiaomeng', 'xiaozhi']   #列表
for name in names:
    if name == "xiao":
        print("名称：",name)
        break
    print("循环名称列表 " , name)  # + 同 ,
else:
    print("没有循环数据!")
print("结束循环!")

#结果：
#循环名称列表 xiaomeng
#循环名称列表 xiaozhi
#没有循环数据!
#结束循环!

