# -*- coding: utf-8 -*-
# @Time    : 2020/11/30 上午11:12
# @Author  : Zstone
# @FileName: Bot_ding.py
# @Software: PyCharm

#  导入依赖库
# from apscheduler.schedulers.blocking import BlockingScheduler
# from datetime import datetime
import time
import hmac
import hashlib
import base64
import urllib.parse
import requests
import json

'''
对接钉钉消息通知
'''


def dingding():
    # 获取时间
    timestamp = str(round(time.time() * 1000))
    secret = 'SEC0f54b28f5ea9407eeb97d4df0f0d27b95631d6ee2a7a0c444f62975fc10d0039'  # 秘钥
    secret_enc = secret.encode('utf-8')  # encode格式
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    print(timestamp)
    print(sign)

    access_token = '574e451ea5a9979edf22b0ba904826652044d52871af6cc06dc93fa93151bde3'
    url = 'https://oapi.dingtalk.com/robot/send?' \
          'access_token={}&timestamp={}&sign={}'.format(access_token, timestamp, sign)
    print(url)

    # # 获取当前时间
    # str_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    # 发送的消息格式
    data = {
        "msgtype": "link",
        "link": {
            "text": "这就是展示的内容",
            "title": "时代的火车向前开",
            "picUrl": "",
            "messageUrl": "https://www.baidu.com"
        }
    }
    headers = {'Content-Type': 'application/json'}
    message = requests.post(url, json.dumps(data), headers=headers).json()
    print(message)


# def stag_request():
#     try:
#         access_token = '78a5497534adcfcef14cce21c19f5b7c4bf1dc44cb68c290a6fa3f1ad3c8bdbb'
#         stag_URL = 'https://oapi.dingtalk.com/robot/send'
#         data = {
#             "msgtype": "text",
#             "text": {
#                 "title": "测试已完成",
#                 "text": '1111111'
#             },
#             "at": {"atMobiles": ["17600972766"]},
#             "isAtAll": False
#         }
#         stag_r = requests.post(stag_URL, headers=write_header(), data=data)
#         # print(write_header())
#         stag_header = open("/Users/zhengshi/PycharmProjects/TestTools_Python/TeatData/load/Response", 'a')
#         print(json.loads(stag_r.text))
#         stag_dict = json.loads(stag_r.text)
#         print('Response Success, more detail read file named "Response"')
#         return json.dump(stag_dict, stag_header, indent=4, ensure_ascii=False)
#
#     except:
#         print("Fail, your headers maybe has something wrong")


if __name__ == "__main__":
    dingding()
