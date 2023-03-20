import pytest

from common.base import Base
from common.getdata import get_data

tcs = get_data("D:\code\DAS_KDT\\testdata\case2.xls", 'login')

class TestDASLogin:
    @pytest.fixture(scope='function')
    def open_das(self, driver):
        '''每次用例回到界面首页'''
        self.das = Base(driver)

    @pytest.mark.compare
    @pytest.mark.parametrize('tc', tcs)
    def test_do_login(self, open_das, tc):
        '''进入DAS项目空间'''
        from common.parseFunction import do_step
        results, result = do_step(self.das, tc.steps)
        print(f"测试用例{tc.tcno}-{tc.title}执行结果为：{results}")
        assert result is True


if __name__ == '__main__':
    pytest.main(['-v', 's', '-m', 'compare', 'test_01_login.py'])