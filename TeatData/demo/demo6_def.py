# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 4:11 下午
# @Author  : Zstone
# @FileName: demo6_def.py
# @Software: PyCharm

# 带参数的函数
def add2num(a, b):
    c = a + b
    return c


print(add2num(1, 2))


def divid(a, b):
    c = a + b
    d = a * b
    return c, d


ad, p = divid(3, 4)
print(ad, p)

