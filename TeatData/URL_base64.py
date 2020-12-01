# -*- coding: utf-8 -*-
# @Time    : 2019-07-18 14:04
# @Author  : Zstone
# @FileName: URL_base64.py
# @Software: PyCharm

import json
import base64


def translation():

    try:
        note = input("Please input the data :")
        data_json = open('/Users/zhengshi/PycharmProjects/TestTools_Python/TeatData/decoding.json', 'w')
        data_change = note.replace("_", "/").replace("-", "+")
        data_base64_decode = base64.standard_b64decode(data_change).decode()
        data_loads = json.loads(data_base64_decode) #To python dic
        print("\n------ ✅ 格式化：Base64 & JSON")
        return json.dump(data_loads, data_json, indent=4, ensure_ascii=False)# dump for indent?


    except:
        print("Your data maybe not the code of base64")


def judge_event_name():
    data_json = open('/Users/zhengshi/PycharmProjects/TestTools_Python/TeatData/decoding.json', 'r')
    data_dict = json.loads(data_json.read())

    try:
        '''——————此处更改事件名称校验👇——————'''
        if data_dict['event'] in read_event():
            print("------ ✅ 事件名：'" + data_dict['event'] + "'，校验成功")

        else:
            print("------ ❌ 事件名：" + data_dict['event'] + " 该「事件」不符合需求！")

    except:
        print("------ ❌ 数据异常，并非事件上报")


def read_event():
    try:

        with open('/Users/zhengshi/PycharmProjects/TestTools_Python/TeatData/load/Sensor_Event') as fin:
            event_list = []
            for data in fin:
                event_list.append(data.rstrip('\n'))
            # print(event_list)
        return event_list
    except:
        print('打开文件失败，该文件不存在或文件名错误')


if __name__ == '__main__':

    translation()
    judge_event_name()
    # os.open("/Users/zhengshi/PycharmProjects/TestTools_Python/TeatData/decoding.json", os.O_RDWR|os.O_CREAT)

