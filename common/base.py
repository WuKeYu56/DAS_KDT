import random
import time

import pyautogui as ui
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


# driver = webdriver.Chrome()
# driver.maximize_window()
class Base:
    '''基于原生的selenium做二次封装'''
    def __init__(self, driver):#初始化self,driver
        self.driver = driver
        self.timeout = 10
        self.t = 0.5
        self.driver.maximize_window()

    def open(self, url):
        try:
            self.driver.get(url)
            return True
        except:
            return False

    def findElement(self, locator):
        '''定位到元素，返回元素的对象，没定位到，timeout异常'''
        if not isinstance(locator, tuple):#Isinstance的用法是用来判断一个量是否是相应的类型，接受的参数一个是对象加一种类型
            print('locator参数类型错误，必须传元组类型：loc=("id","value1")')
        else:
            print('正在定位元素信息：定位方式->%s,value值—>%s'%(locator[0], locator[1]))#返回一个元组取下标0和1
            ele = WebDriverWait(self.driver,
                                self.timeout,
                                self.t).until(EC.presence_of_element_located(locator))#显性等待方法
            return ele

    def findElements(self, locator):
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元组类型：loc=("id","value1")')
        else:
            try:
                print('正在定位元素信息：定位方式->%s,value值—>%s'%(locator[0],locator[1]))
                eles = WebDriverWait(self.driver,
                                   self.timeout,
                                   self.t).until(EC.presence_of_element_located(locator))#显性等待方法
                return eles
            except:
                return []

    def isElementExist(self, locator):
        try:
            self.findElement(locator)
            return True
        except:
            return False

    def sendkeys(self, locator, text=''):
        try:
            ele = self.findElement(locator)
            ele.send_keys(text)
            return True
        except:
            return False


    def click(self, locator):#点击方法
        try:
            if locator[0] == "link_text":
                locator = list(locator)
                locator[0] = "link text"
                locator = tuple(locator)
            print(locator)
            ele = self.findElement(locator)
            ele.click()
            return True
        except:
            return False

    def clear(self, locator):#清除方法
        try:
            ele = self.findElement(locator)
            ele.clear()
            return True
        except:
            return False


    def isSelected(self, locator):
        '''判断元素是否被选中，返回bool布尔值'''
        ele=self.findElement(locator)
        r=ele.is_selected()#判断元素是否被选中并返回
        return r

    def is_title(self,_title=''):
        '''返回bool值'''
        try:
            result=WebDriverWait(self.driver,
                                 self.timeout,
                                 self.t).until(EC.title_ls(_title))
            return result
        except:
            return False

    def is_title_contains(self,_title=''):
        '''返回bool值'''
        try:
            result = WebDriverWait(self.driver,
                                   self.timeout,
                                   self.t).until(EC.title_contains(_title))
            return result
        except:
            return False

    # def is_text_in_element(self, locator, _text=''):
    #     '''返回bool值'''
    #     if not isinstance(locator, tuple):
    #         print('locator参数类型错误，必须传元组类型：loc=("id","value1")')
    #         try:
    #             result = WebDriverWait(self.driver,
    #                                    self.timeout,
    #                                    self.t).until(EC.text_to_be_present_in_element(locator, _text))
    #             return result
    #         except:
    #             return False

    def is_text_in_element(self, locator, _text=''):
        '''返回bool值'''
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元组类型：loc=("id","value1")')
        try:
            text = self.get_text(locator)
            print(text, _text)
            if text == _text:
                return True
            else:
                return False
        except:
            return False

    def is_value_in_element(self, locator, _value=''):
        '''返回bool值,value为空字符串，返回Fasle'''
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元组类型：loc=("id","value1")')
            try:
                result = WebDriverWait(self.driver,
                                       self.timeout,
                                       self.t).until(EC.text_to_be_present_in_element_value(locator, _value))
                return result
            except:
                return False

    def is_alert(self, timeout=3):
        try:
            result = WebDriverWait(self.driver, timeout, self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    def get_title(self):
        '''获取title'''
        return self.driver.title

    def get_text(self,locator):
        '''获取文本'''
        try:
            t = self.findElement(locator).text
            return t
        except:
            print('获取text失败，返回”“')
            return ""

    def get_attribute(self, locator, name):
        '''获取属性'''
        try:
            element = self.findElement(locator)
            return element.get_attribute(name)
        except:
            print('获取%s属性失败，返回""'%name)
            return ""

    def js_focus_element(self,locator):
        '''聚焦元素'''
        target=self.findElement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();",target)

    def js_scroll_top(self):
        '''滚动到顶部'''
        js='window.scrollTo(0,0)'
        self.driver.execute_script(js)

    def js_scroll_end(self,x=0):
        '''滚动到底部'''
        js = 'window.scrollTo(%s,document.body.scrollHeight)'%x
        self.driver.execute_script(js)

    def select_by_index(self, locator, index=0):
        '''通过索引，index是索引第几个，从0开始，默认选第一个'''
        element = self.findElement(locator)#定位select这一栏
        Select(element).select_by_index(index)

    def select_by_value(self, locator, value):
        '''通过value属性'''
        element = self.findElement(locator)
        Select(element).select_by_value(value)

    def select_by_text(self, locator, text):
        '''通过文本值定位'''
        element = self.findElement(locator)
        Select(element).select_by_visible_text(text)

    def switch_iframe(self, id_index_locator):
        '''切换iframe'''
        try:
            if isinstance(id_index_locator, int):
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator, str):
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator, tuple):
                ele = self.findElement(id_index_locator)
                self.driver.switch_to.frame(ele)
        except:
            print('iframe切换异常')

    def switch_handle(self, window_name):
        self.driver.switch_to.window(window_name)

    def switch_alert(self):
        r = self.is_alert()
        if not r:
            print('alert不存在')
        else:
            return r

    def move_to_element(self, locator):
        '''鼠标悬停操作'''
        try:
            ele = self.findElement(locator)
            ActionChains(self.driver).move_to_element(ele).perform()
            return True
        except:
            return False

    def mapping_inn_disease(self, num_type):
        """通过鼠标操作绘制病害"""
        if not isinstance(num_type, tuple):
            print('num_type参数类型错误，必须传元组类型：num_type=(num, type) 其中num为点击次数，type为绘制类型')
        else:
            ui.FAILSAFE = True
            #基于屏幕分辨率获取中心点
            m, n = ui.size()
            x1, y1 = (m*840)/2880, n/2
            ui.click(x1, y1, button='left')
            ui.scroll(400)
            time.sleep(2)

            if num_type[1] == '':
                type = 'polyline'
            else:
                type = num_type[1]
            num = int(num_type[0])

            #绘制不同类型病害
            if type == 'polyline':
                self.click(('xpath', '//*[@id="maptop"]/div[2]/div[1]/div[1]/div[1]/div/a[1]'))
                ui.click(x1, y1, button='left')  #点击中心点开始绘制
                for i in range(num):
                    x2 = x1+random.randint(0, 200)  #可改变数字调节点击位置
                    y2 = y1+random.randint(0, 200)
                    ui.click(x2, y2, button='left')
                    time.sleep(1)
                ui.click(x2, y2, button='left')
                print('已点击末点')

            elif type == "polygon":
                self.click(('xpath', '//*[@id="maptop"]/div[2]/div[1]/div[1]/div[1]/div/a[2]'))
                ui.click(x1, y1, button='left')  #点击中心点开始绘制
                for i in range(num):
                    x2 = x1+random.randint(0, 200)  #可改变数字调节点击位置
                    y2 = y1+random.randint(0, 200)
                    ui.click(x2, y2, button='left')
                    time.sleep(1)
                ui.click(x1, y1, button='left')
                print('已点击中心点')
            else:
                print('请输入正确的参数：type=polyline/polygon')
            return True

    def mapping_sur_disease(self, num_type):
        """通过鼠标操作绘制病害"""
        if not isinstance(num_type, tuple):
            print('num_type参数类型错误，必须传元组类型：num_type=(num, type) 其中num为点击次数，type为绘制类型')
        else:
            ui.FAILSAFE = True
            #基于屏幕分辨率获取中心点
            m, n = ui.size()
            x1, y1 = m/2, n/2
            ui.click(x1, y1, button='left')
            ui.scroll(400)

            if num_type[1] == '':
                type = 'polyline'
            else:
                type = num_type[1]
            num = int(num_type[0])

            #绘制不同类型病害
            if type == 'polyline':
                self.click(('xpath', '//*[@id="mapid"]/div[2]/div[1]/div/div[1]/div/a[1]'))
                ui.click(x1, y1, button='left')  #点击中心点开始绘制
                for i in range(num):
                    x2 = x1+random.randint(0, 200)  #可改变数字调节点击位置
                    y2 = y1+random.randint(0, 200)
                    ui.click(x2, y2, button='left')
                    time.sleep(1)
                ui.click(x2, y2, button='left')
                print('已点击末点')

            elif type == "polygon":
                self.click(('xpath', '//*[@id="mapid"]/div[2]/div[1]/div/div[1]/div/a[2]'))
                ui.click(x1, y1, button='left')  #点击中心点开始绘制
                for i in range(num):
                    x2 = x1+random.randint(0, 200)  #可改变数字调节点击位置
                    y2 = y1+random.randint(0, 200)
                    ui.click(x2, y2, button='left')
                    time.sleep(1)
                ui.click(x1, y1, button='left')
                print('已点击中心点')

            elif type == "stake":
                time.sleep(2)
                ui.click(x1, y1, button='left')  #点击中心点开始绘制
                for i in range(num):
                    x2 = x1+random.randint(0, 200)  #可改变数字调节点击位置
                    y2 = y1+random.randint(0, 200)
                self.click(('xpath', '//*[@id="mapid"]/div[2]/div[1]/div/div[1]/div/a[4]'))
                ui.click(x2, y2, button='left')
                print("确定桩号位置")
            else:
                print('请输入正确的参数：type=polyline/polygon')
            return True



if __name__ == '__main__':
    driver = webdriver.Chrome
    web = Base(driver)
    driver.get('https://home.cnblogs.com/u/yoyoketang/')
    loc_1 = ('id', 'header_user_left')
    t = web.get_text(loc_1)