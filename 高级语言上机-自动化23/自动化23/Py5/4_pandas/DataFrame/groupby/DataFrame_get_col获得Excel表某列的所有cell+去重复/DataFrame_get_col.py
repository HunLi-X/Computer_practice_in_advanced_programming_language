'''DataFrame_get_col.py获得Excel表某列的所有cell+去重复
DataFrame_get_col.py获取指定列的所有cell(行、格、元素)
'''
import numpy as np
import pandas as pd
mydf=pd.read_excel('groupby_test.xlsx')
print(mydf)
'''
    工号  姓名  部门   职位    薪酬
0    1  管1  管理   经理  8000
1    2  研1  研发  工程师  9999
2    3  生1  生产   工人  6666
3    4  管2  管理   经理  8000
4    5  研2  研发  工程师  9999
5    6  生2  生产   工人  6666
6    7  管3  管理   经理  8000
7    8  研3  研发  工程师  9999
8    9  生3  生产   工人  6666
9   10  管4  管理   经理  8000
10  11  研4  研发  工程师  9999
11  12  生4  生产   工人  6666
'''
mycol=mydf['部门']
print(mycol)
'''
0     管理
1     研发
2     生产
3     管理
4     研发
5     生产
6     管理
7     研发
8     生产
9     管理
10    研发
11    生产
'''
print(type(mycol))
'''
Name: 部门, dtype: object
<class 'pandas.core.series.Series'>
'''
mylist=list(mycol)
print(mylist)
#['管理', '研发', '生产', '管理', '研发', '生产', '管理', '研发', '生产', '管理', '研发', '生产']
print(type(mylist))
#<class 'list'>
myset=set(mylist)
print(myset)
#{'管理', '研发', '生产'}

print(type(myset))
#<class 'set'>
