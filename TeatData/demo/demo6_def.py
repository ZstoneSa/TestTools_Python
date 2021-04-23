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


# 给两个对象赋值
ad, p = divid(3, 4)
print(ad, p)


def line():
    a = "-----------"
    return a


print(line())


def line2(n):
    Tline = ''
    a = 1
    while a != n:
        Tline = Tline + line() + '\n'
        a += 1
    return Tline


print(line2(5))


def total1(a, b, c):
    t = a + b + c
    return t


def ave(a, b, c):
    a = total1(a, b, c) / 3.0
    return a


print(ave(10, 20, 30))








