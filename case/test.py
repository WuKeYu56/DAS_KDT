import time

from selenium import webdriver

from common.base import Base
from pages.loginpage import login

d = webdriver.Chrome()
login(d)
das = Base(d)
das.open("http://11.0.0.167:9103/v2/site/record.html?siteId=100024")
print(d.title)
das.click(('xpath', '//button[@ng-click="addProject()"]'))
das.switch_iframe("projectForm")
# das.click(('xpath', '//*[@id="projectForm"]/div[1]/div/input'))
das.sendkeys(('xpath', '//*[@id="projectForm"]/div[1]/div/input'), 'test_project')
#选择类型
das.click(('xpath', '//*[@id="projectForm"]/div[2]/div/div'))
das.click(('xpath', '//*[@id="projectForm"]/div[2]/div/div/dl/dd[3]'))
#选择任务
das.click(('xpath', '//*[@id="projectForm"]/div[4]/div/div/div'))
das.click(('xpath', '//*[@id="projectForm"]/div[4]/div/div/dl/dd[3]'))
#选择坐标
das.click(('xpath', '//*[@id="projectForm"]/div[5]/div/div/div'))
das.click(('xpath', '//*[@id="projectForm"]/div[5]/div/div/dl/dd[2]'))
#选择走向
das.click(('xpath', '//*[@id="projectForm"]/div[6]/div/div/div'))
das.click(('xpath', '//*[@id="projectForm"]/div[6]/div/div/dl/dd[2]'))
#选择区域
das.click(('xpath', '//*[@id="projectForm"]/div[7]/div/div/div'))
das.click(('xpath', '//*[@id="projectForm"]/div[7]/div/div/dl/dd'))
#点击添加
das.
das.click(('xpath', '//*[@id="layui-layer8"]/div[3]/a[1]'))


time.sleep(5)
d.close()