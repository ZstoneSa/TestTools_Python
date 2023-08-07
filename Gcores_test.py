# -*- coding: utf-8 -*-
# @Time    : 2023/8/7 16:14
# @Author  : Zstone
# @FileName: Gcores_test.py
# @Software: PyCharm
import datetime
from retrying import retry
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from airtest.core.api import *
# from selenium.webdriver.common.keys import Keys
# from pyvirtualdisplay import Display
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# 基本操作
@retry(wait_fixed=10, stop_max_attempt_number=1)
def login():
    print("密码登录操作中...")
    loginhome_btn = driver.find_element(By.XPATH, '//*[@id="app_inner"]/div[3]/div/div[2]/nav/div/div[2]/div[3]/button')
    loginhome_btn.click()
    # 断言登录弹窗是否展示
    assert '免密登录' in driver.page_source
    passwd_login = driver.find_element(By.XPATH, '/html/body/div[13]/div/div/div[2]/div[1]/ul/li[2]/a/span')
    passwd_login.click()
    print("密码登录")
    phonenum_input = driver.find_element(By.XPATH, '/html/body/div[13]/div/div/div[2]/form/div[1]/div/input')
    phonenum_input.click()
    print("正在输入账号密码")
    phonenum_input.send_keys("13520363642")
    passnum_input = driver.find_element(By.XPATH, '/html/body/div[13]/div/div/div[2]/form/div[2]/div/input')
    passnum_input.click()
    passnum_input.send_keys("Zs111111")
    keeplogin_btn = driver.find_element(By.XPATH, '//*[@id="rememberMe"]')
    keeplogin_btn.click()
    login_btn = driver.find_element(By.XPATH, '/html/body/div[13]/div/div/div[2]/form/div[4]/button')
    login_btn.click()
    assert '500'

    try:
        # 断言登录成功，在首页展示收藏
        collections_btn = driver.find_element(By.XPATH, '//*[@id="app_inner"]/div[3]/div/div[2]/nav/div/div[2]/div[3]/a[2]')
        assert_equal(collections_btn.text, "收藏", "登录成功，定位首页收藏")
        print("登录成功后，首页显示：{}".format(collections_btn.text))
    except NoSuchElementException:
        log("未定位到「收藏」btn，请检查登录状态")


'''
normal：等待整个页面加载完毕再开始执行操作
eager：等待整个dom树加载完成，即DOMContentLoaded这个事件完成，也就是只要 HTML 完全加载和解析完毕就开始执行操作。放弃等待图片、样式、子帧的加载。
none：等待html下载完成，哪怕还没开始解析就开始执行操作。
'''
try:
    chrome_options = Options()
    chrome_options.page_load_strategy = 'normal'
    # 启动chrome
    driver = webdriver.Chrome(options=chrome_options)
    # 命令超出时长异常抛出
    driver.implicitly_wait(20)
    # 计算启动时间
    start_time = datetime.datetime.now()
    driver.get('https://www.gcores.com/')
    # 断言网址是否正确
    assert 'https://www.gcores.com/' in driver.current_url
    driver.maximize_window()

    '''测试用例'''
    login()
    end_time = datetime.datetime.now()
    print(end_time - start_time)
    # 退出chrome
    driver.quit()

finally:
    log("测试结束，请查看终端消息")