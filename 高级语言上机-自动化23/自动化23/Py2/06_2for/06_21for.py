#6.6.2  for循环
n=0
fields=['a','b','c']   #列表
while n<len(fields):   #len(fields)=3,n<3,n=0,1,2
    print('当前字母是：',fields[n])
    n += 1  #n=n+1,n=1,2,3
#结果：
#当前字母是： a
#当前字母是： b
#当前字母是： c

fields=['a','b','c']   #列表
for f in fields:       #fields列表名
    print('当前字母是：',f)
#结果：
#当前字母是： a
#当前字母是： b
#当前字母是： c

print('-----for循环字符串-----------')	
for letter in 'good':    #for循环字符串
   print ('当前字母 :', letter)
#-----for循环字符串-----------
#当前字母 : g
#当前字母 : o
#当前字母 : o
#当前字母 : d
   
print('-----for循环数字序列-----------')	
number=[1,2,3]
for num in  number:    #for循环数字序列
    print('当前数字：',num)
#-----for循环数字序列-----------
#当前数字： 1
#当前数字： 2
#当前数字： 3
    
print('-----for循环字典-----------')
abcs={'name':'小智','number':'1002'}
for abc in abcs:   #for循环字典
    print('%s:%s' % (abc,abcs[abc]))
#-----for循环字典-----------
#name:小智
#number:1002
