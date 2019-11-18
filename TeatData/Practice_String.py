# -*- coding: utf-8 -*-
# @Time    : 2019-08-20 15:14
# @Author  : Zstone
# @FileName: Practice_String.py
# @Software: PyCharm

# 换行 & 加空格

message = "languages:\n\tJava\n\tPythonn\n\tC++"

print(message)

# 去空格

message_space = ' python '

print(message_space.rstrip())  # 去字段尾
print(message_space.lstrip())  # 去字段首
print(message_space.strip())   # 去字段两边

# 简单的加减乘除

num_plus = 1 + 2
num_minus = 4 - 2
num_times = 3 * 4
num_into = 2 / 4
num_square = 2 ** 3  # 乘方
num_root = 9 ** 0.5  # 开根

print(num_plus, num_minus, num_times, num_into, num_square, num_root)

# 数字强转为string类型

age = 24
message_birth = 'Thanks for my ' + str(age) + 'th Birthday!'

print(message_birth)

# 取整 & 精确相除

num_round = 3 // 2
num_float = 3.0 / 2

print(num_round, num_float)

# python of zen
import this





