import pytest

from common.base import Base

# url = "http://11.0.0.167:9103/v2/site/record.html?siteId=100024"
url = "http://home.gm-robot.com:9103/v2/site/record.html?siteId=100028"
#进入项目管理页面测试

test_about_data = [
    (('id', 'siteDropdown'), '四川省成都市龙泉驿区西河镇车城大道辅路'),
    (('xpath', '//button[@ng-click="addTask()"]'), '创建任务'),
    (('xpath', '//button[@ng-click="addProject()"]'), '创建工程')
]


class TestDASProject:
    @pytest.fixture(scope='function')
    def open_das(self, driver):
        '''每次用例回到界面首页'''
        self.das = Base(driver)
        driver.get(url)

    # @pytest.mark.title
    # @pytest.mark.parametrize()
    # def test_01(self, driver, open_das):
    #     '''关于禅道——升级专业版本'''
    #     t1 = driver.title
    #     print('获取到的Text文本为：%s'%t1)
    #     assert t1 == 'DAS-项目管理'

    @pytest.mark.compare
    @pytest.mark.parametrize('local_about,expect', test_about_data)
    def test_02(self, open_das, local_about, expect):
        '''关于禅道-官方网站'''
        t1 = self.das.get_text(local_about)
        print('获取到的Text文本为：%s' % t1)
        assert t1 == expect


if __name__ == '__main__':
    pytest.main(['-v', '-m', 'compare', 'test_after_login.py'])