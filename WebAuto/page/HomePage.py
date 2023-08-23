# -*- coding: utf-8 -*-
# @Time    : 2023/8/23 13:07
# @Author  : Zstone
# @FileName: HomePage.py
# @Software: PyCharm

import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver


class HomePage:
    url = "https://www.gocres.com"
    search_ipt_btn = ('class', 'gnav_item.o_plainButton')
    feeds_icon = ('href', '/feeds')
    gpass_btn = ('class', 'fa_gpassButton_bg')
    contrib_btn = ('class', 'p_svgNavBtn.gnav_item.o_plainButton')
    personal_icon = ('class', 'gnav_item.o_plainButton')
    coll_icon = ('class', 'gnav_item')
    msg_icon = ('class', 'gnav_item.o_plainButton')

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        print("打开机核首页")
        self.driver.get(self.url)


    def click_search_ipt_btn(self):
        print("点击首页搜索框")
        self.driver.find_element()


    def input_search_keyword(self, keyword):
