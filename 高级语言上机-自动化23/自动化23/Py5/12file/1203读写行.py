#12.2.2  读写行
#! /usr/bin/python
# -*-coding:UTF-8-*-

path = './test1203.txt'
f_name = open(path, 'w')
f_name.write('Hello world!\n')
f_name = open(path, 'a')
f_name.write('welcome!')
f_name = open(path,'r')
print('readline result:', f_name.readline())

#执行结果：
#readline result: Hello world!


#! /usr/bin/python
# -*-coding:UTF-8-*-

path = './test1203.txt'
f_name = open(path, 'w')
str_list = ['Hello world!\n', 'welcome!\n', 'welcome!\n']
print('write length:', f_name.writelines(str_list))
f_name = open(path,'r')
print('read result:', f_name.read())
f_name = open(path,'r')
print('readline result:', f_name.readlines())

#执行结果：
#write length: None
#read result: Hello world!
#welcome!
#welcome!

#readline result: ['Hello world!\n', 'welcome!\n', 'welcome!\n']



