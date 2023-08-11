# -*- coding: utf-8 -*-
# @Time    : 2019-09-05 17:14
# @Author  : Zstone
# @FileName: try_multiprocessing.py
# @Software: PyCharm

from multiprocessing import process

import multiprocessing
import os

'''
尝试多线程同时运行不同脚本，若要尝试自动化运行Android和iOS操作系统下的不同测试机脚本 该方法大致是可以实现的
'''

def worker(file):
    os.system("python3 " + str(file))
    # 用python3来运行方法


if __name__ == '__main__':  # 最外层为input类型方法可以嵌套内层方法return使用
    files = ["../URL_base64.py", "../award_json.py"]
    for i in files:
        p = multiprocessing.Process(target=worker, args=(i,))
        p.start()
