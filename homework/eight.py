#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/21 22:15

'''编写一个函数实现大写转小写，小写变大写，并且转换为镜像字符串，
并且将字符串变为镜像字符串。 例如：’A’变为’Z’,’b’变为’y
示范字符串： ”sdSdsfdAdsdsdfsfdsdASDSDFDSFa”字符串大写变小写 小写变大写。'''

class Letter:
    def __init__(self,str_1):
        self.str_1=str_1

    @staticmethod
    def change(a):
        print("大写转小写，小写变大写：",a.swapcase())

    @staticmethod
    def mirror(b):
        b1=b
        for i in b :
            if i.islower():
                c=chr(219-ord(i))
                b1+=c
            if i.isupper():
                c=chr(155-ord(i))
                b1+=c
        print("镜像字符串：",b1)

L1=Letter('abcd')
L1.change('sdSdsfdAdsdsdfsfdsdASDSDFDSFa')
L1.mirror('sdSdsfdAdsdsdfsfdsdASDSDFDSFa')

