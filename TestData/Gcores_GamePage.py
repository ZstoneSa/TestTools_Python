# -*- coding: utf-8 -*-
# @Time    : 2023/12/15 12:03
# @Author  : Zstone
# @FileName: Gcores_GamePage.py
# @Software: PyCharm


import requests
import json


def key_values_to_dic(key_values_):
    """
    将键值对转换为字典形式
    """
    key_values_dic_ = {}
    for line in key_values_.split("\n"):
        line = line.strip()
        if not line:
            continue
        try:
            key, value = line.split(":", 1)
            key = key.strip()
            key_values_dic_[key] = value
        except ValueError:
            print("ERROR: 键值对错误，转换失败", line)
    return key_values_dic_


# 测试环境
key_values = """
Host: www.game-cores.com:443
Accept: application/vnd.api+json
Authorization: Token eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJ1c2VyX2lkIjo1ODIzOTgsImF1dGhfdG9rZW4iOiJ5MWc3ajF2dkpzeGJDTS1WQnlIREpRIn0.lVVM3Fye2ZL8NrudTcEuHDe4688_vXOXRcBuQ4G1SIH6pRJu9UT7s8ekQjMbQx_NWKltv7V7ClYrnnZRJGjDDw
"""
# print(key_values_to_dic(key_values))


def request_url():
    # URL为测试环境
    stag_url = 'https://www.game-cores.com:443/gapi/v1/entries/701?include=tags,involvements.entity.user,topics.operational-events.giveaways,topics.operational-events.public-candidates,topics.linked-videos,topics.linked-articles,topics.linked-radios,game-links,public-rate-discussions.recommend-poll-options.recommend-comments.user&from-app=1'
    # headers
    stag_headers = key_values_to_dic(key_values.replace(": ", ":"))
    # 如果需要URL后填写入参，参考下列
    stag_query = {'include': 'tags,involvements.entity.user,topics.operational-events.giveaways,topics.operational-events.public-candidates,topics.linked-videos,topics.linked-articles,topics.linked-radios,game-links,public-rate-discussions.recommend-poll-options.recommend-comments.user'}
    stag_r = requests.get(stag_url, headers=stag_headers, params=stag_query)
    # print(key_values_to_dic(key_values.replace(": ", ":")))
    print(stag_r.status_code)
    stag_header = open("/Users/zhengshi/PycharmProjects/TestTools_Python/TestData/load/Response.txt", 'a')

    stag_dict = json.loads(stag_r.text)

    # 从数据结构层级中获取某个key的value值
    game_comment = stag_dict['included'][12]['attributes']['body']
    print('Response Success, more detail read file named "Response"')
    return game_comment


'''请求次数'''


def request_times():
    note = input("Please input the request almost times :")
    c_times = 0
    game_comment_list = []
    while c_times < int(note):
        game_comment_list.append(request_url())
        c_times = c_times + 1

    else:
        print(game_comment_list)
        dict_comment = {}
        for key in game_comment_list:
            dict_comment[key] = dict_comment.get(key, 0) + 1
        stag_header = open("/Users/zhengshi/PycharmProjects/TestTools_Python/TestData/load/Response.txt", 'a')
        print('FINISH✅\n' + '-----------------已请求: ' + str(c_times) + '次-----------------')
        return json.dump(dict_comment, stag_header, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # 多次请求接口
    request_times()

    # 单次请求
    # request_url()
