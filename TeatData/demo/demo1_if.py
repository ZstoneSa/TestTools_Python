# -*- coding: utf-8 -*-
# @Time    : 2020-11-12 18:38
# @Author  : Zstone
# @FileName: demo1_if.py
# @Software: PyCharm

'''
a = int(input("data:"))
print(type(a))
print('output:%d'%a)
'''
if True:# >1数字或True ，都判断为真，反之False同理
    print("1")
else:
    print("2")

issues = 6

if issues >= 0 and issues <= 10:
    print('quality level is A')
elif issues > 10 and issues <= 20:
    print('quality level is B')


import random

x = random.randint(1, 100)  # [1,100]
print(x)

shouShi = random.randint(0, 2)
if shouShi == 0:
    print('剪刀(%d)' % shouShi)
elif shouShi == 1:
    print('石头(%d)' % shouShi)
elif shouShi == 2:
    print('布(%d)' % shouShi)