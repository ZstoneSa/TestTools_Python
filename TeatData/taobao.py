# -*- coding: utf-8 -*-
# @Time    : 2021/2/9 3:34 下午
# @Author  : Zstone
# @FileName: taobao.py
# @Software: PyCharm

import os
from selenium import webdriver
import datetime
import time
from os import path
from selenium.webdriver.common.action_chains import ActionChains

d = path.dirname(__file__)
abspath = path.abspath(d)

driver = webdriver.Chrome()
print("start webdriver")

# driver = webdriver.Firefox()
driver.maximize_window()


def login():
    # 打开淘宝登录页，并进行扫码登录
    driver.get("https://www.taobao.com")
    time.sleep(3)
    if driver.find_element_by_link_text("亲，请登录"):
        driver.find_element_by_link_text("亲，请登录").click()

    print("请在30秒内完成扫码")
    time.sleep(30)
    print("cart1")
    driver.get("https://cart.taobao.com/cart.htm")
    print("cart2")
    time.sleep(3)
    print("cart3")
    # 点击购物车里全选按钮
    # if driver.find_element_by_id("J_CheckBox_939775250537"):
    # driver.find_element_by_id("J_CheckBox_939775250537").click()
    # if driver.find_element_by_id("J_CheckBox_939558169627"):
    # driver.find_element_by_id("J_CheckBox_939558169627").click()
    print("enter into cart!")
    if driver.find_element_by_id("J_SelectAll1"):
        driver.find_element_by_id("J_SelectAll1").click()
        print('select the product')
        # print("SelectAll1!")
    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))


def buy(buytime):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        # 对比时间，时间到的话就点击结算
        if now > buytime:
            try:
                # 点击结算按钮
                if driver.find_element_by_id("J_Go"):
                    driver.find_element_by_id("J_Go").click()
                driver.find_element_by_link_text('提交订单').click()
            except:
                time.sleep(0.1)
        print(now)
        time.sleep(0.1)


if __name__ == "__main__":
    # times = input("请输入抢购时间：")
    # 时间格式："2018-09-06 11:20:00.000000"
    login()
    buy("2021-02-09 17:00:00.000000")