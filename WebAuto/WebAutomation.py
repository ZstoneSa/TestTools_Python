# -*- coding: utf-8 -*-
# @Time    : 2023/8/4 15:30
# @Author  : Zstone
# @FileName: Gcores_web.py
# @Software: PyCharm

import datetime
import pytest
from retrying import retry
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from airtest.core.api import *

global base_url


def open_home_page():
    print("检查「主页」中...")
    driver.get(base_url)
    driver.maximize_window()
    # 断言网址是否正确
    try:
        assert base_url in driver.current_url
        # 页面唯一标志（用于定位页面）
        unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "home", "当前页面为：首页")
        print("√ 机核主页正常加载")
    except AssertionError:
        pytest.fail("定位「机核首页」失败，请检查首页状态")
        # log("× 机核主页状态异常")
    sleep(3)


def open_topic_home():
    print("检查「机组首页」中...")
    url = base_url + 'topics/home'
    driver.get(url)
    # 断言网址是否正确
    try:
        assert url in driver.current_url
        # 页面唯一标志（用于定位页面）
        unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "topicsHome", "当前页面为：机组首页")
        print("机组首页正常加载")
    except AssertionError:
        pytest.fail("定位「机组首页」失败，请检查首页状态")
        # log("× 机核主页状态异常")
    sleep(3)


def open_news_page():
    print("检查「资讯页」中...")
    url = base_url + 'news'
    driver.get(url)
    # 断言网址是否正确
    try:
        assert url in driver.current_url
        # 页面唯一标志（用于定位页面）
        unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "newsList", "当前页面为：咨询页")
        print("咨询页正常加载")
    except AssertionError:
        pytest.fail("定位「资讯页」失败，请检查首页状态")
        # log("× 机核主页状态异常")
    sleep(3)


def open_radios_page():
    print("检查「播客页」中...")
    url = base_url + 'radios'
    driver.get(url)
    # 断言网址是否正确
    try:
        assert url in driver.current_url
        # 页面唯一标志（用于定位页面）
        unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "radios", "当前页面为：播客页")
        print("播客页正常加载")
    except AssertionError:
        pytest.fail("定位「播客页」失败，请检查首页状态")
        # log("× 机核主页状态异常")
    sleep(3)


def open_articles_page():
    print("检查「文章页」中...")
    url = base_url + 'articles'
    driver.get(url)
    # 断言网址是否正确
    try:
        assert url in driver.current_url
        # 页面唯一标志（用于定位页面）
        unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "articles", "当前页面属于：文章页")
        print("播客页正常加载")
    except AssertionError:
        pytest.fail("定位「播客页」失败，请检查首页状态")
        # log("× 机核主页状态异常")
    sleep(3)


def open_videos_page():
    print("检查「视频页」中...")
    url = base_url + 'videos'
    driver.get(url)
    # 断言网址是否正确
    try:
        assert url in driver.current_url
        # 页面唯一标志（用于定位页面）
        unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "videos", "当前页面为：视频页")
        print("视频页正常加载")
    except AssertionError:
        pytest.fail("定位「视频页」失败，请检查页面状态")
        # log("× 机核主页状态异常")
    sleep(3)


def open_audiobooks_page():
    print("检查「有声书页」中...")
    url = base_url + 'audio_books'
    driver.get(url)
    # 断言网址是否正确
    try:
        assert url in driver.current_url
        # 页面唯一标志（用于定位页面）
        unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "audioBooks", "当前页面为：有声书页")
        print("有声书页正常加载")
    except AssertionError:
        pytest.fail("定位「有声书页」失败，请检查首页状态")
        # log("× 机核主页状态异常")
    sleep(3)


