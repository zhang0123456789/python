#!/usr/bin/env python
# -*- coding:utf-8-*-
#@author:蜜蜜
#@file: 旋转.py 
#@time: 2019/06/02 
#@email:1402686685@qq.com
from PIL import Image

# dir =r"F:\photo"
#图片旋转
def rotateimg():

    img=Image.open("Chrysanthemum.jpg")
    print(img.size)
    img.show()
    img2=img.rotate(90)
    print(img2.size)
    img2.show()
    img2.save("Chrysanthemum1.jpg")

rotateimg()









