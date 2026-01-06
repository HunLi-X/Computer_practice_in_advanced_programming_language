#complex，复数，a+bj，实部a，虚部b，complex(a,b)
c=complex(1,1)
print(c)
#(1+1j)

a=2
b=2
c1=complex(a,b)
print(c1)
#(2+2j)

a=3.0
b=3.0
c2=complex(a,b)
print(c2)
#(3+3j)      #为什么不是(3.0+3.0j)
print(type(c2))
#<class 'complex'>

a=1.1
b=1.1
c3=complex(a,b)
print(c3)
#(1.1+1.1j)
print(type(c3))
#<class 'complex'>

c4=c2+c3
print(c4)
#(4.1+4.1j)
print(type(c4))
#<class 'complex'>

