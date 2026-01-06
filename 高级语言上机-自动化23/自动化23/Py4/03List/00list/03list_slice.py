print(list('女排夺冠了'))
#['女', '排', '夺', '冠', '了']
boil=list('女排夺冠了')
print(boil)
#['女', '排', '夺', '冠', '了']
show=list('hi,boy')
print(list(show))
#['h', 'i', ',', 'b', 'o', 'y']
show[3:]=list('man')#从[3]覆盖
print(show)
#['h', 'i', ',', 'm', 'a', 'n']
greeting=list('hi')
print(greeting)
#['h', 'i']
greeting[1:]=list('ello')#从[1]覆盖
print(greeting)
#['h', 'e', 'l', 'l', 'o']
field=list('ae')
print(field)
#['a', 'e']
field [1:1]=list('bcd')#从[1]插入
print(field)
#['a', 'b', 'c', 'd', 'e']
boil=list('女排夺冠了')
print(boil)
#['女', '排', '夺', '冠', '了']
boil[2:2]=list('2016年奥运会')#从[2]插入
print(boil)
['女', '排', '2', '0', '1', '6', '年', '奥', '运', '会', '夺', '冠', '了']
field=list('abcde')
print(field)
#['a', 'b', 'c', 'd', 'e']
field[1:4]=[]   #从[1]到[3]被清空
print(field)
#['a', 'e']
boil=list('女排2016年奥运会夺冠了')
print(boil)
#['女', '排', '2', '0', '1', '6', '年', '奥', '运', '会', '夺', '冠', '了']
boil[2:10]=[]   #从[2]到[9]被清空
print(boil)
#['女', '排', '夺', '冠', '了']
field=list('abcde')
print(field)
#['a', 'b', 'c', 'd', 'e']
del field[1:4]  #从[1]到[3]被清空
print(field)
#['a', 'e']
