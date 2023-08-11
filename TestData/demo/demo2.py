# -*- coding: utf-8 -*-
# @Time    : 2020-11-13 14:50
# @Author  : Zstone
# @FileName: demo2.py
# @Software: PyCharm


import time

'''
for i in range(0,12,4):   #从0开始，依次+4，直到>=12停止，步进值
    print(i)
'''
'''
name = 'Beijing'

for i in name:
    print(i, end='\t')# end->末尾添加

a = ['aa', 'bb', 'cc']

for i in range(0, len(a)): #长度从0到a的元素总数
    print(i, a[i])

i = 0
while i < 5:
    # 循环数量
    print("这是第%d次循环" % (i+1))
    print("当前i为%d" % i)
    i += 1

sumNum = 0
Num = 100
counter = 1

while counter <= Num:
    sumNum += counter
    counter += 1
    print('当前执行第%d次，总和为%d' % (counter, sumNum))
    # 元组形式

i = 0
while i < 5:
    print('i=%d,i<5' % i)
    i += 1
else:
    print('i=%d,i> or =5' % i)

n = 0
while n < 10:
    n += 1
    print('='*30)
    if n == 5:
        # 在5时截断输出
        break
    print(n)


g = 0
while g < 10:
    g += 1
    print('='*30)
    if g == 5:
        # 跳过5这个输出
        continue
    print(g)
'''
'''99乘法表'''
# for i in range(1, 10):
#     # range的范围是[1,10)不包含10，只到9，因此需要+1
#     for i2 in range(1, i+1):
#         print('%d*%d=%d' % (i, i2, i*i2), end='\t')
#     print(end='\n')

# n = 1
# while n < 10:
#     n2 = 1
#     while n2 < n+1:
#         print('%d*%d=%d' % (n, n2, n*n2), end='\t')
#         n2 += 1
#     print('\n')
#     n += 1




# print("---RUNOOB EXAMPLE ： Loading 效果---")
#
# print("Loading", end="")
# for i in range(20):
#     print(".", end='', flush=True)
#     time.sleep(0.5)

