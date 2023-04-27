import time

from selenium import webdriver

from common.base import Base
from pages.loginpage import login

d = webdriver.Chrome()
login(d)
das = Base(d)

das.open("http://11.0.0.167:9103/v2/visual/mercator.html?siteId=100024")
# das.click(("xpath", "//div[@class=\"layui-unselect layui-form-select\"]"))
# das.click(("xpath", '//dd[@lay-value="6"]'))
# das.click(('xpath', '//span[@class="open"]'))
# das.click(('xpath', '//tr[@data-index="0"]'))

# das.open("http://11.0.0.167:9103/v2/dataprocessed/radarAnalysis.html?siteId=100024&projId=100030")
# das.click(('xpath', '//*[@id="capture"]/div[1]/div[2]/div[2]/button[2]'))
# time.sleep(2)
# das.mapping_inn_disease((4, ''))
# das.sendkeys(('xpath', '//input[@name="radius"]'), '0.1')
# time.sleep(2)
# das.click(('xpath', '/html/body/div[1]/div[3]/div/section/div[8]/div[3]/a[1]'))

# das.click(('xpath', '//button[@ng-click="drawRegion(\'disease\')"]'))
# das.mapping_inn_disease((4, 'polyline'))
# das.sendkeys(("xpath", '//input[@name="name"]'), "测试内部线性病害")
# das.click(('xpath', '/html/body/div[1]/div[3]/div/section/div[7]/div[3]/a[1]'))
# das.click(('xpath', '/html/body/div[1]/div[3]/div/section/div[2]/div[2]/span[2]'))
# time.sleep(2)
# das.click(('xpath', '//*[@id="_theme_blue"]/div[1]/div[3]/div/section/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[2]/div/a'))

# das.click(('xpath', '//*[@id="_theme_blue"]/div/div[3]/div/section/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[13]/div/div/button[2]'))
# time.sleep(2)
# das.click(('xpath', '/html/body/div[3]/div[3]/a[1]'))
#
# time.sleep(2)
# das.click(('xpath', '//*[@id="_theme_blue"]/div/div[3]/div/section/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[13]/div/div/button[2]'))
# time.sleep(2)
# das.click(('xpath', '/html/body/div[4]/div[3]/a[1]'))

time.sleep(5)
d.close()