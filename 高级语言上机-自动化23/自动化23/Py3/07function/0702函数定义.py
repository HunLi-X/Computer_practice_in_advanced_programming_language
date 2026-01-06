#7.2  定义函数
#! /usr/bin/python3
# -*- coding:UTF-8 -*-

def hello():
    print('hello,world')

hello()
#执行结果：
#Hello,world!

def printmore():
    print('该函数可以输出多条语句，我是第一条。')
    print('我是第二条')
    print('我是第三条')

printmore()  #调用函数
#执行结果：
#该函数可以输出多条语句，我是第一条。
#我是第二条
#我是第三条

def mixoperation():
    a=10
    b=20
    print(a)
    print(b)
    print(a+b)
    print('a+b的和等于:',a+b)

mixoperation()   #调用函数
#执行结果：
#10
#20
#30
#a+b的和等于: 30

def donothing():
	    pass

donothing()
#执行结果：什么也不显示
