# -*- coding: utf-8 -*-
# @Time    : 2020/11/16 下午4:19
# @Author  : Zstone
# @FileName: demo4.py
# @Software: PyCharm


# import random
#
# # 数组for循环遍历
# list1 = ["11", "22", "33"]
# for i in list1:
#     print(i)
#
# print("-----华丽分隔符-----")
# # 数据增删改查
#
# list1.append('44')
# for i in list1:
#     print(i)
# print("-----华丽分隔符-----")
# # 将列表作为一个元素添加到列表里
# a = ['55', '66']
# list1.append(a)
# for i in list1:
#     print(i)
#
# print("-----华丽分隔符-----")
# # 将列表中每个元素逐一追加到列表中
# b = ['77', '88']
# list1.extend(b)
# for i in list1:
#     print(i)
#
# # 插入insert(index:a, object)
# c = [1, 2, 3, 4]
# c.insert(2, 2)
# print(c)
#
# # del删除指定下表元素
# del c[2]
#
# # pop弹出最后一个元素
# c.pop()
#
# # remove删除找到的指定元素（仅第一个）
# c.remove(3)
# print(c)
#
# # 直接修改元素
# c[0] = 5
# print(c)
#
# # 多个列表,查询
# s = [["1", ['11', '22'], "3"], ["11", "22", "33"]]
# print(s[0][1][1])
#
# # 将一个列表中的元素随机添加到空列表,查询空列表中每个列表的具体数量，以及每个列表中的元素名称
#
# data = ['1', '2', '3', '4', '5', '6', '7', '8']
# list2 = [[], [], []]
#
# for number1 in data:
#     index = random.randint(0, 2)    # 生成随机数
#     list2[index].append(number1)    # 将data中遍历的元素，根据list2的随机下标分别填入数组中
# print(list2)
#
# i = 0
# for number2 in list2:
#     print("列表%d，元素数量为:%d" % (i, len(number2)))   # 通配符打印
#     i += 1
#
#     for name in number2:
#         print('元素：%s.' % name, end='\t')
#
#     print('^'*20)

#   打印一个商品列表
# 循环询问商品，打印购物车，Q中止循环计算总价格
products = [['apple', 5], ['banana', 10], ['water', 2], ['orange', 7]]  # 一个包含所有商品名称和价格的列表
i = 0
print('-'*4,'商品名称', '-'*4)
for product in products:    # 循环遍历所有商品元素
    print("%d %s %d" % (i, product[0], product[1]))  # 打印元素
    i += 1

answerQuestion = ''
gouWu = []
n = 0
price = 0

while len(products):
    try:
        answerQuestion = input("欢迎购物，请输入您要购买的商品编号加入购物车（结算查看商品请输入Q）：")
        if answerQuestion.isdigit() and int(answerQuestion) < 4:
            gouWu.append(products[int(answerQuestion)])
            print("已加入购物车「商品：%s，单价：%d」" % (products[int(answerQuestion)][0], products[int(answerQuestion)][1]), end='\n')

        elif answerQuestion.isalpha() and answerQuestion == 'Q':
            print('-' * 4, '购物车名单', '-' * 4)
            for product_buy in gouWu: # 从购物车中遍历
                ProName = product_buy[0]
                ProPrice = product_buy[1]
                print("%d %s %d" % (n, ProName, ProPrice))
                price += ProPrice
                n += 1
            print('已购买%d个商品，总价为%d' % (n, price))
            break


    except():
        print('输入有误，不存在该商品编号')

