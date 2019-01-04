#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/12/4 21:48

'''读取所有数据'''
# import pandas as pd
# df=pd.read_excel("python14.xlsx",sheet_name='Sheet1')
# res=df.values
# print('res:',res)

'''读取某行的数据    #默认第一行为A,B,C,D,E.......直接读取第二行数据'''
# import pandas as pd
# df=pd.read_excel("python14.xlsx",sheet_name='Sheet1')
# res=df.ix[0].values
# print('res:',res)   #返回的是第二行数据

'''读取某行的数据    #给第一行添加为A,B,C,D,E.......读的是第一行数据'''
# import pandas as pd
# df=pd.read_excel("python14.xlsx",sheet_name='Sheet1')
# res=df.ix[0].values  #从0开始数的
# print('res:',res)   #返回的是第一行数据

'''读取第三行的数据'''
import pandas as pd
df=pd.read_excel("python14.xlsx",sheet_name='Sheet1')
res=df.ix[3].values  #从0开始数的
print('res:',res)   #返回的是第三行数据

'''读取多行的数据  使用嵌套列表'''
# import pandas as pd
# df=pd.read_excel("python13.xlsx",sheet_name='Sheet1')
# res=df.ix[[1,2]].values  #从0开始数的
# print('res:',res)   #返回的是第二、三行数据

'''读取指定的列的数据'''
# import pandas as pd
# df=pd.read_excel("python13.xlsx",sheet_name='Sheet1')
# res=df['C'].values  #从0开始数的
# print('res:',res)   #返回的是第二、三行数据


'''拓展pandas读书节  写数据无能为力
openpyxl'''