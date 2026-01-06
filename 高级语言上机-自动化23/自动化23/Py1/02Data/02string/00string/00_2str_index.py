#字符串索引index,最左从0开始，最右从-1开始
#index= 0 1 2 , , ,  n
#index=-n,,,,,-3 -2 -1
#Python采用Unicode编码，中文汉字、英文字母、数字，都当一个字符，占3个字节。
str='零一二三四五ab89'
print(str[0],str[1],str[2],str[3],str[4],str[5],str[6],str[7],str[8],str[9])
#零 一 二 三 四 五 a b 8 9

print(str[-10],str[-9],str[-8],str[-7],str[-6],str[-5],str[-4],str[-3],str[-2],str[-1])
#零 一 二 三 四 五 a b 8 9

print(str[10])  #越界，报错
#
print(str[-11])  #越界，报错
#
