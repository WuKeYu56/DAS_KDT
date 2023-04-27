import pytest

from common.base import Base
from common.getdata import get_data
from common.parseFunction import do_step
from pages.loginpage import login

#测试用例的文件路径及所测试模块名
tcs = get_data("D:\code\DAS_KDT\\testdata\case2.xls", '2DView')

class TestDASProject:
    @pytest.fixture(scope='function')
    def open_das(self, driver):
        '''每次用例回到界面首页'''
        self.das = Base(driver)
        login(driver)

    @pytest.mark.compare
    @pytest.mark.parametrize('tc', tcs)
    def test_do_imgAnalysis(self, open_das, tc):
        '''进入DAS项目管理界面'''
        results, result = do_step(self.das, tc.steps)
        print(f"测试用例{tc.tcno}-{tc.title}执行结果为：{results}")
        assert result is True

if __name__ == '__main__':
    pytest.main(['-v', 'test_05_2DView.py'])