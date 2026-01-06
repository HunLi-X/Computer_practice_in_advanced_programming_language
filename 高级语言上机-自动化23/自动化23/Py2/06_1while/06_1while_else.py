#6.6.6  循环中的else子句
#1. 在while循环中使用else语句，成对使用
#! /usr/bin/python3
#-*- coding:UTF-8 -*-

num = 0
while num < 3:
   print (num, " 小于 3")
   num = num + 1
else:
   print (num, " 大于或等于 3")
print("结束循环!")
#结果：
#0  小于 3
#1  小于 3
#2  小于 3
#3  大于或等于 3
#结束循环!
num = 0
while num < 3:
   print (num, " 小于 3")
   num = num + 1

print (num, " 大于或等于 3")
print("结束循环!")
#结果：
#0  小于 3
#1  小于 3
#2  小于 3
#3  大于或等于 3
#结束循环!
#不用else，效果一样
