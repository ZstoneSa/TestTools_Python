# -*- coding: utf-8 -*-
# @Time    : 2019-07-18 11:32
# @Author  : Zstone
# @FileName: Test_Prectise.py
# @Software: PyCharm

import base64
import json
import pprint


def translation():
    #note = input('Please input data_value :')
    note = 'eyJkaXN0aW5jdF9pZCI6IjEyMDAwNTA5MiIsImxpYiI6eyIkbGliIjoianMiLCIkbGliX21ldGhvZCI6ImNvZGUiLCIkbGliX3ZlcnNpb24iOiIxLjYuNTEifSwicHJvcGVydGllcyI6eyIkb3MiOiJpT1MiLCIkbW9kZWwiOiJpcGhvbmUiLCIkb3NfdmVyc2lvbiI6IjEyLjMiLCIkc2NyZWVuX2hlaWdodCI6ODEyLCIkc2NyZWVuX3dpZHRoIjozNzUsIiRsaWIiOiJqcyIsIiRsaWJfdmVyc2lvbiI6IjEuNi41MSIsIiRicm93c2VyIjoid2VidmlldyIsIiRicm93c2VyX3ZlcnNpb24iOiItMSIsIiRsYXRlc3RfcmVmZXJyZXIiOiIiLCIkbGF0ZXN0X3JlZmVycmVyX2hvc3QiOiIiLCJINVBhZ2UiOiJodHRwczovL2g1Lmt1YWlrYW5tYW5odWEuY29tL2F3YXJkX21lbWJlcj9jb25mMmZ1bGxzY3JlZW49MSZjb25mMnNjcm9sbHdoaXRlYXJlYT0xJm9yaWdpbj12aXBzaGl5b25nJm5vbl9pYXBfc3VwcG9ydGVkPTEiLCJUcmlnZ2VyUGFnZSI6InZpcHNoaXlvbmciLCJQYXlBY3Rpdml0eU5hbWUiOiLlvIDpgJrkvJrlkZjmir3lpKflpZYiLCJNZW1iZXJzaGlwQ2xhc3NpZnkiOiLlhYXlgLzkvJrlkZgiLCIkaXNfZmlyc3RfZGF5IjpmYWxzZSwiJGlzX2ZpcnN0X3RpbWUiOmZhbHNlfSwidHlwZSI6InRyYWNrIiwiZXZlbnQiOiJQYXlBY3Rpdml0eVBWIiwiX25vY2FjaGUiOiI1ODMzOTc1NTU1MTg2In0='
    data_json = ""
    with open("/Users/zhengshi/PycharmProjects/TestTools_Python/TeatData/decoding.json", "w") as file:
        data_str = note.replace("_", "/").replace("-", "+")
        data_decode = base64.standard_b64decode(data_str)
        data_json = data_decode
        json.dump(data_decode, file)
    pprint(file.read())


def main():
    translation()


if __name__ == '__main__':
    main()