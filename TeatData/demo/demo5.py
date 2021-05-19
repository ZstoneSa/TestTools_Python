# -*- coding: utf-8 -*-
# @Time    : 2020/11/27 下午3:37
# @Author  : Zstone
# @FileName: demo5.py
# @Software: PyCharm


#   tuple 元组，元素不可修改

tup1 = ()    # 空，元组类型
tup2 = (10)  # int类型
tup3 = (10,)  # 元组类型
tup4 = (10, 20, 30)

print(type(tup4))

# 下标、切片
tup5 = ('11', '22', 33, 44, 55, 66)
print(tup5[0])
print(tup5[-1])
print(tup5[1:5])    # [1,5)

#   增
tup6 = ('11', 77)
tup = tup5 + tup6


#   元组，不可删，不可改
del tup  # 删除整个元组变量

# 对象变成元组，tuple()

'''字典,java称之为map，即为键值对'''
# key必须是唯一的
# 字典的定义
info = {"name": "zhengshi", "age": 18}

print(info)
print(info['name'])  # 直接访问，若没有这个key则会报错
# print(info['money'])
print(info.get('money'))  # 没有key这个键值时返回NONE
print(info.get('money', 'fun'))  # 没有key这个键值时返回默认值"fun"

# 字典，增
info['id'] = 94391247
print(info)

# 字典，删

del info['name']
print(info)  # 删除一个键值对

#  清空字典
# info.clear()

# 字典，改
info['age'] = 50
print(info)

# 字典，查
# 拿到所有的键key[list]
keys = info.keys()
print(keys)

# 拿到所有的值
print(info.values())

# 字典转列表，每个元素是一个元组
items = info.items()
print(info.items())

# 遍历所有的key
for key in keys:
    print(key, end='\t')

# 遍历所有键值对，无需变成元组即可循环遍历加入字典
for key, value in items:
    print('key=%s,value=%s' % (key, value))
    #  反之dict（[(),(),()]）列表中元组


# 使用枚举函数enumerate():
list2 = [11, 22, 33, 44, 55]
for i, x in enumerate(list2):
    print(i, x)


# 合并字典update()
dic1 = {'name': '111', 'bug': 23, 'what': 'happen'}
dic2 = {''}

# 集合：
s = set([1, 2, 3])
print(s)


