#06_21for_in_range.py

for i in range(3):  #0,1,2
    print('i=',i)
#i= 0
#i= 1
#i= 2
    
for i in range(3,6):#3,4,5
    print('i=',i)
#i= 3
#i= 4
#i= 5

for i in range(3,6,2):#从3到5，步进2
    print('i=',i)
#i= 3
#i= 5

for c in "Python123":  #字符串
    print(c,end=",")
#P,y,t,h,o,n,1,2,3,

for c in [123,'Python',456]:  #列表
    print(c,end=",")
#123,Python,456,