def check_store_link():
    print("检查链接跳转是否正常")
    store_icon = driver.find_element(By.XPATH, '//*[@id="app_inner"]/div[3]/section/div[1]/div/div[9]/button/span/span[2]')
    assert store_icon.text == '商店'
    ActionChains(driver).move_to_element(store_icon)
    hidden_store_link_g = driver.find_element(By.XPATH, '/html/body/div[10]/div/div/ul/li/a/span/span')
    hidden_store_link_h = driver.find_element(By.XPATH, '/html/body/div[10]/div/div/ul/li[1]/a/span/span')
    assert hidden_store_link_g.text == "吉考斯工业"
    assert hidden_store_link_h.text == "核市奇谭"
    # 点击跳转"吉考斯工业"
    ActionChains(driver).click(hidden_store_link_g)

    assert "吉考斯工业", "核市奇谭" in driver.page_source
    sleep(3)


def open_works_page():
    print("检查「原创作品页」中...")
    url = base_url + 'works'
    driver.get(url)
    # 断言网址是否正确
    try:
        assert url in driver.current_url
        # 页面唯一标志（用于定位页面）
        unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "works", "当前页面为：原创作品页")
        print("原创作品页正常加载")
    except AssertionError:
        pytest.fail("定位「原创作品页」失败，请检查首页状态")
        # log("× 机核主页状态异常")
    sleep(3)


def open_games_original_page():
    print("检查「原创游戏页」中...")
    url = base_url + 'games/original'
    driver.get(url)
    try:
        # 断言网址是否正确
        assert url in driver.current_url
        # 页面唯一标志（用于定位页面）
        unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "gamesOriginal", "当前页面为：原创游戏页")
        print("原创游戏页正常加载")
    except AssertionError:
        pytest.fail("定位「原创游戏页」失败，请检查首页状态")
        # log("× 机核主页状态异常")
    sleep(3)


def open_albums_page():
    print("检查「播单页」中...")
    url = base_url + 'albums'
    driver.get(url)
    # 断言网址是否正确
    try:
        assert url in driver.current_url
        # 页面唯一标志（用于定位页面）
        unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "albums", "当前页面为：播单页")
        print("播单页正常加载")
    except AssertionError:
        pytest.fail("定位「播单页」失败，请检查首页状态")
        # log("× 机核主页状态异常")
    sleep(3)


def open_collections_page():
    print("检查「专题页」中...")
    url = base_url + 'collections'
    driver.get(url)
    # 断言网址是否正确
    try:
        assert url in driver.current_url
        # 页面唯一标志（用于定位页面）
        unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "collections", "当前页面为：专题页")
        print("专题页正常加载")
    except AssertionError:
        pytest.fail("定位「专题页」失败，请检查首页状态")
        # log("× 机核主页状态异常")
    sleep(3)


def open_app_download_page():
    print("检查「app下载页」中...")
    url = base_url + 'app'
    driver.get(url)
    # 断言网址是否正确
    try:
        assert url in driver.current_url
        # 页面唯一标志（用于定位页面）
        unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "app", "当前页面为：app下载页")
        print("app下载页正常加载")
    except AssertionError:
        pytest.fail("定位「app下载页」失败，请检查首页状态")
        # log("× 机核主页状态异常")
    sleep(3)


def open_gpass_buy_page():
    print("检查「会员购买页」中...")
    url = base_url + 'gpass'
    driver.get(url)
    # 断言网址是否正确
    try:
        assert url in driver.current_url
        # 页面唯一标志（用于定位页面）
        unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "gpass", "当前页面为：会员购买页")
        print("会员购买页正常加载")
    except AssertionError:
        pytest.fail("定位「会员购买页」失败，请检查首页状态")
        # log("× 机核主页状态异常")
    sleep(3)


def open_gpass_privilege():
    print("检查「会员权益页」中...")
    url = base_url + 'gpass_privilege'
    driver.get(url)
    # 断言网址是否正确
    try:
        assert url in driver.current_url
        # 页面唯一标志（用于定位页面）
        unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "gpassPanel", "当前页面为：会员权益页")
        print("会员权益页正常加载")
    except AssertionError:
        pytest.fail("定位「会员权益页」失败，请检查首页状态")
        # log("× 机核主页状态异常")
    sleep(3)


