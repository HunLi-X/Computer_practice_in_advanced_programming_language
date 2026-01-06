#ord(字符)函数，把字符转换为十进制（Unicode编码）数字，
#或称：查看字符的(数字)Unicode编码

a=ord('a')
print(a,hex(a))
#97 0x61
print(type(a))
#<class 'int'>

b=ord('A')
print(b,hex(b))
#65 0x41
print(type(b))
#<class 'int'>

c=ord('学')#扩展到汉字，ok
print(c,hex(c))
#23398 0x5b66
print(type(c))
#<class 'int'>

'''
c=ord('学习')#扩展到两（多）个汉字，不可以
print(c,hex(c))
TypeError: ord() expected a character, but string of length 2 found
'''
e=ord('语')#扩展到汉字,嵩天p285,语的Unicode编码是8B ED,utf-8编码是E8 AF AD
print(e,hex(e))
#35821 0x8bed
print(type(e))
#<class 'int'>

f=ord('言')#扩展到汉字,嵩天p285,言的Unicode编码是8A 00,utf-8编码是E8 A8 80
print(f,hex(f))
#35328 0x8a00
print(type(f))
#<class 'int'>
