'''groupby_test_auto.py从1个xlsx文件自动识别所有部门+按部门拆分为多个xlsx文件
https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html
功能： 从'部门'列取该列所有行的cell，组成series，转换为列表，
      再转换为集合，再转换回列表，以列表元素拆分为几个小xlsx文件
'''
import numpy as np
import pandas as pd
colname='部门'   # 从'部门'列，拆分为若干个xlsx文件
mydf=pd.read_excel('groupby_test_auto_中原工学院教职工名单.xlsx')
print(mydf)
#请同学们继续编写下面的源程序