def open_gpass_orders_page():
    print("检查「会员订单页」中...")
    url = base_url + 'gpass_privilege/orders'
    driver.get(url)
    # 断言网址是否正确
    try:
        assert url in driver.current_url
        # 页面唯一标志（用于定位页面）
        unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "gpassOrders", "当前页面为：会员订单页")
        print("会员订单页正常加载")
    except AssertionError:
        pytest.fail("定位「会员订单页」失败，请检查首页状态")
        # log("× 机核主页状态异常")
    sleep(3)


def open_mails_page():
    print("检查「私信页」中...")
    url = base_url + 'mails?opponentID=0'
    driver.get(url)
    # 断言网址是否正确
    try:
        assert url in driver.current_url
        # 页面唯一标志（用于定位页面）
        unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "mails", "当前页面为：会员订单页")
        print("私信页正常加载")
    except AssertionError:
        pytest.fail("定位「私信页」失败，请检查首页状态")
        # log("× 机核主页状态异常")
    sleep(3)


def open_user_page(user_id):
    print("检查「个人页」中...")
    url = base_url + 'users/' + str(user_id) + '/'
    driver.get(url)
    # 断言网址是否正确
    try:
        assert driver.current_url == url + 'talks'
        # 页面唯一标志（用于定位页面）
        unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "userTalks", "当前页面为：个人页")
        print("个人页正常加载")
    except AssertionError:
        pytest.fail("定位「个人页」失败，请检查首页状态")
        # log("× 机核主页状态异常")
    sleep(3)


def open_setting_page():
    print("检查「设置页」中...")
    url = base_url + 'settings'
    driver.get(url)
    # 断言网址是否正确
    try:
        assert url in driver.current_url
        # 页面唯一标志（用于定位页面）
        unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "settings", "当前页面为：个人页")
        print("设置页正常加载")
    except AssertionError:
        pytest.fail("定位「设置页」失败，请检查页面状态")
        # log("× 机核主页状态异常")
    sleep(3)


def open_writing_management():
    print("检查「投稿管理 - 草稿」中...")
    url = base_url + 'writing/drafts'
    driver.get(url)
    # 断言网址是否正确
    try:
        assert url in driver.current_url
        # 页面唯一标志（用于定位页面）
        unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "writingDrafts", "当前页面为：投稿管理 - 草稿")
        print("投稿管理 - 草稿正常加载")
    except AssertionError:
        pytest.fail("定位「投稿管理 - 草稿」失败，请检查页面状态")
    sleep(3)

    print("检查「投稿管理 - 发布状态」中...")
    url = base_url + 'writing/published'
    driver.get(url)
    # 断言网址是否正确
    try:
        assert url in driver.current_url
        # 页面唯一标志（用于定位页面）
        unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "writingPublished", "当前页面为：投稿管理 - 发布状态")
        print("投稿管理 - 发布状态正常加载")
    except AssertionError:
        pytest.fail("定位「投稿管理 - 发布状态」失败，请检查页面状态")
    sleep(3)

    print("检查「投稿管理 - 动态管理」中...")
    url = base_url + 'writing/talks'
    driver.get(url)
    # 断言网址是否正确
    try:
        assert url in driver.current_url
        # 页面唯一标志（用于定位页面）
        unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "writingTalks", "当前页面为：投稿管理 - 动态管理")
        print("投稿管理 - 动态管理正常加载")
    except AssertionError:
        pytest.fail("定位「投稿管理 - 动态管理」失败，请检查页面状态")
    sleep(3)


