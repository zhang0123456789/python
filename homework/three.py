#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/3 21:52
# d={"广东":["深圳","广州","阳江"],
#    "湖南":["长沙","益阳","怀化"],
#    "湖北":["武汉","襄阳","黄冈"]}
# p=input("请输入省份:")
# if p in d:
#     print("可选择的城市是：",d[p])
#     c=input("请输入城市:")
#     if c in d[p]:
#         print("你选择了:{}省{}市:".format(p,c))
#     elif p not in d or c not in d[p]:
#         print("省份不存在 或者是城市不存在")
# else:
#         print("输入错误 终止程序")

d={"广东":["深圳","广州","阳江"],
   "湖南":["长沙","益阳","怀化"],
   "湖北":["武汉","襄阳","黄冈"]}
p=input("请输入省份:")
if p in d:
    print("可选择的城市是：",d[p])
    c=input("请输入城市:")
    if c in d[p]:
        print("你选择了:{}省{}市:".format(p,c))
    elif p not in d or c not in d[p]:
        print("输入错误 终止程序")



