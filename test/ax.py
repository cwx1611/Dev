# coding=utf-8
import time
from selenium import webdriver

driver = webdriver.Firefox()  # 打开FileFox浏览器

driver.get('http://www.baidu.com')  # 打开百度界面

#driver.find_element_by_id('kw').send_keys('selenium')  # 在搜索框内输入想要搜索内容

#time.sleep(2)  # 浏览器加载需要时间

#driver.find_element_by_id('su').click()  # 搜索完成
