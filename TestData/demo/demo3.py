# -*- coding: utf-8 -*-
# @Time    : 2020/11/16 下午3:17
# @Author  : Zstone
# @FileName: demo3.py
# @Software: PyCharm


word = """
       lalalalal
       dudududud
       kukukukuk
"""

print(word)

# 特殊符号,转译
someWords = 'i2mababy'
print(someWords)
print(someWords[0:3])
# 步进值，0~7，每两个字符取一个
print(someWords[0:7:2])
# 爬虫一般会使用的字符串化
print(r"ni\nhao")
# 判断字符串是不是数字或数字
if someWords.isalnum():
    print('全部是数字或字母')
else:
    print('不全部是数字或字母')
# 判断字符串是不是字母
if someWords.isalpha():
    print('全部是字母')
else:
    print('不全部是字母')
# join(sep)字符串之间添加相同字符

# len长度

# lstrip的使用，去左空格

# rstrip的使用，去右空格

# split


