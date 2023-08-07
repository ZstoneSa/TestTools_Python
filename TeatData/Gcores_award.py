# -*- coding: utf-8 -*-
# @Time    : 2019-08-21 12:27
# @Author  : Zstone
# @FileName: award_json.py
# @Software: PyCharm

import requests
import json


def key_values_to_dic(key_values_):
    """
    将键值对转换为字典形式
    :param key_values_:
    :return:
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


key_values = """
Host: www.gcores.com
Content-Type: application/vnd.api+json
Accept: application/vnd.api+json
User-Agent: GcoresMobile/910 CFNetwork/1406.0.4 Darwin/22.4.0
Connection: keep-alive
baggage: sentry-environment=production,sentry-transaction=gcores.TopicNG,sentry-public_key=54114cac2d09482db1440ce9976a4778,sentry-trace_id=70db06478cf945b4a16768454f967cfc,sentry-sample_rate=0.1
Accept-Language: zh-CN,zh-Hans;q=0.9
Authorization: Token eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJ1c2VyX2lkIjo1ODIzOTgsImF1dGhfdG9rZW4iOiJ5MWc3ajF2dkpzeGJDTS1WQnlIREpRIn0.RRJYd_kI-5WLEpRG0GJusr-qx1slbz9hxWUER20IkxPy4rdSVJ2HGiK_DQ28jqv3Bg5ysiXt0y4uhJSzxPbl0w
Accept-Encoding: gzip, deflate, br
sentry-trace: 70db06478cf945b4a16768454f967cfc-90d72b97aa1d8757-0
"""
# print(key_values_to_dic(key_values))


def get_times():
    stag_url = 'https://www.gcores.com/gapi/v1/grpg-reward-pools/8/activate-free-pulls'
    # 如果需要URL后填写入参，参考下列
    # data = {'activity_name': 'topic_lottery_202004'}
    stag_r = requests.post(stag_url, headers=key_values_to_dic(key_values.replace(": ", ":")))
    # print(key_values_to_dic(key_values.replace(": ", ":")))
    print(stag_r.status_code)
    stag_header = open("/Users/zhengshi/PycharmProjects/TestTools_Python/TeatData/load/Response", 'a')
    stag_dict = json.loads(stag_r.text)
    print('Response Success, more detail read file named "Response"')
    return json.dump(stag_dict, stag_header, indent=4, ensure_ascii=False)


def check_times():
    try:
        stag_url = 'https://www.gcores.com/gapi/v1/grpg-reward-pools/8'
        stag_r = requests.get(stag_url, headers=key_values_to_dic(key_values.replace(": ", ":")))
        print(stag_r.status_code)
        stag_header = open("/Users/zhengshi/PycharmProjects/TestTools_Python/TeatData/load/Response", 'a')
        print(json.loads(stag_r.text))
        stag_dict = json.loads(stag_r.text)
        print('Response Success, more detail read file named "Response"')
        return json.dump(stag_dict, stag_header, indent=4, ensure_ascii=False)

    except:
        print("Fail, your headers maybe has something wrong")


def award():

    stag_url = 'https://www.gcores.com/gapi/v1/grpg-reward-pools/8/pull'
    stag_r = requests.post(stag_url, headers=key_values_to_dic(key_values.replace(": ", ":")))
    print(stag_r.status_code)
    # print(key_values_to_dic(key_values.replace(": ", ":")))
    stag_header = open("/Users/zhengshi/PycharmProjects/TestTools_Python/TeatData/load/Response", 'a')
    stag_dict = json.loads(stag_r.text)
    print(stag_dict)
    return json.dump(stag_dict, stag_header, indent=4, ensure_ascii=False)


'''请求次数'''


def award_times():
    note = input("Please input the lottery_times :")
    try:
        c_times = 0
        while c_times < int(note):
            award()
            c_times = c_times + 1

        else:
            # print('-----------------✅已请求: ' + str(c_times) + '次')
            print("结束请求，查看Response结果")
    except:
        print('Something wrong')


if __name__ == '__main__':
    # 多次抽奖
    award_times()

    # 获取抽奖次数
    # get_times()

    # 查看抽奖次数
    # check_times()

    # 单次抽奖
    # award()