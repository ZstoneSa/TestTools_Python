# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 下午12:37
# @Author  : Zstone
# @FileName: gzip-decode.py
# @Software: PyCharm


import json
import base64
import gzip
from io import BytesIO


def translation():

    note = input("Please input the data :")
    data_base64_decode = base64.b64decode(note)
    print("\n------ ✅ 格式化：Base64 & JSON")
    return data_base64_decode


def judge_event_name():
    data_json = open('/TestData/decoding.json', 'r')
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

        with open('/TestData/load/Sensor_Event') as fin:
            event_list = []
            for data in fin:
                event_list.append(data.rstrip('\n'))
            # print(event_list)
        return event_list
    except:
        print('打开文件失败，该文件不存在或文件名错误')


def gzip_decompress(buf):
    data = open('/TestData/decoding.json', 'w')
    obj = BytesIO(buf)
    with gzip.GzipFile(fileobj=obj) as f:
        result = f.read().decode('utf-8')
    print(type(result))
    print(result)
    return json.dump(result, data, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # s = "H4sIAAAAAAAAE4vmUlCoBmIFBaWCovyC1KKSzNRiJQUrqCBQOCS/IDPZ0wUkZqgDE3TOz4UJGsAFVfLBOpUy/YOV4IJuiZk5QamJxfl5YLlnc3qfdi18OnPFs1lNz6Zve7Kj92n/+udTVui8WL/9+YrepxP6Xrb3vlg/VQmsvxZijFJJZUEqWHtJUWJythJMNDMXLGpoZmBqYWJiamRqbmQBlUstS80rAWsJdvEG2p8CdjHI1FquWADuiwNE9QAAAA=="
    # b = bytes(s, encoding="utf-8")
    gzip_decompress(translation())
    # os.open("/Users/zhengshi/PycharmProjects/TestTools_Python/TestData/decoding.json", os.O_RDWR|os.O_CREAT)

