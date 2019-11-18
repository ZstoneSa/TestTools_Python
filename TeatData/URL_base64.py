# -*- coding: utf-8 -*-
# @Time    : 2019-07-18 14:04
# @Author  : Zstone
# @FileName: URL_base64.py
# @Software: PyCharm

import json
import os
import base64

def translation():
    note = input("Please input the data :")
    data_json = open('/Users/zhengshi/PycharmProjects/TestTools_Python/TeatData/decoding.json', 'w')
    try:
        data_change = note.replace("_", "/").replace("-", "+")
        data_base64_decode = base64.standard_b64decode(data_change).decode()
        data_loads = json.loads(data_base64_decode) #To python dic
        return json.dump(data_loads, data_json, indent=4, ensure_ascii=False)# dump for indent?

    except:
        print("Your data maybe not the code of base64")
        
if __name__ == '__main__':
    translation()
    os.open("/Users/zhengshi/PycharmProjects/TestTools_Python/TeatData/decoding.json", os.O_RDWR|os.O_CREAT)