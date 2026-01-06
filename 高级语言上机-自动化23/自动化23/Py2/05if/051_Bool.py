#6.5.1  布尔变量的作用
print(True)
#True
print(False)
#False
print(True == 1)
#True
print(False == 0)
#True
print(True+False+2)#True+False+2=1+0+2=3
#3
print(bool('good good study'))#将【非空字符串】强制类型转换为【布尔类型】
#True
print(bool(''))               #将【空字符串】强制类型转换为【布尔类型】
#False
print(bool(3))  #将【非0数字】强制类型转换为【布尔类型】
#True
print(bool(0))  #将【数字0】强制类型转换为【布尔类型】
#False
print(bool([1]))#将【非空列表】强制类型转换为【布尔类型】
#True
print(bool([]))#将【空列表】强制类型转换为【布尔类型】
#False
print(bool())  #将【空元组】强制类型转换为【布尔类型】
#False

