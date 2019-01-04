#!/usr/bin/env python
# -*- coding:utf-8-*-
#@author:蜜蜜
#@file: study_random1.py 
#@time: 2018/12/29 
#@email:1402686685@qq.com
import random

#随机小数
print(random.random())#>0且<1的小数
print(random.uniform(1,3))#>1且<3的小数

#随机整数
print(random.randint(1,5))#》1且《5的整数
print(random.randrange(1,10,2))#》1且《10的奇数

#随机选择一个返回
print(random.choice([1,'23',[4,5]]))# #1或者23或者[4,5]
#随机选择多个返回，返回的个数为函数的第二个参数
print(random.sample([1,'23',[4,5]],2)) # #列表元素任意2个组合


#打乱列表顺序
item=([1,3,5,7,9])
random.shuffle(item) # 打乱次序
print(item)

random.shuffle(item)
print(item)#打乱次序


'''生成随机验证码'''
import random

def v_code():
    code = ''
    for i in range(6):
        num=random.randint(0,9)
        alf=chr(random.randint(97,122))
        add=random.choice([num,alf])
        code="".join([code,str(add)])
    return code

print(v_code())