def open_original_editor():
    print("检查「编辑器页」中...")
    url = base_url + 'original_editor?type=articles'
    driver.get(url)

    try:
        # 断言网址是否正确
        assert url in driver.current_url
        # 页面唯一标志（用于定位页面）
        unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "originalEditor", "当前页面为：投稿编辑器")
        print("投稿编辑器正常加载")
    except AssertionError:
        pytest.fail("定位「投稿编辑器」失败，请检查页面状态")
        # log("× 机核主页状态异常")
    sleep(3)


def open_topic_editor():
    print("检查「动态编辑器」中...")
    url = base_url + 'topics/editor'
    driver.get(url)

    try:
        # 断言网址是否正确
        assert url in driver.current_url
        # 页面唯一标志（用于定位页面）
        unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "topicEditor", "当前页面为：投稿编辑器")
        print("动态编辑器正常加载")
    except AssertionError:
        pytest.fail("定位「动态编辑器」失败，请检查页面状态")
        # log("× 机核主页状态异常")
    sleep(3)


def open_games_detail_page(game_id):
    print("检查「游戏详情页」中...")
    url = base_url + 'games/' + str(game_id)
    driver.get(url)
    # 断言网址是否正确
    try:
        assert url in driver.current_url
        # 页面唯一标志（用于定位页面）
        unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "term", "当前页面为：游戏详情页")
        print("游戏详情页正常加载")
    except AssertionError:
        pytest.fail("定位「游戏详情页」失败，请检查首页状态")
        # log("× 机核主页状态异常")
    sleep(5)


def open_article_detail_page():
    print("检查文章详情页（用户发布）中...")
    url = base_url + 'articles/169291'
    driver.get(url)
    # 断言展示
    try:
        # 断言网址是否正确
        assert url in driver.current_url
        # 页面唯一标志（用于定位页面）
        unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "article", "当前页面属于：文章页(含资讯)")
        print("√ 文章详情页（含资讯）正常加载")
    except AssertionError:
        pytest.fail("文章详情页状态异常")
        # log("× 文章详情页状态异常")
    sleep(5)


def open_talk_detail_page():
    print("检查机组动态详情页中...")
    url = base_url + 'talks/633413'
    driver.get(url)
    # 断言展示
    try:
        # 断言网址是否正确
        assert url in driver.current_url
        unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "talk", "当前页面属于：机组动态详情页")
        print("√ 机组动态详情页正常加载")
    except AssertionError:
        pytest.fail("机组动态详情页状态异常")
        # log("× 话题详情页状态异常")
    sleep(5)


def open_radio_detail_page():
    print("检查播客详情页中...")
    url = base_url + 'radios/169168'
    driver.get(url)
    # 断言展示
    try:
        # 断言当URL是否正确
        assert url in driver.current_url
        # 页面唯一标志
        unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "radio", "当前页面属于：播客详情页")
        print("√ 播客详情页正常加载")
    except AssertionError:
        pytest.fail("播客详情页状态异常")
        # log("× 电台详情页状态异常")
    sleep(5)


def open_timeline_page(radio_id):
    print("检查「时间轴页」中...")
    url = base_url + 'radios/' + str(radio_id) + '/timelines'
    driver.get(url)
    # 断言展示
    try:
        # 断言当URL是否正确
        assert url in driver.current_url
        # 页面唯一标志
        unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "timelines", "当前页面属于：时间轴页")
        print("√ 时间轴页正常加载")
    except AssertionError:
        pytest.fail("「时间轴页」状态异常")
        # log("× 电台详情页状态异常")
    sleep(5)


def open_video_detail_page():
    print("检查视频详情页(taptap源)中...")
    url = base_url + 'videos/169095'
    driver.get(url)

    try:
        assert url in driver.current_url
        unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "video", "当前页面属于：视频详情页(taptap源)")
        print("√ 视频详情页(taptap源)正常加载")

    except AssertionError:
        pytest.fail("视频详情页中(taptap源)异常")
    sleep(5)

    print("检查视频详情页(官方)中...")
    url = base_url + 'videos/169539'
    driver.get(url)

    try:
        assert url in driver.current_url
        unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "video", "当前页面属于：视频详情页(官方)")
        print("√ 视频详情页(官方)正常加载")

    except AssertionError:
        pytest.fail('视频详情页(官方)异常')
    sleep(5)


