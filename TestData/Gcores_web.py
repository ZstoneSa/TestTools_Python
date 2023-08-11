# -*- coding: utf-8 -*-
# @Time    : 2023/8/4 15:30
# @Author  : Zstone
# @FileName: Gcores_web.py
# @Software: PyCharm

import datetime
import json

import pytest
import logging
import WebAuto.data
from retrying import retry
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from airtest.core.api import *


def open_home_page():
    print("检查「主页」中...")
    driver.get('https://www.gcores.com/')
    # 断言网址是否正确
    try:
        assert 'https://www.gcores.com/' in driver.current_url
        # 页面唯一标志（用于定位页面）
        home_unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = home_unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "home", "当前页面为：首页")
        print("√ 机核主页正常加载")
    except AssertionError:
        pytest.fail("未定位到首页，请检查首页状态")
        # log("× 机核主页状态异常")


# 基本操作
@retry(wait_fixed=10, stop_max_attempt_number=1)
def login():
    print("密码登录操作中...")
    loginhome_btn = driver.find_element(By.XPATH, '//*[@id="app_inner"]/div[3]/div/div[2]/nav/div/div[2]/div[3]/button/span')
    # 断言是否存在登录按钮
    assert loginhome_btn.text in driver.page_source
    loginhome_btn.click()
    # 断言登录弹窗是否展示
    assert '免密登录' in driver.page_source
    passwd_login = driver.find_element(By.XPATH, '/html/body/div[13]/div/div/div[2]/div[1]/ul/li[2]/a/span')
    passwd_login.click()
    print("密码登录")
    phonenum_input = driver.find_element(By.XPATH, '/html/body/div[13]/div/div/div[2]/form/div[1]/div/input')
    phonenum_input.click()
    print("正在输入账号密码")
    account = json.loads(open())
    phonenum_input.send_keys("13520363642")
    passnum_input = driver.find_element(By.XPATH, '/html/body/div[13]/div/div/div[2]/form/div[2]/div/input')
    passnum_input.click()
    passnum_input.send_keys("Zs111111")
    keeplogin_btn = driver.find_element(By.XPATH, '//*[@id="rememberMe"]')
    keeplogin_btn.click()
    login_btn = driver.find_element(By.XPATH, '/html/body/div[13]/div/div/div[2]/form/div[4]/button')
    login_btn.click()
    sleep(5)

    try:
        # 断言登录成功，在首页展示收藏
        collections_btn = driver.find_element(By.XPATH, '//*[@id="app_inner"]/div[3]/div/div[2]/nav/div/div[2]/div[3]/a[2]')
        assert_equal(collections_btn.text, "收藏", "登录成功，定位首页收藏")
        print("登录成功后，首页显示：{}".format(collections_btn.text))
    except AssertionError:
        pytest.fail("未定位到首页「收藏」btn，请检查页面状态")
        # log("未定位到「收藏」btn，请检查登录状态")


def signout():
    try:
        # 鼠标移动到顶部右上角头像，是否展示退出按钮
        avatar = driver.find_element(By.CLASS_NAME, 'avatar_img')
        ActionChains(driver).move_to_element(avatar)
        signout_btn = driver.find_element(By.LINK_TEXT, '退出')
        assert signout_btn.text in driver.page_source
        signout_btn.click()
        # 退出成功断言
        loginhome_btn = driver.find_element(By.XPATH, '//*[@id="app_inner"]/div[3]/div/div[2]/nav/div/div[2]/div[3]/button/span')
        # 断言是否存在登录按钮
        assert loginhome_btn.text in driver.page_source
        print("退出登录成功")

    except AssertionError:
        pytest.fail("× 退出登录异常")


def open_topic_home():
    print("检查「机组首页」中...")
    driver.get('https://www.gcores.com/topics/home')
    # 断言网址是否正确
    try:
        assert 'https://www.gcores.com/topics/home' in driver.current_url
        # 页面唯一标志（用于定位页面）
        home_unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = home_unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "topicsHome", "当前页面为：机组首页")
        print(" 机组首页正常加载")
    except AssertionError:
        pytest.fail("未定位到首页，请检查首页状态")
        # log("× 机核主页状态异常")


def news_page():
    pass


def radio_page():
    pass


def article_page():
    pass


def video_page():
    pass


def audiobooks_page():
    pass


def store_link():
    pass


def work_page():
    pass


def game_origin_page():
    pass


def albums_page():
    pass


def collection_page():
    pass


def app_download_page():
    pass


def article_detail_page():
    print("检查文章详情页（用户发布）中...")
    driver.get('https://www.gcores.com/articles/169291')
    sleep(5.0)
    # 断言展示
    try:
        # 断言网址是否正确
        assert 'https://www.gcores.com/articles/169291' in driver.current_url
        # 页面唯一标志（用于定位页面）
        home_unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = home_unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "article", "当前页面属于：文章页")
        print("√ 当前页面属于「文章页（一级页）」")
        article_unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]/div[3]/div/div[3]/div[1]/div/div/div[1]/div[4]')
        assert_equal(article_unique_mark.text, "本文系用户投稿，不代表机核网观点", "当前位于文章页")
        print("√ 文章详情页正常加载")
    except AssertionError:
        pytest.fail("文章详情页状态异常")
        # log("× 文章详情页状态异常")


def talk_detail_page():
    print("检查话题详情页中...")
    driver.get('https://www.gcores.com/talks/633413')
    # 断言展示
    try:
        # 断言网址是否正确
        assert 'https://www.gcores.com/talks/633413' in driver.current_url
        talk_unique_maek = driver.find_element(By.XPATH, '//*[@id="app_inner"]/div[3]/div/div[3]/div/div[1]/div/div[2]/div[1]/div[4]/a/span')
        assert_equal(talk_unique_maek.text, "🧩一枚生活碎片", "")
        print("√ 话题详情页正常加载")
    except AssertionError:
        pytest.fail("话题详情页状态异常")
        # log("× 话题详情页状态异常")


def radio_detail_page():
    print("检查电台详情页中...")
    driver.get('https://www.gcores.com/radios/169168')
    # 断言展示
    try:
        # 断言当URL是否正确
        assert 'https://www.gcores.com/radios/169168' in driver.current_url
        # 页面唯一标志
        radio_unique_mark = driver.find_element(By.CLASS_NAME, 'radioPage_radio')
        assert radio_unique_mark.text in driver.page_source
        print("√ 电台详情页正常加载")
    except AssertionError:
        pytest.fail("电台详情页状态异常")
        # log("× 电台详情页状态异常")


def video_detail_page():
    try:
        video_unique_mark = driver.find_element(By.CLASS_NAME, 'videoPlayer_container')
        assert video_unique_mark.text in driver.page_source

    except NoSuchElementException:
        pytest.fail()


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
    # 启动chrome超出25S 抛出异常
    driver.implicitly_wait(25)
    # 计算启动时间
    start_time = datetime.datetime.now()
    # 打开主站 - 未登录
    open_home_page()
    driver.maximize_window()
    end_time = datetime.datetime.now()
    print(end_time - start_time)
    '''测试用例'''
    login()
    radio_detail_page()
    article_detail_page()
    talk_detail_page()

    # 退出chrome
    driver.quit()

finally:
    log("测试结束，请查看控制台结果")
