# -*- coding: utf-8 -*-
# @Time    : 2019-08-21 12:27
# @Author  : Zstone
# @FileName: award_json.py
# @Software: PyCharm

import requests
import json

'''从文件中读取headers，并转为json格式将之返回 '''


def write_header():
    try:
        with open('/Users/zhengshi/PycharmProjects/TestTools_Python/TeatData/load/Request') as fin:
            valid = (line.split(': ', 1) for line in fin)
            data = {k: v.rstrip('\n') for k, v in valid}
            # print(data)
            return data

    except:
        print('Data Error')


'''通过request方法，请求接口，并将之写入Response文件中'''


def stag_request():
    try:
        stag_URL = 'http://h5.quickcan.cn/v1/payactivity/lottery/start?topic_id=4'
        data = {'activity_name': 'topic_lottery_202004'}
        stag_r = requests.post(stag_URL, headers=write_header(), data=data)
        # print(write_header())
        stag_header = open("/Users/zhengshi/PycharmProjects/TestTools_Python/TeatData/load/Response", 'a')
        print(json.loads(stag_r.text))
        stag_dict = json.loads(stag_r.text)
        print('Response Success, more detail read file named "Response"')
        return json.dump(stag_dict, stag_header, indent=4, ensure_ascii=False)

    except:
        print("Fail, your headers maybe has something wrong")


'''请求次数'''


def circle_times():
    note = input("Please input the lottery_times :")
    try:
        c_times = 0
        while c_times < int(note):
            stag_request()
            c_times = c_times + 1

        else:
            print('-----------------✅已请求: ' + str(c_times) + '次')
    except:
        print('Something wrong')


if __name__ == '__main__':
    # write_header()
    # stag_request()
    circle_times()

