# -*- coding: utf-8 -*-

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import os
import requests
import datetime
import ctypes,sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def save_info(username, password, operater, path = None):
    # 将用户名、密码和路径信息存储到文本文件中
    with open('info.txt', 'w') as f:
        f.write(f"{username}\n{password}\n{operater}\n{path}")

def load_info(index):
    print('加载信息')
    if os.path.isfile('info.txt'):
        # 解码加密文件并读取内容
        with open('info.txt', 'r', encoding='utf-8') as f:
            content = f.readlines()
            # content = f.read()

        return content
    else:
        if index == '1':
            print('*************信息输入***************')
            path = input('请输入向日葵软件路径：')
            username = input('请输入用户名：')
            password = input('请输入密码：')
            operater = input('运营商：2-电信 3-联通 4-移动\n')
            save_info(username, password, operater, path)
            return [username, password, operater, path]
        else:
            print('*************信息输入***************')
            username = input('请输入用户名：')
            password = input('请输入密码：')
            operater = input('运营商：2-电信 3-联通 4-移动\n')
            save_info(username, password, operater)
            return [username, password, operater]


if is_admin():
    print("正在以管理员身份运行！")
    index = input('是否打开向日葵？ 0-close 1-open \n')
    # path = r"D:\向日葵\SunloginClient\SunloginClient.exe"  # 向日葵软件路径
    if index == '1':
        info = load_info(index)
        userkey, passwordkey, operater, path = info[0], info[1], info[2], info[3]
        # print(userkey, passwordkey, operater, path)
        time.sleep(3)
        if info[3] == 'None':
            os.remove('info.txt')
            path = input('请输入向日葵软件路径：')
            save_info(userkey, passwordkey, operater, path)

    else:
        info = load_info(index)
        if len(info) < 3:
            os.remove('info.txt')
            info = load_info(index)
        userkey, passwordkey, operater= info[0], info[1], info[2]
    while 1:
        driver=webdriver.Edge()
        driver.maximize_window()

        while 1:
            try:
                driver.get('http://10.255.0.19/')
                username = driver.find_elements(By.NAME, 'DDDDD')[1]
                #print(username)
                password = driver.find_elements(By.NAME, "upass")[1]
                username.send_keys(userkey)
                password.send_keys(passwordkey)
                s1 = Select(driver.find_element(By.NAME, "ISP_select"))
                s1.select_by_index(int(operater))
                time.sleep(5)
                driver.find_elements(By.NAME, "0MKKey")[1].click()
                print("网络已连接！")
                print("连接时间：", datetime.datetime.now())
                if index == '1':
                    while 1:
                        try:
                            command = 'taskkill /F /IM SunloginClient.exe'
                            os.system(command)
                            print("向日葵软件已关闭！")
                            break
                        except:

                            os.startfile(path)
                            print("向日葵软件已开启！")
                    os.startfile(path)
                    print("向日葵软件已开启！")
                time.sleep(5)
                driver.close()
                break
            except:
                #print("网络已连接！")
                print('检查完毕，网络正常！')
                print("检查时间：", datetime.datetime.now())
                if index == '1':
                    os.startfile(path)
                    print("向日葵软件已开启！")
                driver.close()
                break

        # else:
        #     print('检查完毕，网络正常！')
        #     print("检查时间：", datetime.datetime.now())
        #     driver.close()

        time.sleep(21600)   #暂停6小时
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    print("已切换管理员身份！")


#pyinstaller -F C:\Users\p\PycharmProjects\untitled\定期检查校园网.py
#C:\Users\p\dist
#shell:startup

