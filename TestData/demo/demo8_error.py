# -*- coding: utf-8 -*-
# @Time    : 2021/5/12 1:19 下午
# @Author  : Zstone
# @FileName: demo8_error.py
# @Software: PyCharm

"""

try:
    print('t1')

    f = open('t2.txt', 'r')

    print('t2')

    print(num)

except (NameError, IOError) as ErrorResult:  # 文件未找到属于IO异常，补货异常后执行的代码
    print('xxx Error')
    print(ErrorResult)

"""

import time

try:
    f = open('abtest_change1.txt', 'r')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(5)
            print(content)
    finally:
        f.close()
        print('文件已关闭')

except Exception as ErrorResult:
    print("❌发生异常：%s" % ErrorResult)




