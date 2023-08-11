# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 12:06 下午
# @Author  : Zstone
# @FileName: demo7_file.py
# @Software: PyCharm

file = open('abtest.txt', 'w')  # 写入（write），不存在则会新建该文件

file.write('hello baby')

file.close()

''''''
file2 = open('abtest.txt', 'r')

c = file2.read(5)

''''''

file3 = open('abtest.txt', 'r')

content = file3.readlines()  # 一次性读取全部文件为列表，每行一个字符串

i = 1

for temp in content:
    print('%d:%s' % (i, temp))
    i += 1

file3.close()

''''''

import os

os.rename('abtest.txt', 'abtest_change.txt')

