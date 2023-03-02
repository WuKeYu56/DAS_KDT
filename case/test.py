import time

from selenium import webdriver

from common.base import Base
from pages.loginpage import login

d = webdriver.Chrome()
login(d)
das = Base(d)
das.open("http://11.0.0.167:9103/v2/dataprocessed/mercatorImageAnalysis.html?siteId=100024&projId=100028")

# print(das.click(('xpath', '//*[@id="mapid"]/div[2]/div[1]/div/div[1]/div/a[1]'))) #绘制线性病害
# print(das.click(("xpath", '//*[@id="mapid"]/div[2]/div[1]/div/div[1]/div/a[2]'))) #绘制多边形
das.mapping_disease((4, 'polyline'))
das.sendkeys(('xpath', '//input[@name="name"]'), "测试病害")
time.sleep(2)
das.click(('xpath', '/html/body/div[1]/div[3]/div/section/div[3]/div[3]/a[1]'))

d.refresh()
das.click(('xpath', '//*[@id="_theme_blue"]/div[1]/div[3]/div/section/div[2]/div[2]/span[2]'))
time.sleep(1)
print(das.click(('xpath', '//*[@id="_theme_blue"]/div[1]/div[3]/div/section/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[2]/div/a')))


# def mapping_disease(num, type='polygon'):
#
#     """通过鼠标操作绘制病害"""
#     ui.FAILSAFE = True
#     #基于屏幕分辨率获取中心点
#     m, n = ui.size()
#     x1, y1 = m/2, n/2
#     ui.click(x1, y1, button='left')
#     ui.scroll(400)
#
#     #绘制不同类型病害
#     if type == 'polyline':
#
#         for i in range(num):
#             x2 = x1+random.randint(0, 200)  #可改变数字调节点击位置
#             y2 = y1+random.randint(0, 200)
#             ui.click(x2, y2, button='left')
#             time.sleep(1)
#         ui.click(x2, y2, button='left')
#
#     elif type == "polygon":
#         for i in range(num):
#             x2 = x1+random.randint(0, 200)  #可改变数字调节点击位置
#             y2 = y1+random.randint(0, 200)
#             ui.click(x2, y2, button='left')
#             time.sleep(1)
#         ui.click(x1, y1, button='left')
#
#     else:
#         print('请输入正确的参数：type=polyline/polygn')
#     return True

# mapping_disease(3, type='polyline')
print(d.title)

# das.move_to_element(('xpath', '//*[@id="_theme_blue"]/div[1]/div[3]/div/section/div[1]/div[1]/div[1]/div[2]/div/ul/li[2]'))
# time.sleep(2)
# das.click(('xpath', '//*[@id="_theme_blue"]/div[1]/div[3]/div/section/div[1]/div[1]/div[1]/div[2]/div/ul/li[2]/i[2]'))
# time.sleep(2)
# das.click(('xpath', '/html/body/div[4]/div[3]/a[1]'))
# das.click(('xpath', '//button[@ng-click="addProject()"]'))
# das.switch_iframe("projectForm")
# # das.click(('xpath', '//*[@id="projectForm"]/div[1]/div/input'))
# das.sendkeys(('xpath', '//*[@id="projectForm"]/div[1]/div/input'), 'test_project')
# #选择类型
# das.click(('xpath', '//*[@id="projectForm"]/div[2]/div/div'))
# das.click(('xpath', '//*[@id="projectForm"]/div[2]/div/div/dl/dd[3]'))
# #选择任务
# das.click(('xpath', '//*[@id="projectForm"]/div[4]/div/div/div'))
# das.click(('xpath', '//*[@id="projectForm"]/div[4]/div/div/dl/dd[3]'))
# #选择坐标
# das.click(('xpath', '//*[@id="projectForm"]/div[5]/div/div/div'))
# das.click(('xpath', '//*[@id="projectForm"]/div[5]/div/div/dl/dd[2]'))
# #选择走向
# das.click(('xpath', '//*[@id="projectForm"]/div[6]/div/div/div'))
# das.click(('xpath', '//*[@id="projectForm"]/div[6]/div/div/dl/dd[2]'))
# #选择区域
# das.click(('xpath', '//*[@id="projectForm"]/div[7]/div/div/div'))
# das.click(('xpath', '//*[@id="projectForm"]/div[7]/div/div/dl/dd'))
# #点击添加
# das.click(('xpath', '//*[@id="layui-layer8"]/div[3]/a[1]'))


time.sleep(5)
d.close()