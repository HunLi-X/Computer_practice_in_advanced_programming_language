#6.5.4  elif子句
#! /usr/bin/python3
# -*- coding:UTF-8 -*-

num = 99
if num > 100:
    print('num的值大于100')
elif 90<=num<=100:
    print('num的值介于90到100之间，优')
elif 80<=num<=89:
    print('num的值介于80到89之间，良')
elif 70<=num<=79:
    print('num的值介于70到79之间，中')
    
elif 60<=num<=69:
    print('num的值介于60到69之间，及格')
else:
    print('num的值小于60，不及格')

#结果：
#num的值介于0到10之间


