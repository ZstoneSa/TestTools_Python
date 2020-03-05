# -*- coding: utf-8 -*-
# @Time    : 2019-12-30 14:40
# @Author  : Zstone
# @FileName: Android_test.py
# @Software: PyCharm

import os,unittest,time,sys
import self as self
from appium import webdriver
from time import sleep

desired_caps = {
      'platformName': 'Android', # 设备系统
      'deviceName': 'Meizu_M15_CN', # 设备名称
      'platformVersion': '7.1.2', # 系统版本
      'noReset': 'true',
      'unicodeKeyboard': 'true',
      'resetKeyboard': 'true',
      'appPackage': 'com.kuaikan.comic',# 包名
      'appActivity': 'com.kuaikan.main.LaunchActivity',# app启动活动
      'automationName':'UiAutomator1'#
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) # 启动app

time.sleep(5)#等待五秒

#根据id定位点击
self.driver.find_element_by_id("com.smartisanos.notes:id/new_note_button").click()

#根据id定位输入字
self.driver.find_element_by_id(“com.smartisanos.notes:id/list_rtf_view”).send_keys(“你好”)

#根据坐标定位点击
self.driver.tap([(983, 1820)])

#截图保存到当前文件夹
#driver.save_screenshot(‘login.png’)

#截图保存到指定文件夹，需在同级建一个名为images的文件夹，保存的图片名为login1
driver.get_screenshot_as_file('./images/login1.png')