#12.2.1  文件读和写
#! /usr/bin/python
# -*-coding:UTF-8-*-

path = './test1202.txt'

f_name = open(path,'r')  #'r'以只读方式打开文件
print('read result:', f_name.read(12))
#执行结果：
#read result: Hello world!

path = './test1202.txt'
f_name = open(path, 'w') #'w'以写入方式打开文件
print('write length:', f_name.write('Hello world!'))
#执行结果：
#write length: 12


f_name = open(path,'r')  #'r'以只读方式打开文件
print('read result:', f_name.read())
#执行结果：
#read result: Hello world!

path = './test1202.txt'

f_name = open(path, 'w')
print('write length:', f_name.write('Hello world!'))
f_name = open(path,'r')
print('read result:', f_name.read())

f_name = open(path, 'a')
print('add length:', f_name.write('welcome!'))
f_name = open(path,'r')
print('read result:', f_name.read())
'''
执行结果：
write length: 12
read result: Hello world!
add length: 8
read result: Hello world!welcome!
'''

f_name = open(path, 'w')
print('write length:', f_name.write('Hello world!'))
f_name = open(path,'r')
print('read result:', f_name.read())

f_name = open(path, 'a')
print('add length:', f_name.write('welcome!'))
f_name = open(path,'r')
print('read result:', f_name.read())
'''
执行结果：
write length: 12
read result: Hello world!

add length: 8
read result: Hello world!welcome!
'''

