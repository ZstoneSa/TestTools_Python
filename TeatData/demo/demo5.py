# -*- coding: utf-8 -*-
# @Time    : 2020/11/27 下午3:37
# @Author  : Zstone
# @FileName: demo5.py
# @Software: PyCharm


#   tuple 元组，元素不可修改

tup1 = ()    # 空，元组类型
tup2 = (10)  # int类型
tup3 = (10,) # 元组类型
tup4 = (10, 20, 30)

print(type(tup4))

# 下标、切片
tup5 = ('11', '22', 33, 44, 55, 66)
print(tup5[0])
print(tup5[0])
print(tup5[1:5])    # [1,5)

#   增
tup6 = ('11', 77)
tup = tup5 + tup6


#   删
del tup  # 删除整个元组变量

#   改（不可改）


'''字典'''

# 字典的定义
info = {"name": "zhengshi", "age": 18}

print(info)
print(info['name'])
# print(info['money'])
print(info.get('money'))  # 没有key这个键值时返回NONE




