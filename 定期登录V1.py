# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.9 (tags/v3.8.9:a743f81, Apr  6 2021, 14:02:34) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: 定期登录.py
# Size of source mod 2**32: 227 bytes
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import os, requests, datetime
while True:
    driver = webdriver.Edge()
    driver.maximize_window()
    while True:
        try:
            driver.get('http://10.255.0.19/')
            username = driver.find_elements(By.NAME, 'DDDDD')[1]
            password = driver.find_elements(By.NAME, 'upass')[1]
            username.send_keys('')  # 账号
            password.send_keys('')  # 密码
            s1 = Select(driver.find_element(By.NAME, 'ISP_select'))
            s1.select_by_index(2)   # 运营商 2-电信 3-联通 4-移动
            time.sleep(5)
            driver.find_elements(By.NAME, '0MKKey')[1].click()
            print('网络已连接！')
            print('连接时间：', datetime.datetime.now())
            command = 'taskkill /F /IM SunloginClient.exe'
            os.system(command)
            print('向日葵软件已关闭！')
            path = 'D:/向日葵/SunloginClient/SunloginClient.exe'
            os.startfile(path)
            print('向日葵软件已开启！')
            time.sleep(5)
            driver.close()
            break
        except:
            print('检查完毕，网络正常！')
            print('检查时间：', datetime.datetime.now())
            path = 'D:/向日葵/SunloginClient/SunloginClient.exe'
            os.startfile(path)
            print('向日葵软件已开启！')
            driver.close()
            break

    time.sleep(21600)
# okay decompiling 定期登录.pyc
