'''
Excel
详见 Excel 文档:
https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-excel
将DataFrame写入 Excel 文件：
'''
import numpy as np
import pandas as pd
df=pd.DataFrame({'A':[11,21,31,41,51,61],
	'B':[12,22,32,42,52,62],
	'C':[13,23,33,43,53,63],
	'D':[14,24,34,44,54,64]})
print(df)
'''
    A   B   C   D
0  11  12  13  14
1  21  22  23  24
2  31  32  33  34
3  41  42  43  44
4  51  52  53  54
5  61  62  63  64
'''
df.to_excel('DataFrame_32读写Excel文件.xlsx', sheet_name='Sheet1')

#读取 Excel 文件到DataFrame：

myread=pd.read_excel('DataFrame_32读写Excel文件.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
print(myread)
'''
   Unnamed: 0   A   B   C   D
0           0  11  12  13  14
1           1  21  22  23  24
2           2  31  32  33  34
3           3  41  42  43  44
4           4  51  52  53  54
5           5  61  62  63  64
'''


