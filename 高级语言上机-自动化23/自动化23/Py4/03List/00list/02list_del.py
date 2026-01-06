#del删除第0,1,2,,,,n个元素
tring=['a','b','c','d','e']
print(tring)
#['a', 'b', 'c', 'd', 'e']
print(len(tring))  #len,共5个元素，下标=0,1,2,3,4
#5
del tring[1]
print('删除第二个元素之后：',tring)
#删除第二个元素之后： ['a', 'c', 'd', 'e']
print(len(tring))
#4

num=[1,2,3]
print(len(num))  #len,共3个元素，下标=0,1,2
#3
del num[2]
print('删除第3个元素后：',num)
#删除第3个元素后：[1, 2]
print(len(num))
#2
