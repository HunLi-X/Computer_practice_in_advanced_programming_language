'''
groupby_test.py_从1个xlsx文件搜索某（指定）部门员工另存为1个xlsx文件
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
print(type(mydf))
#<class 'pandas.core.frame.DataFrame'>

mygroup=mydf.groupby('部门')
print(mygroup)
'''
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x00000213FEEF90F0>
'''
print(type(mygroup))
#<class 'pandas.core.groupby.generic.DataFrameGroupBy'>
mygroup=mydf.groupby('部门').get_group('管理')
mygroup.to_excel('groupby_test_管理.xlsx')
print(mygroup)
'''
0   1  管1  管理  经理  8000
3   4  管2  管理  经理  8000
6   7  管3  管理  经理  8000
9  10  管4  管理  经理  8000
'''
mygroup=mydf.groupby('部门').get_group('研发')
mygroup.to_excel('groupby_test_研发.xlsx')

mygroup=mydf.groupby('部门').get_group('生产')
mygroup.to_excel('groupby_test_生产.xlsx')
