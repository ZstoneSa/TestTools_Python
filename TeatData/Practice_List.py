# -*- coding: utf-8 -*-
# @Time    : 2019-08-20 17:33
# @Author  : Zstone
# @FileName: Practice_List.py
# @Software: PyCharm

# 元素 & 数组（列）
person = ['name', 'face', 'eyes', 'nose', 'ears', True, 'more', 1]

print(person[0].title())  # title方法可以让字符串首字母大写

# 返回列表中各个位置的元素

print(person[-1], person[1], person[3]) # person[-1]为列序最后一个元素

# 元素插入返回的字符串

message = 'I have beautiful ' + str(person[2].title())  # int型元素无法使用title

print(message)


# 增 删 改

person.insert(0, 'legs')  # 自定义增加
person.append('end')      # 尾增加
del person[5]             # 自定义删
person[3] = 'Eyes'        # 自定义改

print(person)



