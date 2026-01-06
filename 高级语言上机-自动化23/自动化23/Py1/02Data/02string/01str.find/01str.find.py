#4.3.1  str.find()方法
#语法：str.find(str,beg=0,end=len(string))
field='do it now'
index=field.find('do')
print(index)
#0
index=field.find('now')
print(index)
#6
index=field.find('python')
print(index)
#-1   #-1说明没找到
index=field.find('it',2)  #提供起点'   it now'
print(index)
#3
index=field.find('it',5)  #提供起点'      now'
print(index)
#-1   #-1说明没找到

index=field.find('it',0,3)  #提供起点和终点'do '
print(index)
#-1    #-1说明没找到
index=field.find('i',0,3)  #提供起点和终点'do '
print(index)
#-1    #-1说明没找到

index=field.find('it',0,5)  #提供起点和终点'do it'
print(index)
#3
index=field.find('it',5,10) #提供起点和终点' now'
print(index)
#-1    #-1说明没找到