def open_albums_detail_page():
    print("检查「播单详情页」中...")
    url = base_url + 'albums/199'
    driver.get(url)
    # 断言展示
    try:
        # 断言当URL是否正确
        assert url in driver.current_url
        # 页面唯一标志
        unique_mark = driver.find_element(By.XPATH, '//*[@id="app_inner"]')
        page_pos = unique_mark.get_attribute('data-page-name')
        assert_equal(page_pos, "album", "当前页面属于：播单详情页")
        print("√ 播单详情页正常加载")
    except AssertionError:
        pytest.fail("播单详情页状态异常")
        # log("× 电台详情页状态异常")
    sleep(5)


@retry(wait_fixed=10, stop_max_attempt_number=1)
def login():
    open_home_page()
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
    # data_json = json.loads(open('/WebAuto/data/data.json', 'r').read())
    # account = json.loads(data_json['accounts'][0])
    # phonenum_input.send_keys(account)
    phonenum_input.send_keys("13520363642")
    passnum_input = driver.find_element(By.XPATH, '/html/body/div[13]/div/div/div[2]/form/div[2]/div/input')
    passnum_input.click()
    # data_json = json.loads(open('/WebAuto/data/data.json', 'r').read())
    # password = json.loads(data_json['passwords'][0])
    # passnum_input.send_keys(password)
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
        pytest.fail("定位：首页「收藏」btn失败，请检查页面状态")
        # log("未定位到「收藏」btn，请检查登录状态")


def signout():
    try:
        open_home_page()
        # 鼠标移动到顶部右上角头像，是否展示退出按钮
        avatar = driver.find_element(By.CLASS_NAME, 'avatar_img')
        ActionChains(driver).move_to_element(avatar).perform()
        ActionChains(driver).click()
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
    sleep(3)


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
    base_url = "http://local.gcores.com:3001/"
    # base_url = "https://www.gcores.com/"
    # 计算启动时间s
    start_time = datetime.datetime.now()
    '''【未登录】打开各页面'''
    open_home_page()
    open_topic_home()
    open_news_page()
    open_radios_page()
    open_articles_page()
    open_videos_page()
    open_audiobooks_page()
    open_works_page()
    open_games_original_page()
    open_albums_page()
    open_collections_page()
    open_app_download_page()
    open_gpass_buy_page()
    open_games_detail_page(game_id=80235)
    open_article_detail_page()
    open_talk_detail_page()
    open_radio_detail_page()
    open_timeline_page(radio_id=94757)
    open_video_detail_page()
    open_albums_detail_page()

    '''【已登录】打开各页面'''
    login()
    open_home_page()
    open_topic_home()
    open_news_page()
    open_radios_page()
    open_articles_page()
    open_videos_page()
    open_audiobooks_page()
    open_works_page()
    open_games_original_page()
    open_albums_page()
    open_collections_page()
    open_app_download_page()
    open_gpass_buy_page()
    open_games_detail_page(game_id=80235)
    open_article_detail_page()
    open_talk_detail_page()
    open_radio_detail_page()
    open_timeline_page(radio_id=94757)
    open_video_detail_page()
    open_albums_detail_page()

    open_gpass_privilege()
    open_gpass_orders_page()
    open_mails_page()
    open_user_page(user_id=582398)
    open_setting_page()
    open_writing_management()
    open_original_editor()
    open_topic_editor()

    end_time = datetime.datetime.now()
    print("总花费时间：{}".format(str(end_time - start_time)))
    # 退出chrome
    driver.quit()

finally:
    log("测试结束，请查看控制台结果")
