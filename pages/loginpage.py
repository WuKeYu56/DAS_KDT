import time

from selenium import webdriver

from common.base import Base


def login(driver, user='gm_admin', psw='qwe123123'):
    host = '11.0.0.167'
    url = f'http://{host}:9103/login'
    print(url)
    #-------定位元素信息--------#
    loc1 = ('xpath', '//button[@class="_btn _btn_primariy ng-binding"]')
    loc2 = ('xpath', '//input[@name="username"]')
    loc3 = ('xpath', '//input[@name="password"]')
    loc4 = ('xpath', '//button[@class="btn btn_submit ng-binding"]')

    '''普通登录函数'''
    zen = Base(driver)
    driver.get(url)
    zen.click(loc1)
    zen.sendkeys(loc2, user)
    zen.sendkeys(loc3, psw)
    zen.click(loc4)
    time.sleep(5)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    login(driver)