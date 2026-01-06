#2.6.6  逻辑(布尔)运算符3个：
#          True  False
#and逻辑与(并且)：T and T=T; T and F=F; F and T=F; F and F=F;
#or 逻辑或(或者)：T  or T=T; T  or F=T; F  or T=T; F  or F=F;
#not逻辑非(反之)：  not T=F;   not F=T;

num =6
if num >=5 and num <= 10:
     print('num的值介于5到10之间')
else:
     print('num的值不介于5到10之间')
#num的值介于5到10之间
     
if num <5 or num > 10:
     print('num的值不介于5到10之间')
else:
     print('num的值介于5到10之间')
#num的值介于5到10之间

a=10
b=20
e=not a  #a=10 数值非0都是True
print(e)
#False
print(type(e))
#<class 'bool'>
g=not b  #b=20 数值非0都是True
print(g)
#False
h=not -1 #-1 数值非0都是True
print(h)
#False
print(not 0)#数值0=False 数值非0都是True
#True

print(not False)
#True
print(not True)
#False

################  数1 and 数2 没有意义，以下代码可以忽略不看     
a=10      #a=10=0000_1010b
b=20      #b=20=0001_0100b,【按位与】c=a & b=0000_1010b & 0001_0100b =0000_0000b;
c=a and b #两个数值a,b【逻辑与】a and b=b后者(右者)
print(c)
#20
print(type(c))
#<class 'int'>
c=b and a #两个数值a,b【逻辑与】b and a=a后者(右者)
print(c)
#10
print(type(c))
#<class 'int'>
d=a or b  #两个数值a,b【逻辑或】a or b=a前者(左者)
print(d)
#10
print(type(d))
#<class 'int'>
d=b or a  #两个数值a,b【逻辑或】b or a=b前者(左者)
print(d)
#20
print(type(d))
#<class 'int'>
