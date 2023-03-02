import time

import pytest

from common.base import Base
from common.getdata import get_data
from pages.loginpage import login

#测试用例的文件路径及所测试模块名
tcs = get_data("D:\code\DAS_KDT\\testdata\case2.xls", 'projects')

class TestDASProject:
    @pytest.fixture(scope='function')
    def open_das(self, driver):
        '''每次用例回到界面首页'''
        self.das = Base(driver)
        login(driver)

    @pytest.mark.compare
    @pytest.mark.parametrize('tc', tcs)
    def test_do_project(self, open_das, tc):
        '''进入DAS项目管理界面'''
        results = []
        for step in tc.steps:
            key = step["key"]
            obj = step["object"]
            obj = tuple(obj.split('=', 1))
            if hasattr(self.das, key):
                func = getattr(self.das, key)
                if len(step) == 2:
                    if len(obj) == 1:
                        rlt = func(obj[0])
                    else:
                        if key == 'open':
                            obj = obj[0]+'='+obj[1]
                            print(f'函数open链接：{obj}')
                        rlt = func(obj)
                elif len(step) == 3:
                    rlt = func(obj, step["param"])
                results.append(rlt)
            else:
                print("传入关键字错误，请检查用例")
                results.append(False)
            if "" not in results and False not in results:
                result = True
            else:
                result = False
            time.sleep(1)
        print(f"测试用例{tc.tcno}-{tc.title}执行结果为：{results}")
        assert result is True

if __name__ == '__main__':
    pytest.main(['-v', 's', '-m', 'compare', 'test_01_login.py'])