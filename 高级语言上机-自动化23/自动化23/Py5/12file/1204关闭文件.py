#12.2.3  关闭文件
#! /usr/bin/python
# -*-coding:UTF-8-*-

path = './test1204.txt'
f_name = open(path, 'w')  #以写的方式打开一个文件，如果该文件不存在，新建之
print('write length:', f_name.write('Hello world!'))
f_name.close()

#write length: 12
#Hello world!
#012345678901

#! /usr/bin/python
# -*-coding:UTF-8-*-

path = './test1204.txt'
try:
    f_name = open(path, 'w')
    print('write length:', f_name.write('Hello world!!'))
finally:
    if f_name:
        f_name.close()
#write length: 13
		
#! /usr/bin/python
# -*-coding:UTF-8-*-

path = './test1204.txt'
with open(path, 'w') as f:
    f_name = open(path, 'w')
    print('write length:', f_name.write('Hello world!!!'))
    f_name.close()
#write length: 14	
	
	
